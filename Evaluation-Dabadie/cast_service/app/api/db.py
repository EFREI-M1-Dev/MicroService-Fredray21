import os

from sqlalchemy import (Column, Integer, MetaData, String, Table,
                        create_engine, ARRAY)

from databases import Database
# get de database uri from the environment variable
DATABASE_URI = os.getenv('DATABASE_URI')

# create the engine and metadata
engine = create_engine(DATABASE_URI)
metadata = MetaData()

# create the casts table
casts = Table(
    'casts',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('nationality', String(20)),
)
# create the movies table
database = Database(DATABASE_URI)
