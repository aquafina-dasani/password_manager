from sqlalchemy.orm import DeclarativeBase, mapped_column
from sqlalchemy import Integer, String, Float, func

# Make it easier create tables in database
class Base(DeclarativeBase):
    pass

# User table, inherits Base
class User(Base):
    __tablename__ = "user"
    
    id = mapped_column(Integer, primary_key=True)
    username = mapped_column(String(250), nullable=False)
    hash_string = mapped_column(String(250), nullable=False)