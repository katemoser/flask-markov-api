
from horoscope_scraper import HoroScraper
from app import db
from models import HoroscopeSeed

def scrape_and_insert_daily_horoscopes():
    """ runs a web scraper and adds the scraped horoscopes to db"""
    scraper = HoroScraper()

    ## for each sign
    for sign in scraper.signs:

        ## for each horoscope found for sign
        for horo_text in scraper.signs[sign].daily:
            daily_horoscope = HoroscopeSeed(
                type="daily",
                sign_name=sign,
                text=horo_text,
                source="test"
            )
            print("horoscope for", sign)
            print("horoscope instance:", daily_horoscope )
            print("horoscope text is", daily_horoscope.text)

            db.session.add(daily_horoscope)
            db.session.commit()


