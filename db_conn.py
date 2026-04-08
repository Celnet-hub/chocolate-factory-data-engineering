from sqlalchemy import create_engine
from env import settings


def get_engine():
    db_url = settings.DB_URL
    try:
        engine = create_engine(db_url)
        print("SQLAlchemy engine created successfully.")
        return engine
    except Exception as e:
        print(f"Engine creation failed: {e}")
        raise e