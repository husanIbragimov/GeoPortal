import re

import pandas as pd
import psycopg2
import requests
from sqlalchemy import create_engine

from app.core.config import settings


class LoadSpheresToDB:
    def __init__(self):
        self.conn = psycopg2.connect(settings.SQLALCHEMY_DATABASE_URI)
        self.cur = self.conn.cursor()
        self.engine = create_engine(settings.SQLALCHEMY_DATABASE_URI)
        self.url = settings.SDMX_URI
        self.siat_url = settings.SIAT_URI

    def insert_sphere(self, pk, title, icon, parent_id, section_id):
        if pk == 0:
            self.cur.execute(
                """
                INSERT INTO spheres (title, icon, icon_light, parent_id, is_active, section_id)
                VALUES (%s, %s, %s, %s, true, %s)
                RETURNING id
                """,
                (title, icon, icon, parent_id, section_id)
            )
        else:
            self.cur.execute(
                """
                INSERT INTO spheres (id, title, icon, icon_light, parent_id, is_active, section_id)
                VALUES (%s, %s, %s, %s, %s, true, %s)
                RETURNING id
                """,
                (pk, title, icon, icon, parent_id, section_id)
            )
        self.conn.commit()
        return self.cur.fetchone()[0]

    def close(self):
        self.cur.close()
        self.conn.close()

    def update_sphere(self, dark, light, pk):
        self.cur.execute(
            """
            UPDATE public.spheres
            SET icon = %s, icon_light = %s
            WHERE id = %s
            """,
            (dark, light, pk)
        )
        self.conn.commit()

    def get_load_json_to_db(self):
        response = requests.get(self.url)
        data = response.json()

        data_df = pd.DataFrame(data)

        for index, row in data_df.iloc[:-2].iterrows():
            for child in row["children"]:
                sphere_id = self.insert_sphere(0, child['name'], child['icon_svg'], None, child['id'])
                for sub_child in child["children"][0]["children"]:
                    self.insert_sphere(sub_child['id'], sub_child['name'], sub_child['icon_svg'], sphere_id,
                                       sub_child['id'])
        return "Success"

    def reset_truncate_identities(self):
        self.cur.execute(
            """
            TRUNCATE TABLE spheres RESTART IDENTITY
            """
        )
        self.conn.commit()

    @staticmethod
    def change_color(new_color, icon):
        return re.sub(r'fill="[^"]+"', f'fill="{new_color}"', icon)

    def update_icon_colors(self, dark, light):
        df = pd.read_sql(
            """
            SELECT id, icon, icon_light
            FROM public.spheres
            where parent_id is null
            """,
            self.engine
        )
        for index, row in df.iterrows():
            self.update_sphere(
                self.change_color(dark, row['icon']),
                self.change_color(light, row['icon_light']),
                row['id']
            )

    def filter_data(self):
        df = pd.read_sql(
            """
            SELECT id
            FROM public.spheres
            WHERE parent_id IS NOT NULL
            """, self.engine)
        ids = df['id'].to_list()

        deletion_ids = []

        for i in ids:
            res = requests.get(f"{self.siat_url}/media/uploads/sdmx/sdmx_data_{i}.json")

            # print(res.json()[0]['data'], "\n\n\n\n")
            if res.status_code == 404:
                deletion_ids.append(i)
            if len(res.json()[0]['data']) == 1:
                deletion_ids.append(i)
            if res.status_code == 200 and len(res.json()[0]['data'][0]['Code']) < 4:
                deletion_ids.append(i)
        return tuple(deletion_ids)

    def delete_empty_and_not_soato(self):
        deletion_ids = self.filter_data()
        if not deletion_ids:
            return "No data to delete"
        query = f"""
        DELETE FROM public.spheres
        WHERE id IN {deletion_ids}
        """
        self.cur.execute(query)
        self.conn.commit()


if __name__ == "__main__":
    load_spheres = LoadSpheresToDB()
    load_spheres.reset_truncate_identities()
    print("Reset identities")
    load_spheres.get_load_json_to_db()
    print("Load spheres")
    load_spheres.delete_empty_and_not_soato()
    print("Delete empty and not soato")
    load_spheres.update_icon_colors("#003985", "#ffffff")
    print("Update colors")
    load_spheres.close()
    print("Success")
