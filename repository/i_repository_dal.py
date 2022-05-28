from abc import ABC, abstractmethod
from typing import Any, List


class IRepositoryDal(ABC):


    @abstractmethod
    async def get_transaction_session_async(self):
        pass

    @abstractmethod
    async def add_async(self, table: str, model: Any):
        pass

    @abstractmethod
    async def add_many_async(self, table: str, models: List):
        pass

    @abstractmethod
    async def get_all_with_client_id_async(self, table: str, client_id: str):
        pass

    @abstractmethod
    async def get_all_async(self, table: str):
        pass

    @abstractmethod
    async def get_by_id_async(self, table: str, _id: str, client_id: str):
        pass

    @abstractmethod
    async def get_by_filter_async(self, table: str, filters: dict):
        pass

    @abstractmethod
    async def get_list_by_filter_async(self, table: str, filters: dict):
        pass

    @abstractmethod
    async def update_async(self, table: str, query: dict, new_value: dict):
        pass

    @abstractmethod
    async def delete_async(self, table: str, query: dict):
        pass

    @abstractmethod
    async def delete_all_async(self, table: str, query: dict):
        pass
