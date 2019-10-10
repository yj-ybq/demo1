#!/usr/bin/env python
#-*-coding:utf-8-*-
from pymongo import MongoClient
MC = MongoClient("127.0.0.1",27017)
MongoDB = MC["S21DAY94"]

# 增
MongoDB.Users.insert_one({"name":"YWB","age":999})
MongoDB.Users.insert_many({"name":"www","age":9},{"name":"YBQ","age":20})
# insertMany时插入的是多条数据，但

# 查
MongoDB.Users.find_one({"name":"YWB"})

# 注意：find只有find_one，没有find_many

# 改


# 删除
MongoDB.Users.delete_one({})
MongoDB.Users.delete_many({})

# 注意：在python中所有的key必须带引号“”，在nomysql软件中key可以不带“”

# 高级函数
from pymongo import DESCENDING,ASCENDING   # DESCENDING 正序  ASCENDING 倒叙

