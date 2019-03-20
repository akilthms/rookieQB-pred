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
        self.rookie_list

    def get_my_rookies(self):
        rookie_qbs = []
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
                    rookie_qbs.append(cols[1].find(name='a').text)
                    print("Name: ", cols[1].find(name='a').text, "Count: ", (len(rookie_QBs)))
            sleep(self.timeout)
            self.rookie_list = rookie_qbs
        print("The function has finished running!!!")
        return rookie_qbs

    def get_college_stats(self,Rookie):
        # manipulate url
        Rookie = Rookie.lower().replace(" ", "-")
        url = 'http://www.sports-reference.com/cfb/players/' + Rookie + '-1.html'
        r = requests.get(url)
        # create beautifulSoup object
        b = BeautifulSoup(r.text)
        # find our row with the career stats of the NFL Rookie QB in college
        row = b.find(name='tfoot').find(name='tr')
        # cols will hold all of our stats we then use indexing/slicing to access each specific stat
        cols = row.find_all(name='td')
        pass_completions = cols[6].text
        attempts = cols[7].text
        pass_completion_precentage = cols[8].text
        passing_yards = cols[9].text
        passing_yards_per_attempt = cols[10].text
        adjusted_passing_yards_per_attempt = cols[11].text
        pass_TDs = cols[12].text
        pass_interceptions = cols[13].text
        passing_effeciency_rating = cols[14].text

        stats_row = [pass_completions, attempts, pass_completion_precentage, passing_yards, passing_yards_per_attempt,
                     adjusted_passing_yards_per_attempt, pass_TDs, pass_interceptions, passing_effeciency_rating]
        stats_row = [float(stat) for stat in stats_row]
        return stats_row

    #defining a function to get all of our stats for our rookies.
    def rookieStatsRoundUp(self, Rookie_List):
        Player_and_Stats = {}
        for rookie in Rookie_List:
            Player_and_Stats[rookie] = self.getCollegeStats(rookie)
            sleep(2)
        return Player_and_Stats

    print(rookieStatsRoundUp(rookie_list))

