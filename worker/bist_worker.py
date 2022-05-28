from core.libraries.scraper.scraper import ScraperApi
from core.utilities.thread_job import ThreadJob
from worker.worker import event
from datetime import datetime
from core.libraries.isyatirim.isyatirim_historical_datas import IsYatirimHistoricalData
from service.isyatirim.isyatirim_historical_data import BistSecuritiesHistoricalService


def bist_worker_services():
    is_yatirim_data_sources = IsYatirimHistoricalData()
    bist_securities_hist_services = BistSecuritiesHistoricalService()
    scrapers = ScraperApi()
    for code in scrapers.get_all_bist_company():
        today = datetime.now()
        hist_data = is_yatirim_data_sources.get_isyatirim_from_to_historical_datas(code=code,
                                                                                   query=".E.BIST",
                                                                                   from_date_year=str(
                                                                                       today.year),
                                                                                   from_date_month=date_obj_to_str(
                                                                                       today.month),
                                                                                   from_date_day=date_obj_to_str(
                                                                                       today.day),
                                                                                   from_date_hour="00",
                                                                                   from_date_minute="00",
                                                                                   to_date_year=str(
                                                                                       today.year),
                                                                                   to_month=date_obj_to_str(
                                                                                       today.month),
                                                                                   to_day=date_obj_to_str(
                                                                                       today.day),
                                                                                   to_hour="23",
                                                                                   to_minute="59"
                                                                                   )
        print("code", code, hist_data)
        return
        await bist_securities_hist_services.save_historical_data_async(table="bist_securities_hist_data",
                                                                       code=code,
                                                                       date=today,
                                                                       data=hist_data)






bist_worker = ThreadJob(bist_worker_services, event, 2)
