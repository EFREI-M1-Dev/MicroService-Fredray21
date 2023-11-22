from fastapi import FastAPI
from app.api.casts import casts
from app.api.db import metadata, database, engine

metadata.create_all(engine)

# create the app
app = FastAPI(openapi_url="/api/v1/casts/openapi.json", docs_url="/api/v1/casts/docs")

# create the database connection
@app.on_event("startup")
async def startup():
    await database.connect()

# close the database connection
@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# include the router
app.include_router(casts, prefix='/api/v1/casts', tags=['casts'])

