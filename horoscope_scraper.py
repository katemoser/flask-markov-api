import requests
from bs4 import BeautifulSoup
from datetime import date

from Markov import MarkovMachine


# Commented out after refactoring
# -- will delete later, after i make sure it didn't break
#
# today = date.today()
# MONTH = today.strftime("%B")
# DAY = today.strftime("%d")
# YEAR = today.strftime("%Y")

# signs = [
#     "test",
#     "aries",
#     "taurus",
#     "gemini",
#     "cancer",
#     "leo",
#     "virgo",
#     "libra",
#     "scorpio",
#     "sagittarius",
#     "capricorn",
#     "aquarius",
#     "pisces"
# ]

# websites= {
#     "horoscope.com": {
#         "base" : "https://www.horoscope.com/us/",
#         "daily" : "horoscopes/general/horoscope-general-daily-today.aspx?sign=",
#     },
#     "astrostyle.com":{
#         "base" : "https://astrostyle.com/horoscopes/",
#         "daily": "daily/",
#     },
#     "chaninicolas.com": {
#         "base": "https://chaninicholas.com/",
#         "daily": "-free-daily-horoscope-",
#     },

# }

# sign = 12

# def first(sign_num):
#     site = websites["horoscope.com"]
#     page = requests.get(f'{site["base"]}{site["daily"]}{sign_num}')

#     soup = BeautifulSoup(page.content, "html.parser")
#     result = soup.find(class_="main-horoscope").find("p").text
#     horoscope =result.split("-", 1)[1].strip()
#     print(f'{site["base"]}: {horoscope}')


# def second(sign_num):
#     site = websites["astrostyle.com"]
#     page = requests.get(f'{site["base"]}{site["daily"]}{signs[sign_num]}')

#     soup = BeautifulSoup(page.content, "html.parser")
#     result = soup.find(class_="horoscope-content").find("p").text
#     horoscope =result.strip()
#     print(f'{site["base"]}: {horoscope}')

# def third(sign_num):
#     site = websites["chaninicolas.com"]
#     date = f'{MONTH}-{DAY}-{YEAR}'
#     page = requests.get(f'{site["base"]}{signs[sign_num]}{site["daily"]}{date}')

#     soup = BeautifulSoup(page.content, "html.parser")
#     result = soup.find(class_="entry-content").find_all("p")[1].text
#     horoscope = result.strip()
#     print(f'{site["base"]}: {horoscope}')


class HoroScraper:
    """Class for web scraping horoscopes"""

    def __init__(self):
        today = date.today()
        self.date = {
            "month": today.strftime("%B"),
            "day": today.strftime("%d"),
            "year": today.strftime("%Y"),
        }

        self.signs = {
            # "aries": Horoscope(1),
            "taurus": Horoscope(2),
            "gemini": Horoscope(3),
            "cancer": Horoscope(4),
            "leo": Horoscope(5),
            "virgo": Horoscope(6),
            "libra": Horoscope(7),
            "scorpio": Horoscope(8),
            "sagittarius": Horoscope(9),
            "capricorn": Horoscope(10),
            "aquarius": Horoscope(11),
            "pisces": Horoscope(12),
        }

        self.websites= {
            "horoscope.com": {
                "base" : "https://www.horoscope.com/us/",
                "daily" : "horoscopes/general/horoscope-general-daily-today.aspx?sign=",
            },
            "astrostyle.com":{
                "base" : "https://astrostyle.com/horoscopes/",
                "daily": "daily/",
            },
            "chaninicolas.com": {
                "base": "https://chaninicholas.com/",
                "daily": "-free-daily-horoscope-",
            },
            "ganeshaspeaks.com": {
                "base" : "https://www.ganeshaspeaks.com/horoscopes/",
                "daily" : "daily-horoscope/",
            },
            "mpanchang.com": {
                "base" : "https://www.mpanchang.com/horoscope/",
                "daily" : "daily-horoscope/",
            }
        }

        self._populate()

    def generate_daily(self, sign):
        """using the markov machine to generate a horoscope"""
        input = " @ ".join(self.signs[sign].daily)
        mm = MarkovMachine(input)

        return mm.get_text()


    def _populate(self):
        """populates daily, weekly, monthly, yearly for each sign"""
        for sign in self.signs:
            self._populate_daily(sign)

    def _populate_daily(self, sign):
        """populates daily horoscopes for one sign"""

        # get from horoscope.com
        site = self.websites["horoscope.com"]
        page = requests.get(
            f'{site["base"]}{site["daily"]}{self.signs[sign].number}'
        )

        soup = BeautifulSoup(page.content, "html.parser")
        result = soup.find(class_="main-horoscope").find("p").text
        horoscope =result.split("-", 1)[1].strip()
        self.signs[sign].daily.append(horoscope)

        # get from astrostyle.com
        site = self.websites["astrostyle.com"]
        page = requests.get(
            f'{site["base"]}{site["daily"]}{sign}')

        soup = BeautifulSoup(page.content, "html.parser")
        result = soup.find(class_="horoscope-content").find("p").text
        horoscope =result.strip()
        self.signs[sign].daily.append(horoscope)

        # get from chaninicolas.com
        # site = self.websites["chaninicolas.com"]
        # today = f'{self.date["month"]}-{self.date["day"]}-{self.date["year"]}'
        # page = requests.get(f'{site["base"]}{sign}{site["daily"]}{today}/')

        # soup = BeautifulSoup(page.content, "html.parser")
        # try:
        #     result = soup.find(class_="entry-content").find_all("p")[1].text
        #     horoscope = result.strip()
        #     self.signs[sign].daily.append(horoscope)
        # except(AttributeError):
        #     pass

        # get from ganeshaspeaks.com
        # site = self.websites["ganeshaspeaks.com"]
        # page = requests.get(f'{site["base"]}{site["daily"]}{sign}/')

        # soup = BeautifulSoup(page.content, "html.parser")
        # result = soup.find(id="horo_content").text
        # horoscope = result.strip()
        # self.signs[sign].daily.append(horoscope)

        # astroyogi.com
        site = self.websites["mpanchang.com"]
        print(f'{site["base"]}{site["daily"]}{sign}-daily-horoscope/')
        page = requests.get(f'{site["base"]}{site["daily"]}{sign}-daily-horoscope/')

        soup = BeautifulSoup(page.content, "html.parser")
        result = (soup
            .find("h2", string=lambda text: "daily horoscope" in text.lower())
            .find_next_sibling()
            .text
        )
        horoscope = result.strip()
        self.signs[sign].daily.append(horoscope)


class Horoscope:
    """Class for keeping track of web-scraped horoscopes"""

    def __init__(self, sign_num):
        self.number = sign_num
        self.daily = []
        self.weekly = []
        self.monthly = []
        self.yearly = []

    def __repr__(self):
        return f'Daily for {self.number}: {self.daily}'





