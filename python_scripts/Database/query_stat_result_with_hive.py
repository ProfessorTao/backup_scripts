#coding:utf-8
#-------------------------------------------------------------------------------
# Name:        query_stat_result_with_hive
# Purpose:
#
# Author:      TaoTianYi
#
# Created:     2014/12/05
# Copyright:   (c) TaoTianYi 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import copy

import hive_op_with_dataop


class GetStatResultWithHive(object):
    def __init__(self):
        self.__hive_conn = None

        # 是否修改了hive默认设置，如果修改了，那么以后每次运行sql之前都要修改hive设置
        self.__b_hack_sql_config_list = list() # hive hack config

        self.__last_total_sql = None
        self.__last_total_result = None

        self.__last_groupby_sql = None
        self.__last_groupby_result = None
    # end of def


    def __reconnect_hive_conn(self):
        self.__hive_conn = hive_op_with_dataop.Hive_Operation()


    def __hack_hive_config(self):
        for sql_config in self.__b_hack_sql_config_list:
            print sql_config
            self.__hive_conn.execute_sql(sql_config)
    # end of def


    def _modify_hive_config(self, sql_config_list = None):
        if not sql_config_list:
            ## 防止hive报分片不均匀的错误而临时改变hive的默认配置，以达到正常执行的目的
            sql_config_list = [ 'set mapreduce.reduce.shuffle.memory.limit.percent=0.05', 
                                'set mapreduce.reduce.shuffle.parallelcopies=10', 
                                'set mapreduce.reduce.shuffle.merge.percent=0.6'  ]
        # end of if

        if isinstance(sql_config_list, list):
            self.__b_hack_sql_config_list = copy.deepcopy(sql_config_list)
    # end of def


    def _get_data_with_hive(self, date_str, sql_groupby, sql_total, total_value = 'total'):
        ### 分析total数据
        if sql_total == self.__last_total_sql:
            total_result_list = self.__last_total_result
        else:            
            total_result_list = list()
            self.__reconnect_hive_conn() ## 每次运行之前，需要重新连接hive

            if self.__b_hack_sql_config_list:
                self.__hack_hive_config()  ## hack config
            print sql_total

            rows = self.__hive_conn.traverse_table(sql_total)
            if (isinstance(rows, list) or isinstance(rows, tuple)) and len(rows) > 0:
                for row in rows:
                    value_list = [date_str, total_value]
                    value_list.extend(list(row))
                    total_result_list.append(tuple(value_list))
            # end of if

            ## save last info
            self.__last_total_sql = sql_total
            self.__last_total_result = copy.deepcopy(total_result_list)
        # end of if


        ### 分析groupby数据
        if sql_groupby == self.__last_groupby_sql:
            groupby_result_list = self.__last_groupby_result
        else:
            groupby_result_list = list()
            self.__reconnect_hive_conn() ## 每次运行之前，需要重新连接hive   

            if self.__b_hack_sql_config_list:
                self.__hack_hive_config()  ## hack config
            print sql_groupby
            
            rows = self.__hive_conn.traverse_table(sql_groupby)
            if (isinstance(rows, list) or isinstance(rows, tuple)) and len(rows) > 0:
                for row in rows:
                    value_list = [date_str]
                    value_list.extend(list(row))
                    groupby_result_list.append(tuple(value_list))
            # end of if

            ## save last info
            self.__last_groupby_sql = sql_groupby
            self.__last_groupby_result = copy.deepcopy(groupby_result_list)            
        # end of if


        result_list = list()
        result_list.extend(total_result_list)
        result_list.extend(groupby_result_list)
        return result_list
    # end of def
# end of class

