from fastapi import FastAPI

from app.api.movies import movies
from app.api.db import metadata, database, engine

metadata.create_all(engine)

# create the app
app = FastAPI(openapi_url="/api/v1/movies/openapi.json", docs_url="/api/v1/movies/docs")

# create the database connection
@app.on_event("startup")
async def startup():
    await database.connect()

# close the database connection
@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# include the router
app.include_router(movies, prefix='/api/v1/movies', tags=['movies'])

