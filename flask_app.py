import requests
import json
from flask import Flask
app = Flask(__name__)



response = requests.get("https://data.cityofchicago.org/resource/4ijn-s7e5.json")

parsed = response.json()

@app.route('/')
def raw_data():
	return "{}".format(parsed)



if __name__ == '__main__':
	app.run()

