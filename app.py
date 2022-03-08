import requests
from flask import Flask, render_template, request, jsonify, redirect, url_for


app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://jwc2005:jwc20122470!@cluster0.xlzfh.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def main():
    return render_template("index.html")


@app.route('/detail')
def test_map():
    return render_template("detail.html")


# headers = {
#     "X-NCP-APIGW-API-KEY-ID": "s76fz5795p",
#     "X-NCP-APIGW-API-KEY": "slSZ5BKsgMyGfrEp7LFXW8UcaQ7VZpTgW0mMAzHl"
# }
# address="경북 상주시 문무1길 40-5"
# r = requests.get(f"https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode?query={address}", headers=headers)
# response = r.json()
# # print(response)
# if response["status"] == "OK":
#     if len(response["addresses"]) > 0:
#         x = float(response["addresses"][0]["x"])
#         y = float(response["addresses"][0]["y"])
#         print(x, y)
#         doc = {
#             "mapx": x,
#             "mapy": y}
#         db.matjips.insert_one(doc)
#     else:
#         print( "좌표를 찾지 못했습니다")
# else:
#     print(response["status"])
#
# all_users = list(db.users.find({},{'_id':False}))
# print(all_users)
if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
