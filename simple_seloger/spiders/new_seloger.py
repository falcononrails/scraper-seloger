import scrapy
import scrapy.cmdline

from scrapy.loader import ItemLoader
from simple_seloger.items import AnnonceItem

import json
import logging


class SelogerSpider(scrapy.Spider):
    name = "seloger"

    # Support user giving the starting url to the scraper from the CLI
    def __init__(self, *args, **kwargs):
        super(SelogerSpider, self).__init__(*args, **kwargs)

        self.start_urls = [kwargs.get('search_url')]

    # Parse the data we get from parsing the current page

    def parse(self, response):
        # For every annonce in the response
        for annonce in response.xpath("//div[@class='c-pa-info']"):
            # Load the following attributes into AnnonceItem
            loader = ItemLoader(item=AnnonceItem(),
                                selector=annonce, response=response)
            loader.add_xpath(
                'type_bien', ".//a[@class='c-pa-link link_AB']/text()")
            loader.add_xpath(
                'prix', ".//div[@class='c-pa-price']/span[@class='c-pa-cprice']")
            loader.add_xpath(
                'surface', ".//div[@class='c-pa-criterion']/em[contains(text(), '²')]")

            loader.add_xpath('ville', "//div[@class='c-pa-city']")

            # Filter annonces by plateforme for formatting purposes
            if(annonce.xpath(".//a[@class='c-pa-link link_AB']/@href").extract_first().find('neuf') != -1):
                loader.add_value('plateforme', "seloger_neuf")
            elif(annonce.xpath(".//a[@class='c-pa-link link_AB']/@href").extract_first().find('construire') != -1):
                loader.add_value('plateforme', "seloger_construire")
            else:
                loader.add_value('plateforme', "seloger")

            # Get the IDs of every annonce to get (les +, general, exterieur) using the parse_json_info method
            annonce_id = annonce.xpath(
                ".//div[@class='h-fi-pulse annonce__detail__sauvegarde']/@data-idannonce").extract_first()

            # Send a request to get additional data for each annonce
            yield scrapy.Request(url="https://www.seloger.com/detail,json,caracteristique_bien.json?idannonce={0}".format(annonce_id), callback=self.parse_json_info, meta={'loader': loader})

            # Moving on to the next page to support pagination
            try:
                next_page_url = "https:" + response.xpath(
                    "//a[@class='pagination-next']/@href").extract_first()
                if next_page_url:
                    yield scrapy.Request(url=next_page_url, callback=self.parse)
            except TypeError:
                logging.info("No more pages to crawl")

    # Parse the required additional info from the returned JSON object returned by seloger
    def parse_json_info(self, response):
        # Get the loader sent by the parse method to fill the remaining fields in our annonce item
        loader = response.request.meta['loader']

        categories = json.loads(response.body).get('categories')

        diag_perf_energie = json.loads(
            response.body).get('energie').get('chiffre')
        indice_gaz = json.loads(response.body).get('ges').get('chiffre')

        les_plus_array = categories[0].get('criteria')
        general_array = categories[1].get('criteria')
        interieur_array = categories[2].get('criteria')
        exterieur_array = categories[3].get('criteria')

        les_plus = [list(dict_item.values())[0]
                    for dict_item in les_plus_array]
        general = [list(dict_item.values())[0]
                   for dict_item in general_array]
        interieur = [list(dict_item.values())[0]
                     for dict_item in interieur_array]
        exterieur = [list(dict_item.values())[0]
                     for dict_item in exterieur_array]

        loader.add_value('les_plus', les_plus)
        loader.add_value('general', general)
        loader.add_value('interieur', interieur)
        loader.add_value('exterieur', exterieur)
        loader.add_value('diag_perf_energie', diag_perf_energie)
        loader.add_value('indice_gaz', indice_gaz)

        # Yield the collected item
        yield loader.load_item()
