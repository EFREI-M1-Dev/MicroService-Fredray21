from sqlalchemy import (Column, Integer, MetaData, String, Table, create_engine, ARRAY)

from databases import Database
import os

# DATABASE_URL = 'postgresql://postgres:root@localhost/movie_db'
# get the database uri from the environment variable
DATABASE_URI = os.getenv('DATABASE_URI')

# create the engine and metadata
engine = create_engine(DATABASE_URI)
metadata = MetaData()

# create the casts table
movies = Table(
    'movies',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('plot', String(250)),
    Column('genres', ARRAY(String)),
    Column('casts_id', ARRAY(Integer))
)

# create the database connection
database = Database(DATABASE_URI)