#몽고db는 딕셔너리가 쌓이는 db

#파이몽고 쓸게염
from pymongo import MongoClient
#내 로컬에서 사용할게염
client = MongoClient('localhost', 27017)
#dbsparta라는 db이름으로 접속할거에염
db = client.dbsparta

# 코딩 시작
insert/find/update/delete

#딕셔너리 만들어서
doc = {'name':'jane','age':21}
#db안에 users라는 collection안에 insert해라
db.users.insert_one(doc)


# 저장 - 예시
doc = {'name':'bobby','age':21}
db.users.insert_one(doc)

# 한 개 찾기 - 예시
user = db.users.find_one({'name':'bobby'})

# 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
same_ages = list(db.users.find({'age':21},{'_id':False}))

# 바꾸기 - 예시
db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

# 지우기 - 예시
db.users.delete_one({'name':'bobby'})
