[![Python 3.6.5](https://img.shields.io/badge/python-3.6.5-blue.svg)](https://www.python.org/downloads/release/python-365/)
## Overview  
This is a scraper for the website [seloger.com](https://www.seloger.com), built using [Scrapy](https://github.com/scrapy/scrapy/tree/1.7).

## Setup
- Install virtualenv `pip install virtualenv`
- Create a new virtual workspace `virtualenv my_workspace && cd my_workspace`
- Clone the project into your workspace folder:    
`git clone https://github.com/falcononrails/scraper-seloger.git` and navigate to it `cd scraper-seloger`
- Install the required packages `pip install -r requirements.txt`

## Usage
Go to the project folder 
```bash
cd ~/my_workspace/scraper-seloger/simple_seloger
```
Run the spider using the URL of your search query on [seloger.com](https://www.seloger.com)
```bash
scrapy crawl seloger -a search_url="https://www.seloger.com/list.htm?tri=initial&enterprise=0&idtypebien=2,1&pxMax=1000000&idtt=2,5&naturebien=1,2,4&ci=910377"
```
You can use the **-o** option to specify an output file (JSON or CSV):
```bash
scrapy crawl seloger -o annonces.csv -a search_url="https://www.seloger.com/list.htm?tri=initial&enterprise=0&idtypebien=2,1&pxMax=1000000&idtt=2,5&naturebien=1,2,4&ci=910377"
```
## Exporting the data to MongoDB 

- Make sure you have MongoDB installed and its deamon running.
- Change *MONGO_URI* and *MONGO_DB* in the **settings.py** file of the project.  
A typical scenario is `MONGO_URI = mongodb://localhost:27017` and `MONGO_DB = seloger`
- You can use [Robo 3T](https://robomongo.org/) to see your database and manipulate the data.

## Deploying on Heroku

The repo has all the files you need to deploy to Heroku, I'll clarify the steps below.
- Install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#download-and-install)
- Create a a new Heroku app `heroku create seloger-demo`
- Add the new app as a remote `heroku git:remote -a seloger-demo`
- Change the **url** argument under the **[deploy:local]** section in the *scrapy.cfg* file to `url = https://seloger-demo.herokuapp.com/`
- Add `git add .` and commit everything `git commit -m "first commit"`
- Finally push to Heroku and watch your app deploy `git push heroku master`

The **scrapyd** interface is now accessible through `https://seloger-demo.herokuapp.com/`

To start a job through scrapyd, run the following from your terminal:

```bash
curl https://seloger-demo.herokuapp.com/schedule.json -F project=default -F spider=seloger 
-F search_url="https://www.seloger.com/list.htm?tri=initial&enterprise=0&idtypebien=2,1&pxMax=1000000&idtt=2,5&naturebien=1,2,4&ci=910377"
```
## Adding MongoDB Lab module through Heroku
- Add the add-on to your existing app `heroku addons:create mongolab:sandbox --app seloger-demo`
- Get the mLab URI `heroku config:get MONGODB_URI --app seloger-demo`
- Replace *MONGO_URI* and *MONGO_DB* in the **settings.py** file of the project with the values returned in your terminal.
- Example: 
```python
MONGO_URI = 'mongodb://heroku_v10nm298:kj9ouu5ckrbmcoud5ib55041hv@ds137740.mlab.com:37740/heroku_v10nm298'
MONGO_DB = 'heroku_v10nm298'
```
The data you scrape will now be saved in an external cloud MongoDB database linked with your Heroku app.
