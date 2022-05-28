from core.libraries.scraper.scraper import ScraperApi
from datetime import datetime
from core.libraries.isyatirim.isyatirim_historical_datas import IsYatirimHistoricalData
from helper.helper import Helper
from service.isyatirim.investment_item_historical_service import InvestmentItemHistoricalService



class BistWorker:
    async def bist_worker_services(self):
        is_yatirim_data_sources = IsYatirimHistoricalData()
        bist_securities_hist_services = InvestmentItemHistoricalService()
        h = Helper()
        scrapers = ScraperApi()
        for code in scrapers.get_all_bist_company():
            today = datetime.now()
            hist_data = is_yatirim_data_sources.get_isyatirim_from_to_historical_datas(code=code,
                                                                                    query=".E.BIST",
                                                                                    from_date_year=str(
                                                                                        today.year),
                                                                                    from_date_month=h.date_obj_to_str(
                                                                                        today.month),
                                                                                    from_date_day=h.date_obj_to_str(
                                                                                        today.day),
                                                                                    from_date_hour="00",
                                                                                    from_date_minute="00",
                                                                                    to_date_year=str(
                                                                                        today.year),
                                                                                    to_month=h.date_obj_to_str(
                                                                                        today.month),
                                                                                    to_day=h.date_obj_to_str(
                                                                                        today.day),
                                                                                    to_hour="23",
                                                                                    to_minute="59"
                                                                                    )
         
            print("code : ", code, hist_data)
            # await bist_securities_hist_services.save_historical_data_async(table="bist_securities_hist_data",
            #                                                             code=code,
            #                                                             date=today,
            #                                                             data=hist_data)

