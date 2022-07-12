from http import client
from urllib import response
from wsgiref import headers
from pymongo import MongoClient
from flask import Flask, render_template, jsonify, request
import requests
import json

app = Flask(__name__)

client = MongoClient('mongodb+srv://test:sparta@cluster0.n802d.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

# @app.route('/aaa', methods=["POST"])
# def post_now_showing():
#     url = 'https://api.odcloud.kr/api/15042291/v1/uddi:f831fb62-a6ca-483b-94f8-dfc2243fa3ef'
#     headers = {
#         'Authorization' : 'uO1FqnqYYWxvHGeughWph2r0W6+bqIPqgtC4eqiJ1sWInFsnyy7t3zLr4ZrVxum49BK+qA0xDxRWBMmYZake3w=='
#     }
#     params = {
#         'page' : '1',
#         'perPage': '60',
#         'serviceKey': 'uO1FqnqYYWxvHGeughWph2r0W6+bqIPqgtC4eqiJ1sWInFsnyy7t3zLr4ZrVxum49BK+qA0xDxRWBMmYZake3w=='
#     }
#     alcoholList = requests.get(url, headers=headers, params=params).json()
#     alcohol_infos = alcoholList['data']
    
    
#     db.alchols.delete_one({
#             'place': "place",
#             'name': "name",
#             'kind': "kind"
#         })
    
#     for alchol in alcohol_infos:
#         place = alchol["주소"]
#         name = alchol["품명"]
#         kind = alchol["품목"]
#         doc = {
#             'place': place,
#             'name': name,
#             'kind': kind
#         }
#         db.alchols.insert_one(doc)

#     return jsonify({'result': 'success'})


@app.route('/alchol', methods=['GET'])
def get_now_showing():
    alchols_list = list(db.alchols.find({}, {'_id': False}))
    # place_info = alchols_list['place']
    return jsonify({'alchols' : alchols_list})


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