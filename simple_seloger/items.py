import scrapy
from scrapy.loader.processors import MapCompose, Identity, Join, TakeFirst
from w3lib.html import remove_tags


def remove_quotations(value):
    return value.replace(u"\u00a0", '').replace(u"\u20ac", '').replace('"', '')


def format_surface(value):
    return value.replace("m²", '')


class AnnonceItem(scrapy.Item):
    plateforme = scrapy.Field(
        input_processor=MapCompose(str.strip),
        output_processor=TakeFirst()
    )
    type_bien = scrapy.Field(
        input_processor=MapCompose(remove_tags, str.strip),
        output_processor=TakeFirst()
    )
    prix = scrapy.Field(
        input_processor=MapCompose(
            remove_tags, remove_quotations, str.strip),
        output_processor=TakeFirst()
    )
    surface = scrapy.Field(
        input_processor=MapCompose(
            remove_tags, format_surface, remove_quotations, str.strip),
        output_processor=TakeFirst()
    )
    ville = scrapy.Field(
        input_processor=MapCompose(remove_tags),
        output_processor=TakeFirst()
    )
    les_plus = scrapy.Field(
        input_processor=MapCompose(remove_tags, remove_quotations),
        output_processor=Identity()
    )
    general = scrapy.Field(
        input_processor=MapCompose(remove_tags, remove_quotations),
        output_processor=Identity()
    )
    interieur = scrapy.Field(
        input_processor=MapCompose(remove_tags, remove_quotations),
        output_processor=Identity()
    )
    exterieur = scrapy.Field(
        input_processor=MapCompose(remove_tags, remove_quotations),
        output_processor=Identity()
    )
    diag_perf_energie = scrapy.Field(
        input_processor=MapCompose(),
        output_processor=TakeFirst()
    )
    indice_gaz = scrapy.Field(
        input_processor=MapCompose(),
        output_processor=TakeFirst()
    )
