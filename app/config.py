import os
from dotenv import load_dotenv

load_dotenv()

class Config(object):
    """Base Config Object"""
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'Som3$ec5etK*y')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', '')or 'mysql://user:password@localhost/database'

    SQLALCHEMY_BINDS = {
        'db2': 'mysql://user:pass@localhost/database2'
        #'db3': 'mysql://user:pass@localhost/database3'
}
    SQLALCHEMY_TRACK_MODIFICATIONS = False # This is just here to suppress a warning from SQLAlchemy as it will soon be removed