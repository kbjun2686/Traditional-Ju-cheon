from flask import Flask, render_template, request, jsonify, redirect, url_for
from pymongo import MongoClient


app = Flask(__name__)

client = MongoClient('3.34.136.176', 27017, username="test", password="test")
db = client.dbsparta


@app.route('/')
def main():
    return render_template("index.html")

@app.route('/alchol', methods=["GET"])
def get_alchol():
    # 주소 목록을 반환하는 API
    alchols_list = list(db.alchols.find({}, {'_id': False}))
    # alchols_list 라는 키 값에 맛집 목록을 담아 클라이언트에게 반환합니다.
    return jsonify({'result': 'success', 'alchols_list': alchols_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)