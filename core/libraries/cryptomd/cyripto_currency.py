import pandas as pd

from cryptocmd import CmcScraper


class CmcScraperCryptoApi:

    def get_historical_crypto_currency(self, code: str, from_day: str, from_month: str, from_year: str,
                                       to_day: str, to_month: str, to_year: str) -> pd.DataFrame:
        scraper = CmcScraper(code, f"{from_day}-{from_month}-{from_year}",
                             f"{to_day}-{to_month}-{to_year}", order_ascending=False, fiat="TRY")

        df = scraper.get_dataframe()
        return df

    def get_yesterday_crypto_currency(self, code: str) -> pd.DataFrame:
        scraper = CmcScraper(code, fiat="TRY")

        df = scraper.get_dataframe()
        return df.iloc[0]
