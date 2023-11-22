from app.api.models import CastIn, CastOut, CastUpdate
from app.api.db import casts, database

# function to create a cast
async def add_cast(payload: CastIn):
    query = casts.insert().values(**payload.dict())

    return await database.execute(query=query)

# function to get cast by id
async def get_cast(id):
    query = casts.select(casts.c.id==id)
    return await database.fetch_one(query=query)
