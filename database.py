import os
import urllib

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

#load_dotenv(".env")

host_server = os.environ.get('host_server', 'localhost')
db_server_port = urllib.parse.quote_plus(str(os.environ.get('db_server_port', '5432')))
database_name = os.environ.get('database_name', 'item_db')
db_username = urllib.parse.quote_plus(str(os.environ.get('db_username', 'postgres')))
db_password = urllib.parse.quote_plus(str(os.environ.get('db_password', '123456')))
DATABASE_URL = 'postgresql://{}:{}@{}:{}/{}'.format(db_username, db_password, host_server, db_server_port, database_name)


engine=create_engine(f"postgresql://{db_username}:{db_password}@{host_server}/{database_name}",
    echo=True
)

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)
