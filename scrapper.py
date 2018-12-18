from bs4 import BeautifulSoup
import requests
from time import sleep

"""
The purpose of this class is to create a Web scrapper that can compile a list of college football statistics for Rookie QBs.
"""


class QbScrapper:
    def __init__(self, seasons, site_name='nfl', timeout=1):
        self.seasons = seasons
        self.site_name = site_name
        self.timeout = timeout

    def getMyRookies(self):
        rookie_QBs = []
        for season in self.seasons:
            url = 'http://www.nfl.com/stats/categorystats?' \
                  'archive=false&' \
                  'conference=null&' \
                  'statisticCategory=PASSING&' \
                  'season=' + str(season) + \
                  '&seasonType=REG&' \
                  'experience=0&' \
                  'tabSeq=0&' \
                  'qualified=false&' \
                  'Submit=Go'
            r = requests.get(url)
            b = BeautifulSoup(r.text,features="html.parser")
            rows = b.find_all(name='tr')
            for row in rows[1:]:
                cols = row.find_all(name='td')
                position = cols[3].text
                attempts = int(cols[5].text)
                """
                Only extract Quarterbacks in their first year who threw more then 100 passes. This will give us a clean
                data-set of rookies that played for the majority of the season.
                """
                if position == 'QB' and attempts > 100:
                    rookie_QBs.append(cols[1].find(name='a').text)
                print(rookie_QBs)
            sleep(self.timeout)
        print("The function has finished running")
        return rookie_QBs

