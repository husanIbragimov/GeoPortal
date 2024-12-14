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

6. **Run the migration** to apply the changes to the database
   ```bash
   alembic upgrade head
   ```

7. **Create Sphere data**
    ```bash
    python load_spheres_to_db.py
    ```

8. Run the FastAPI project
    ```bash
     fastapi run
     ```