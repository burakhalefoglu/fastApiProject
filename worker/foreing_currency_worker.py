
from datetime import datetime
from core.libraries.isyatirim.isyatirim_historical_datas import IsYatirimHistoricalData
from helper.helper import Helper
from service.isyatirim.investment_item_historical_service import InvestmentItemHistoricalService



class ForeignCurrencyWorker:

    async def foreign_currency_worker_services(self):
        is_yatirim_data_sources = IsYatirimHistoricalData()
        h = Helper()
        bist_securities_hist_services = InvestmentItemHistoricalService()
        for code in ['USD/RUB', 'USD/CAD', 'USD/KWD', 'USD/BRL', 'USD/NOK', 'USD/COP', 'USD/CNH', 'USD/UYU',
                 'USD/DKK', 'USD/DZD', 'USD/INR', 'USD/SAR', 'USD/SEK', 'USD/ZAR', 'USD/JOD', 'USD/KRW',
                 'USD/AZN', 'USD/ARS', 'USD/BHD', 'USD/CHF', 'USD/CLP', 'USD/JPY', 'USD/QAR', 'USD/NZD',
                 'USD/NOK', 'USD/COP', 'USD/CRC', 'USD/CSK', 'USD/EGP', 'USD/GEL', 'USD/GHS', 'USD/HKD',
                 'USD/HRK', 'USD/HUF', 'USD/ILS', 'USD/IQD', 'USD/IRR', 'USD/ISK', 'USD/KZT', 'USD/LBP',
                 'USD/LKR', 'USD/LYD', 'USD/MAD', 'USD/MDL', 'USD/MKD', 'USD/MZN', 'USD/MXN', 'USD/MYR',
                 'USD/PHP', 'USD/PKR', 'USD/RSD', 'USD/SGD', 'USD/SYP', 'USD/TMT', 'USD/TWD', 'USD/UAH',
                 'USD/UZS', 'GBP/USD', 'EUR/USD', 'EUR/AED', 'BTC/TRY', 'CHF/TRL', 'GBP/TRL', 'EUR/TRL',
                 'USD/TRL']:
            today = datetime.now()
            hist_data = is_yatirim_data_sources.get_isyatirim_from_to_historical_datas(code=code,
                                                                                    query="",
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
            # await bist_securities_hist_services.save_historical_data_async(table="foreign_currency_hist_data",
            #                                                             code=code,
            #                                                             date=today,
            #                                                             data=hist_data)


