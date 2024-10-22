# To install flask, first run the following line in the terminal:
# pip install flask

#imports
from flask import Flask

flask_app = Flask(__name__)

from app import routes