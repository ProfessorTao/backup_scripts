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


import pymongo
import sys

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
#db_name = 'cce9'
db_table_attrdb = 'attrdb'

db_conn_attrdb = conn[db_name][db_table_attrdb]

BLACK_LEVEL = 200

'''
pipeline = [{'$match': {'main_level': BLACK_LEVEL}}, {'$group':{'_id':'$sig_id', 'count': {'$sum':1}}}, {'$sort': {'count': -1, '_id': 1}}]
cursor = db_conn_attrdb.aggregate(pipeline)

if 1==cursor['ok']:
    for item in cursor['result']:
        print item
'''

       map = function() {
          for (var key in this) {
              emit(key, {count:1});
          }
       }




'''
db_name_stat = 'vdc_stat'
db_name_table= 'result_stat'

print value_dic
conn[db_name_stat][db_name_table].insert(value_dic, manipulate = False)
'''

conn.disconnect()
