import click
from flask.cli import with_appcontext
from flask_jwt_extended import create_access_token, create_refresh_token

from extensions import db
# FIXME from api.models import Admin


@click.command(name='create_tables')
@with_appcontext
def create_tables():
    db.create_all()


""" @click.command(name='create_admin')
@with_appcontext
def create_admin():
    admin = Admin(
        user_id="$pbkdf2-sha256$29000$fm8tBQBAiLG2di5FaM05Jw$Z1oc8Gyc1ImrWgvvzw3m4DYVJ5kUIKyHSaAiFzLbnzs"
    )

    db.session.add(admin)
    db.session.commit()
    access_token = create_access_token(identity=admin.user_id, fresh=True)
    refresh_token = create_refresh_token(identity=admin.user_id)

    print('#' * 100)
    print("Refresh Tokens:")
    print(refresh_token)
    print('#' * 100)
    print(access_token)
 """
