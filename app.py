from flask import Flask
from flask_restful import Api
# from flask_migrate import Migrate

from telebot import apihelper

from commands import create_tables
from config import Config
from extensions import db, jwt
from api.routes import initialize_routes
from api.auth import black_list

apihelper.RETRY_ON_ERROR = True
apihelper.SESSION_TIME_TO_LIVE = 5 * 60


def register_extensions(app):
    db.init_app(app)
    jwt.init_app(app)

    # migrate = Migrate(app, db)

    @jwt.token_in_blocklist_loader
    def check_if_token_in_blacklist(jwt_header, jwt_payload):
        jti = jwt_payload['jti']
        return jti in black_list


def register_resources(app):
    api = Api(app)
    initialize_routes(api)


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.cli.add_command(create_tables)

    register_extensions(app)
    register_resources(app)

    # FIXME
    sentry_sdk.init(
        dsn="",
        integrations=[FlaskIntegration()],
        traces_sample_rate=1.0
    )

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
