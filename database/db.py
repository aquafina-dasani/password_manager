from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base

# create the database to store our passwords and stuff
ENGINE = create_engine("sqlite:///passwd_vault.db")


local_session = sessionmaker(bind=ENGINE)()

# create tables in database
def create_tables():
    Base.metadata.create_all(ENGINE)
