from flask import Flask
import pandas as pd
from bs4 import BeautifulSoup
import requests
from scrapper import QbScrapper

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/rookie-data/<position>')
def get_rookie_data(position):
    print(position)
    if position == 'qb':
        seasons = range(2014, 1979, -1)
        scrapper = QbScrapper(seasons)
        return scrapper.getMyRookies()


if __name__ == '__main__':
    app.run(debug=True)
