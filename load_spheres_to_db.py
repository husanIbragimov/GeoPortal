import psycopg2
import requests
import pandas as pd

SQLALCHEMY_DATABASE_URI="postgresql://husan:123@localhost:5432/gis"


class LoadSpheresToDB:
    def __init__(self):
        self.conn = psycopg2.connect(SQLALCHEMY_DATABASE_URI)
        self.cur = self.conn.cursor()
        self.url = "https://api.siat.stat.uz/sdmx/json/"

    def insert_sphere(self, title, icon, parent_id):
        self.cur.execute(
            """
            INSERT INTO spheres (title, icon, parent_id)
            VALUES (%s, %s, %s)
            RETURNING id
            """,
            (title, icon, parent_id)
        )
        self.conn.commit()
        return self.cur.fetchone()[0]

    def close(self):
        self.cur.close()
        self.conn.close()
    
    def update_sphere(self, icon_svg, title):
        self.cur.execute(
            """
            UPDATE spheres
            SET icon = %s
            WHERE title = %s
            """,
            (icon_svg, title)
        )
        self.conn.commit()

    def get_load_json_to_db(self):
        response = requests.get(self.url)
        data = response.json()
        
        data_df = pd.DataFrame(data)
        # print(data_df)

        for index, row in data_df.iterrows():
            print(len(row["children"]))
            for child in row["children"]:
                sphere_id = self.insert_sphere(child['name'], child['icon_svg'], None)
                for sub_child in child["children"][0]["children"]:
                    self.insert_sphere(sub_child['name'], sub_child['icon_svg'], sphere_id)
        
        return "Success"
    
    def get_load_svg_to_db(self):
        response = requests.get(self.url)
        data = response.json()
        
        data_df = pd.DataFrame(data)
        print(data_df)

        for index, row in data_df.iterrows():
            print(index)
            print(row["children"][0]['name'])
            sphere_id = self.update_sphere(row["children"][0]['icon_svg'], row["children"][0]['name'])
        
        return "Success"


        
if __name__ == "__main__":
    load_spheres = LoadSpheresToDB()
    load_spheres.get_load_json_to_db()
    load_spheres.close()
        
