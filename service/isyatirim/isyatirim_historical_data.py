import datetime

from kink import inject
from core.aspects.exception.exception_aspect import exception_aspect
from core.aspects.log.log_aspect import log_aspect
from core.aspects.performance.performance_aspect import performance_aspect
from model.bist_historical_data_model import BistHistoricalData
from repository.i_repository_dal import IRepositoryDal


class BistSecuritiesHistoricalService:
    
    @exception_aspect  # must be last - 1
    @inject  # must be last - 2
    @log_aspect
    @performance_aspect(1)  # must be first
    async def save_historical_data_async(self,
                                         table: str,
                                         code: str,
                                         data: dict,
                                         data_access: IRepositoryDal):
        if len(data) == 0:
            return {}

        epoch_data_time = data[0]
        data_value = data[1]
        date_time = datetime.datetime.utcfromtimestamp(float(epoch_data_time) / 1000.)
        date_time_turkey = date_time + datetime.timedelta(hours=3)
        bist_historical_data = BistHistoricalData(
            code=code,
            value=data_value,
            date=date_time_turkey)
        await data_access.add_async(table, bist_historical_data)
