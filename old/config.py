import os
from environs import Env

basedir = os.path.abspath(os.path.dirname(__file__))

env = Env()
env.read_env()


class GisConfig:
    SECRET_KEY = env.str("SECRET_KEY", "some-secret-key")
    SQLALCHEMY_DATABASE_URI = env.str("SQLALCHEMY_DATABASE_URI", default="sqlite:///" + os.path.join(basedir, "app.db"))
    SQLALCHEMY_TRACK_MODIFICATIONS = False    
