from sqlalchemy import create_engine
from env import settings


def get_engine():
    db_url = settings.DB_URL
    return create_engine(db_url)