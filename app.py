from urllib import response
from wsgiref import headers
from pymongo import MongoClient
from flask import Flask, render_template, jsonify, request
import requests
from pprint import pprint


app = Flask(__name__)


url = 'https://api.odcloud.kr/api/15042291/v1/uddi:f831fb62-a6ca-483b-94f8-dfc2243fa3ef'

params = {
        'page' : '1',
        'perPage': '135',
        'serviceKey': 'Gt8j+nZ9SiGh7agtjfQ7HXTDG9MQf7CXibre+C8J7Sk5vb9fi6rR7Z6RDZMxpNp0w+mDWgeGf/Cy5At3GNZQ1g=='
}

response = requests.get(url, params=params)
data = response.json()
pprint(data)
    


@app.route('/')
def main():
    return render_template("index.html")


@app.route('/sign_up')
def detail():
    return render_template("sign_up.html")


@app.route('/alcohol_info')
def alcohol_info():
    return render_template("alcohol_info")



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)