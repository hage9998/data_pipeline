from mysql_database import mysql_db
from bq_database import bq_db

def data_pipe():
    records = mysql_db()
    bq_db(records)

if __name__ == "__main__":
    data_pipe()


