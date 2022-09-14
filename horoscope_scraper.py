import requests
from bs4 import BeautifulSoup
from datetime import date

today = date.today()
MONTH = today.strftime("%B")
DAY = today.strftime("%d")
YEAR = today.strftime("%Y")
print(f'TODAY IS {MONTH} {DAY} {YEAR}')

signs = [
    "test",
    "aries",
    "taurus",
    "gemini",
    "cancer",
    "leo",
    "virgo",
    "libra",
    "scorpio",
    "sagittarius",
    "capricorn",
    "aquarius",
    "pisces"
]

websites= {
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

}

sign = 12

def first(sign_num):
    site = websites["horoscope.com"]
    page = requests.get(f'{site["base"]}{site["daily"]}{sign_num}')

    soup = BeautifulSoup(page.content, "html.parser")
    result = soup.find(class_="main-horoscope").find("p").text
    horoscope =result.split("-", 1)[1].strip()
    print(f'{site["base"]}: {horoscope}')


def second(sign_num):
    site = websites["astrostyle.com"]
    page = requests.get(f'{site["base"]}{site["daily"]}{signs[sign_num]}')

    soup = BeautifulSoup(page.content, "html.parser")
    result = soup.find(class_="horoscope-content").find("p").text
    horoscope =result.strip()
    print(f'{site["base"]}: {horoscope}')

def third(sign_num):
    site = websites["chaninicolas.com"]
    date = f'{MONTH}-{DAY}-{YEAR}'
    page = requests.get(f'{site["base"]}{signs[sign_num]}{site["daily"]}{date}')

    soup = BeautifulSoup(page.content, "html.parser")
    result = soup.find(class_="entry-content").find_all("p")[1].text
    horoscope = result.strip()
    print(f'{site["base"]}: {horoscope}')






print(signs[sign])
first(sign)
second(sign)
third(sign)


