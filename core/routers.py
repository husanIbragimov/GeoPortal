class DatabaseRouter:

    @staticmethod
    def db_for_read(model, **hints):
        print(model._meta.app_label, "read")
        if model._meta.app_label == "geomap":
            return "map"
        return "default"

    @staticmethod
    def db_for_write(model, **hints):
        print(model._meta.app_label, "write")
        if model._meta.app_label == "geomap":
            return "map"
        return "default"

    @staticmethod
    def allow_relation(obj1, obj2, **hints):
        print(obj1._meta.app_label, obj2._meta.app_label, "relation")
        db_list = ("map", "default")
        if obj1._meta.app_label in db_list or obj2._meta.app_label in db_list:
            return True
        return None

    @staticmethod
    def allow_migrate(db, app_label, model_name=None, **hints):
        print(app_label, db, "migrate")
        if app_label == "geomap":
            return db == "map"
        return db == "default"
