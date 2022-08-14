import os
from datetime import timedelta
basedir = os.path.abspath(os.path.dirname(__file__))



class Config:
    LOG_FILE_PATH = '../../Logs'
    REPORT_FILE_PATH = '../../Reports'

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):

    LOG_FILE_PATH = '../../Logs/my_log'

env_config = {
    "development": DevelopmentConfig
}
