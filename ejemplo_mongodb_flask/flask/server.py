#!/usr/bin/env python
import os, datetime, json

from flask import Flask
from pymongo import MongoClient

from selenium.webdriver.chrome.options import Options
from selenium import webdriver

from modulo_prueba.modulo_prueba import variable_cualquiera

# Ejemplo https://nander.cc/using-selenium-within-a-docker-container

app = Flask(__name__)

client = MongoClient("mongo:27017",  username='root',  password='example')

def set_chrome_options() -> None:
    """Sets chrome options for Selenium.
    Chrome options for headless browser is enabled.
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_prefs = {}
    chrome_options.experimental_options["prefs"] = chrome_prefs
    # chrome_prefs["profile.default_content_settings"] = {"images": 2}
    return chrome_options

@app.route('/')
def todo():
    try:
        client.admin.command('ismaster')
    except:
        return "Server not available"
    return "Hello fom the MongoDB client!\n"

@app.route("/mongo")
def check_mongo():

    db = client['test-database']

    post = {"author": "Milie",
            "text": "My first blog post too!",
            "tags": ["mongodb", "python", "pymongo"],
            "date": datetime.datetime.utcnow()}

    posts = db.posts
    posts.insert_one(post).inserted_id

    return json.dumps(posts.find_one(), default=str)

@app.route('/selenium')
def prueba_selenium():
    # TODO Agregar threads para que no sea blocking para el server
    driver = webdriver.Chrome(options=set_chrome_options())

    driver.get("https://learn.letskodeit.com/p/practice")

    elemento = driver.find_element_by_id("radio-btn-example")

    texto = elemento.text

    driver.close()

    return texto

@app.route('/prueba')
def prueba():

    return variable_cualquiera

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get("FLASK_SERVER_PORT", 9090), debug=True)