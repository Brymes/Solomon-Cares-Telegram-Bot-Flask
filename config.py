import datetime
import os
import re


class Config():
    SECRET_KEY = os.environ.get("SECRET_KEY")

    # FIXME
    var = os.environ.get('DATABASE_URL')
    SQLALCHEMY_DATABASE_URI = re.sub(r"postgres", "postgresql+psycopg2", var)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_RECORD_QUERIES = True

    JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(days=1)
    PROPAGATE_EXCEPTIONS = True
    JWT_ERROR_MESSAGE_KEY = 'message'

    BOT_KEY = os.environ.get('TELEGRAM_BOT_KEY')
