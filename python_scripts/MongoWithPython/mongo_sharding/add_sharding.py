#coding:utf-8
#-------------------------------------------------------------------------------
# Name:        add_sharding
# Purpose:
#
# Author:      taotianyi
#
# Created:     22/05/2014
# Copyright:   (c) baidu 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------



import pymongo
import sys
import datetime
from datetime import date
import traceback

def get_today_month():
    today = date.today()
    today_year = today.year
    today_month = today.month

    str_month = "%d%02d" % (today_year, today_month)
    return str_month
# end of get_today_month

def main():
    MONGO_HOST = "st01-sw-resultmysql03.st01.baidu.com"
    MONGO_PORT = 16000

    SHARDING_DB_PREFIX = "data_report"
    SHARDING_TB_NAME_LIST = ["softid_1_cmdid_2", "softid_9"]

    if 2 == len(sys.argv):
        str_month = sys.argv[1]
    else:
        str_month = get_today_month()

    sharding_db_name = "%s_%s" % (SHARDING_DB_PREFIX, str_month)
    print sharding_db_name

    mongo_conn = pymongo.MongoClient(host=MONGO_HOST, port=MONGO_PORT)
    db_admin = "admin"

    try:
        mongo_conn[db_admin].command('enablesharding', sharding_db_name)
    except:
        print traceback.format_exc()

    for sharging_tb_name in SHARDING_TB_NAME_LIST:
        sharding_name = "%s.%s" % (sharding_db_name, sharging_tb_name)
        sharding_key_dict = {"stat_date": 1, "guid_1": 1}
        try:
            mongo_conn[db_admin].command('shardcollection', sharding_name, key = sharding_key_dict)
        except:
            print traceback.format_exc()
    # end of for

    mongo_conn.disconnect()
# end of def main()

if __name__ == '__main__':
    main()
