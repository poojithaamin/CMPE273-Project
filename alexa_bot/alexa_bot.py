from flask import Flask
from flask_ask import Ask, statement, question, session
from config import get_pwd
import wikipedia



import json
import requests
import time
import unidecode
import wikipedia
import logging


app = Flask(__name__)






if __name__ == "__main__":
    app.run(debug=True)