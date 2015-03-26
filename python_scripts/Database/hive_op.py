#!/usr/bin/python
#coding=utf-8

#-------------------------------------------------------------------------------
# Name:        hive_op_with_dataop
# Purpose:
#
# Author:      TaoTianYi
#
# Created:     21/06/2014
# Copyright:   (c) TaoTianYi 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import pyhs2
import traceback
#connect(host=nn, port=10000,authMechanism="PLAIN", user=user,database=db)
class Hive_Operation():
    def __init__(self, db_host = 'hive', db_port, db_user, auth_type = "PLAIN", db_name = None):
        self.__user = db_user_name
        self.__db = db_name
        self.__conn = pyhs2.connect(host=db_host, port=db_port, authMechanism=auth_type, user=db_user,database=db_name)
        self.__cur = self.__conn.cursor()
    # end of def __init__

    def __del__(self):
        self.__disconnect()
    # end of __del__

    def __disconnect(self):
        if self.__conn:
            if self.__cur:
                self.__cur.close()
                self.__cur = None
            # end of if self.__cur

            self.__conn.close()
            self.__conn = None
        # end of if self.__conn        
    # end of def

    def __reconnect(self):
        self.__disconnect()
        self.__conn = DataOp.GetHiveConnect(user = self.__user, db = self.__db)
        self.__cur = self.__conn.cursor()
    # end of def        


    def execute_sql(self, sql):
        # print("execute sql:%s", sql)
        try:
            self.__cur.execute(sql)
        except Exception, e:
            print "Hive Error %s, sql is %s, the detail is:" % (e, sql)
            print traceback.format_exc()

        self.__reconnect()
    # end of def execute_sql(self, sql, param = ())


    def traverse_table(self, sql):
        self.execute_sql(sql)
        rows = self.__cur.fetchall()
        return rows
    # end of def traverse_table


    def traverse_table_with_sscursor(self, sql):
        return self.traverse_table(sql)
    # end of traverse_table_with_sscursor


    def convert_list_to_dict(self, column_dict, first_key_list, row):
        result_dict = dict()

        def try_to_int(_value):
            try:
                _value = int(_value)
            except:
                pass

            return _value
        # end of def try_to_int

        for seq, col_name in column_dict.iteritems():
            value = row[col_name]
            if not isinstance(value, dict):
                # 固有字段
                result_dict[col_name] = try_to_int(value)
            else:
                # 协议字段，保存类型是一个map，key是一级上报字段号
                for first_key in first_key_list:
                    if first_key in value:
                        result_dict[first_key] = try_to_int(value[first_key])
                    else:
                        result_dict[first_key] = None
        # end of for key, value

        return result_dict
    # end of def convert_list_to_dict
# end of class MySql_Operation

