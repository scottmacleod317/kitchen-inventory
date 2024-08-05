import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from google.cloud.sql.connector import Connector, IPTypes
import pg8000

# load env vars
load_dotenv()


def init_connection_engine(connector: Connector) -> Engine:
    instance_connection_name = os.getenv(
        "INSTANCE_CONNECTION_NAME"
    )  # e.g. 'project:region:instance'
    db_user = os.getenv("DB_USER")  # e.g. 'my-db-user'
    db_pass = os.getenv("DB_PASS")  # e.g. 'my-db-password'
    db_name = os.getenv("DB_NAME")  # e.g. 'my-database'

    ip_type = IPTypes.PRIVATE if os.getenv("PRIVATE_IP") else IPTypes.PUBLIC

    # initialize Cloud SQL Python Connector object
    connector = Connector()

    def getconn() -> pg8000.dbapi.Connection:
        conn: pg8000.dbapi.Connection = connector.connect(
            instance_connection_name,
            "pg8000",
            user=db_user,
            password=db_pass,
            db=db_name,
            ip_type=ip_type,
        )
        return conn

    # The Cloud SQL Python Connector can be used with SQLAlchemy
    # using the 'creator' argument to 'create_engine'
    pool = create_engine(
        "postgresql+pg8000://",
        creator=getconn,
        # ...
    )
    return pool


# initialize Python Connector and connection pool engine
connector = Connector()
engine = init_connection_engine(connector)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
