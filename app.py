<<<<<<< HEAD
from flask import Flask, render_template, request, jsonify, redirect, url_for
from pymongo import MongoClient
=======

from http import client
from urllib import response
from wsgiref import headers
from pymongo import MongoClient
from flask import Flask, render_template, jsonify, request,redirect, url_for
import requests
import json
import jwt
import datetime
import hashlib
from datetime import datetime, timedelta


client1 = MongoClient('mongodb+srv://test:sparta@cluster0.n802d.mongodb.net/?retryWrites=true&w=majority')
db1 = client1.dbsparta
# app.config["TEMPLATES_AUTO_RELOAD"] = True
# app.config['UPLOAD_FOLDER'] = "./static/profile_pics"

SECRET_KEY = 'SPARTA'

client = MongoClient('mongodb://test:test@localhost', 27017 )
db = client.dbsparta_plus_week4
>>>>>>> da8bc592b4c14ef5eeb151d2c72308647a4b6c8e


app = Flask(__name__)

<<<<<<< HEAD
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

=======




@app.route('/', methods=["GET", "POST"])
def index():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])

        return render_template('index.html')
    except jwt.ExpiredSignatureError:
        return redirect(url_for("login", msg="로그인 시간이 만료되었습니다."))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("login", msg="로그인 정보가 존재하지 않습니다."))


@app.route('/login')
def login():
    msg = request.args.get("msg")
    return render_template('login.html', msg=msg)


@app.route('/user/<username>')
def user(username):
    # 각 사용자의 프로필과 글을 모아볼 수 있는 공간
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        status = (username == payload["id"])  # 내 프로필이면 True, 다른 사람 프로필 페이지면 False

        user_info = db.users.find_one({"username": username}, {"_id": False})
        return render_template('user.html', user_info=user_info, status=status)
    except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
        return redirect(url_for("home"))


@app.route('/sign_in', methods=['POST'])
def sign_in():
    # 로그인
    username_receive = request.form['username_give']
    password_receive = request.form['password_give']

    pw_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
    result = db.users.find_one({'username': username_receive, 'password': pw_hash})

    if result is not None:
        payload = {
         'id': username_receive,
         'exp': datetime.utcnow() + timedelta(seconds=60 * 60 * 24)  # 로그인 24시간 유지
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256').decode('utf-8')

        return jsonify({'result': 'success', 'token': token})
    # 찾지 못하면
    else:
        return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})


@app.route('/sign_up/save', methods=['POST'])
def sign_up():
    username_receive = request.form['username_give']
    password_receive = request.form['password_give']
    password_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
    doc = {
        "username": username_receive,                               # 아이디
        "password": password_hash,                                  # 비밀번호
        "profile_name": username_receive,                           # 프로필 이름 기본값은 아이디
        "profile_pic": "",                                          # 프로필 사진 파일 이름
        "profile_pic_real": "",                                     # 프로필 사진 기본 이미지
        "profile_info": ""                                          # 프로필 한 마디
    }
    db.users.insert_one(doc)
    return jsonify({'result': 'success'})


@app.route('/sign_up/check_dup', methods=['POST'])
def check_dup():
    username_receive = request.form['username_give']
    exists = bool(db.users.find_one({"username": username_receive}))
    return jsonify({'result': 'success', 'exists': exists})


@app.route('/update_profile', methods=['POST'])
def save_img():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        # 프로필 업데이트
        return jsonify({"result": "success", 'msg': '프로필을 업데이트했습니다.'})
    except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
        return redirect(url_for("home"))


@app.route('/posting', methods=['POST'])
def posting():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        # 포스팅하기
        return jsonify({"result": "success", 'msg': '포스팅 성공'})
    except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
        return redirect(url_for("home"))


@app.route("/get_posts", methods=['GET'])
def get_posts():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        # 포스팅 목록 받아오기
        return jsonify({"result": "success", "msg": "포스팅을 가져왔습니다."})
    except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
        return redirect(url_for("home"))


@app.route('/update_like', methods=['POST'])
def update_like():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
        # 좋아요 수 변경
        return jsonify({"result": "success", 'msg': 'updated'})
    except (jwt.ExpiredSignatureError, jwt.exceptions.DecodeError):
        return redirect(url_for("home"))


# @app.route('/aaa', methods=["POST"])
# def post_now_showing():
#     url = 'https://api.odcloud.kr/api/15042291/v1/uddi:f831fb62-a6ca-483b-94f8-dfc2243fa3ef'
#     headers = {
#         'Authorization' : 'uO1FqnqYYWxvHGeughWph2r0W6+bqIPqgtC4eqiJ1sWInFsnyy7t3zLr4ZrVxum49BK+qA0xDxRWBMmYZake3w=='
#     }
#     params = {
#         'page' : '1',
#         'perPage': '135',
#         'serviceKey': 'uO1FqnqYYWxvHGeughWph2r0W6+bqIPqgtC4eqiJ1sWInFsnyy7t3zLr4ZrVxum49BK+qA0xDxRWBMmYZake3w=='
#     }
#     alcoholList = requests.get(url, headers=headers, params=params).json()
#     alcohol_infos = alcoholList['data']
    
    
#     db1.alchols.delete_one({
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
#         db1.alchols.insert_one(doc)

#     return jsonify({'result': 'success'})


@app.route('/alchol', methods=['GET'])
def get_now_showing():
    alchols_list = list(db1.alchols.find({}, {'_id': False}))
    # place_info = alchols_list['place']
    return jsonify({'alchols' : alchols_list})


>>>>>>> da8bc592b4c14ef5eeb151d2c72308647a4b6c8e

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)