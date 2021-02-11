from gevent import monkey

monkey.patch_all()

from app.main.model.user import User
from uuid import uuid4

import os
import unittest

from dotenv import load_dotenv, find_dotenv
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import blueprint

from app.main import create_app, db

load_dotenv(find_dotenv())

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.register_blueprint(blueprint)
app.app_context().push()

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.command
def run():
    app.run(host='0.0.0.0')


if __name__ == '__main__':
    manager.run()
