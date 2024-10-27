import os
import sys
import pandas as pd
import pymongo

import certifi
certifi.where()

from dotenv import load_dotenv
load_dotenv()

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logger.logger import logging
from networksecurity.pipeline.training_pipeline import TrainingPipeline

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, File, UploadFile
from uvicorn import run as app_run
from fastapi.responses import Response
from starlette.responses import RedirectResponse


mongo_db_url = os.getenv("MONGO_DB_URL")
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")

os.environ["AWS_ACCESS_KEY_ID"] = AWS_ACCESS_KEY_ID
os.environ["AWS_SECRET_ACCESS_KEY"] = AWS_SECRET_ACCESS_KEY


app = FastAPI()
origins = ['"*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=['authentication'])
async def index():
    return RedirectResponse(url="/docs")

@app.get("/train")
async def train():
    try:
        pass
    except Exception as e:
        raise NetworkSecurityException(e, sys)
    
# @app.get("/predict")
# async def predict_route(request: Request, file: UploadFile = File(...)):
#     try:
#         pass
#     except Exception as e:
#         raise NetworkSecurityException(e, sys)


if __name__ == "__main__":
    app_run(app, host="localhost", port=8000)