#!/local/bin/env python
#encoding:utf-8

import datetime
import time

def get_last_n_day(n=1):
    today = datetime.date.today()
    today_zero_time = int(time.mktime(today.timetuple()))

    day_seconds = 86400
    end_time = today_zero_time - (n-1)*day_seconds
    begin_time = end_time - day_seconds

    return begin_time, end_time
# end of get_last_n_time


def get_last_date(n=1):
    last_dat_tm = time.localtime(int(time.time()) - 3600*24*n)
    y = last_dat_tm.tm_year
    m = last_dat_tm.tm_mon
    d = last_dat_tm.tm_mday

    return '%d%02d%02d' % (y, m, d)
# end of def get_last_date():


import sys

import pymongo
from bson.code import Code
from bson.son import SON

# 获取命令行参数
# 参数个数：len(sys.argv)
# 脚本名：    sys.argv[0]
# 参数1：     sys.argv[1]
# 参数2：     sys.argv[2]

if 1==len(sys.argv):
    # 无命令行参数
    n = 1
else:
    n = int(sys.argv[1])

str_split = '\n----------------------------------------------------------------------------------'
print '%s\n%s\n' % (str_split, time.ctime())


mongo_ip = '10.52.177.19'
mongo_port = 27017
mongo_pool_size = 1000

conn = pymongo.MongoClient(mongo_ip, port=mongo_port, max_pool_size=mongo_pool_size)
db_name = 'cce15'
db_name = 'cce9'
db_table_attrdb = 'attrdb'

db_conn_attrdb = conn[db_name][db_table_attrdb]

MAP_FILE = 'file_cnt_map.js'
REDUCE_FILE = 'file_cnt_reduce.js'

BLACK_LEVEL = 200


#Load map and reduce functions
map_file_cnt = Code(open(MAP_FILE, 'r').read())
reduce_file_cnt = Code(open(REDUCE_FILE, 'r').read())

#Run the map-reduce query
results = db_conn_attrdb.map_reduce(map_file_cnt, reduce_file_cnt, query={'main_level':150}, out='stat')
#SON([("replace", "mr"), ("db", "outdb")])


#Print the results
#for res in results.find().sort('value.count', pymongo.DESCENDING):
#    print res['_id'], res['value']['count']
cursor = results.find()
for element in cursor:
    print element


conn.disconnect()
