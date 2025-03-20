# GeoPortal

## __How to run the FastAPI project__

1. Clone the repository
   ```bash
   https://github.com/husanIbragimov/GeoPortal.git && cd GeoPortal
   ```
2. Create a virtual environment
   ```bash
    virtualenv venv
    ```
3. Activate the virtual environment
    ```bash
     source venv/bin/activate
     ```
4. Install the requirements
   ```bash
    pip install -r requirements/base.txt
    ```
5. Create a `.env` file in the root directory and add the following environment variables
   ```bash
    cp .env.example .env
    ```
6. **Create migration** to generate the initial migration
   ```bash
   alembic revision --autogenerate -m "Initial migration"
   ```   

7. **Run the migration** to apply the changes to the database
   ```bash
   alembic upgrade head
   ```

8. **Create Sphere data**
    ```bash
    python load_spheres_to_db.py
    ```

9. Run the FastAPI project
    ```bash
     fastapi run
     ```

## Site Views

### 1. GeoPortal default page 
   ![GeoPortal default page](data%2Fimg%2FGeoPortal-default.jpg)

### 2. GeoPortal spheres
   ![GeoPortal-spheres.jpg](data%2Fimg%2FGeoPortal-spheres.jpg)

### 3. Statistical data by region
   ![GeoPortal.jpg](data%2Fimg%2FGeoPortal.jpg)