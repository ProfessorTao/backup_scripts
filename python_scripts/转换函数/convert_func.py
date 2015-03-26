#coding:utf-8
#-------------------------------------------------------------------------------
# Name:        convert_func
# Purpose:     for codes collected
#
# Author:      taotianyi
#
# Created:     31/03/2014
# Copyright:   (c) baidu 2014
# Licence:     <taotianyi01@baidu.com>
#-------------------------------------------------------------------------------

#################################################################################################
# common methods

MAGIC_NUM    = -9223372036854775808  # 2^63

func_ip_int_to_str    = lambda x: '.'.join([str(x/(256**i)%256) for i in range(3,-1,-1)])

func_ip_str_to_int    = lambda x: sum([256**j*int(i) for j,i in enumerate(x.split('.')[::-1])])

func_guid_str_to_long = lambda x: (int(x[0:16], 16) + MAGIC_NUM, int(x[16:32], 16) + MAGIC_NUM)

func_dict_to_sorted_list = lambda dic, index = 0, reverse = True: sorted(dic.iteritems(), key=lambda dic:dic[index], reverse=reverse) 

def convert_list_to_dict(column_dict, first_key_list, row):
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
    # end of for seq, col_name

    return result_dict
# end of def convert_list_to_dict
