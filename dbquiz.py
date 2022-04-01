#파이몽고 쓸게염
from pymongo import MongoClient
#내 로컬에서 사용할게염
client = MongoClient('localhost', 27017)
#dbsparta라는 db이름으로 접속할거에염
db = client.dbsparta

# 코딩 시작

db.movies.update_one({'title':'매트릭스'},{'$set':{'star':'0'}})