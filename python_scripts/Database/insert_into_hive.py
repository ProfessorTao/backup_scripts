#coding:utf-8
#-------------------------------------------------------------------------------
# Name:        insert_into_hive
# Purpose:
#
# Author:      TaoTianYi
#
# Created:     2015/01/06
# Copyright:   (c) TaoTianYi 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import hive_op_with_dataop

class Insert_into_hive(object):
    def __init__(self):
        self.__hive_conn = hive_op_with_dataop.Hive_Operation()

    def __set_config(self):
        # set hive.exec.compress.output=true
        # set io.seqfile.compression.type=BLOCK   //设置压缩        
        sql_config_list = ["set hive.exec.compress.output=true", "set io.seqfile.compression.type=BLOCK"]
        for sql_config in sql_config_list:
            print sql_config
            self.__hive_conn.execute_sql(sql_config)
    # end of def

    def _insert_into_hive_table(self, db_name, tb_name, date_str, value_tuple):
        sql_insert_1 = "insert overwrite table %s.%s partition(stat_date='%s')" % (db_name, tb_name, date_str)
        sql_insert_2 = "values(%s, %s, %s, %s)" % value_tuple
        sql_insert = "%s %s" % (sql_insert_1, sql_insert_2)
        print sql_insert
        self.__hive_conn.execute_sql(sql_insert)
    # end of def
# end of class
