from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('Library_Management_System.Config')  # Replace 'your_module_name' with the actual name of your module


print("Creating instance of database")
# Create an instance of SQLAlchemy and bind it to the Flask app
db = SQLAlchemy(app)


