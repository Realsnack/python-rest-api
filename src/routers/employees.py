from fastapi import APIRouter
import psycopg2
import sys, os
import numpy as np
import pandas as pd
import example_psql as creds
import pandas.io.sql as psql

router = APIRouter(
    prefix="/api/employees",
    tags=["employees"],
    responses={404: {"description": "Not found"}},
)

connection_string = f'host=postgredb.msvacina.cz port=5432 dbname=python-rest user=python-rest_app password=Pythonheslo'
connection = psycopg2.connect(connection_string)

def get_postgres_status():
    try:
        pgStatus = True
    except:
        pgStatus = False

    return pgStatus

@router.get("/")
async def read_employees_root():
    pgStatus = et_postgres_status()
    return {"message": "Welcome to employees API", 'isPostgresUp': pgStatus}
