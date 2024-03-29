from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import create_app
from app import db

# from flask_migrate import Migrate,MigrateCommand


app = create_app('dev')
Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

app.config['DEBUG'] = True
if __name__ == '__main__':
    # app.run()
    manager.run()
