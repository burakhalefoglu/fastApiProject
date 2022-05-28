from kink import di

from repository.i_repository_dal import IRepositoryDal
from repository.mongodb.mongodb_dal import MongodbDal


def inject_dependencies():
    di[IRepositoryDal] = MongodbDal()

