from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///friends.db" # configuring the database
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False # this configuration is for performance reason (reduce memory usage)

db = SQLAlchemy(app)

import routes

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
