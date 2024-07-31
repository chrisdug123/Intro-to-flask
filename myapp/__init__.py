
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yourdatabase.db'
app.config['SECRET_KEY'] = 'c699106fc2dfdc1d9ea0e6ddc55cd3d7edbeb1a5987eed67'
db=SQLAlchemy(app)
migrate=Migrate(app,db)


from myapp import routes, models