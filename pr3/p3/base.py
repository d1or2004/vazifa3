import psycopg2 as psql
import os
from dotenv import load_dotenv

load_dotenv()


class Database:
    @staticmethod
    def connect(query, type):
        database = psql.connect(
            database=os.getenv("db_name"),
            host=os.getenv("db_host"),
            user=os.getenv("db_user"),
            password=os.getenv("db_password")

        )
        cursor = database.cursor()
        cursor.execute(query)
        query_data = ["insert", "create", "delete", "update"]
        if type in query_data:
            database.commit()

            if type == "insert":
                return "Inserted"

            elif type == "create":
                return "Created"

            elif type == "delete":
                return "Deleted"
            elif type == "update":
                return "Updated"
        else:
            return cursor.fetchall()
