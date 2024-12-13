# GeoPortal

## __How to run the FastAPI project__

1. Clone the repository
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
6. **nitialize Alembic** for database migrations
    ```bash
    alembic init alembic
    ```
7. **Configure Alembic:** Edit __alembic.ini__ to set the SQLAlchemy URL. For example:
    ```bash
    sqlalchemy.url = postgresql://user:password@localhost/dbname
    ```
    Here's how you can update your __env.py__ file to combine the metadata from multiple __Base__ classes correctly:

    ```python
    # add your model's MetaData object here
    # for 'autogenerate' support
    # from myapp import mymodel
    # target_metadata = mymodel.Base.metadata
    from app.models import user, sphere
    
    # Combine metadata from multiple Base classes
    target_metadata = MetaData()
    for metadata in [user.Base.metadata, sphere.Base.metadata]:
        for table in metadata.tables.values():
            table.tometadata(target_metadata)
    
    ```

8. **Create a migration repository**
    ```bash
    alembic revision --autogenerate -m "Initial migration"
    ```
9. **Run the migration** to apply the changes to the database
    ```bash
    alembic upgrade head
    ```

10. **Create Sphere data**
    ```bash
    python load_spheres_to_db.py
    ```

11. Run the FastAPI project
    ```bash
     uvicorn app.main:app --reload
     ```