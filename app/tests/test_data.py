import polars as pl
import psycopg2

from app.core.config import settings


class Database:
    def __init__(self):
        self.conn = psycopg2.connect(
            settings.DATABASE_URL
        )
        self.cur = self.conn.cursor()

    def get_data(self, query):
        self.cur.execute(query)
        data = self.cur.fetchall()
        return data

    def filter_data(self, query):
        df = pl.read_database(query, self.conn)
        print(df)
        return df




db = Database()
query = f"""
SELECT
    id,
    title,
    parent_id,
    secton_id
    FROM spheres
    WHERE 
"""
data = db.get_data(query)
