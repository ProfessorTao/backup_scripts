#coding:utf-8
#-------------------------------------------------------------------------------
# Name:        generate_pic
# Purpose:     for codes collected
#
# Author:      taotianyi
#
# Created:     2014/10/13
# Copyright:   (c) baidu 2014
# Licence:     <taotianyi01@baidu.com>
#-------------------------------------------------------------------------------


# http://www.cnblogs.com/shanyou/archive/2012/08/05/2624282.html
# http://www.cnmiss.cn/?p=327
# http://www.oschina.net/question/935739_87064?sort=time
# http://www.cnblogs.com/gxll1314/archive/2010/10/11/1847770.html


import os
import time
from datetime import timedelta
import json


def gen_picture(title, values, outfile_name, temp_json_file = './highcharts.json', scale = 1):
    ## margin  上 右 下 左
    options = {
                "chart":{"type":"line",'width':1000,'margin':[60,80,90,80]},
                "title":{"text":title},
                "xAxis":{'title': {'text': 'Count'}, 'tickInterval': 1}, 
                "yAxis":{'title': {'text': 'Number'}, 'tickInterval': 1}, 
                #"xAxis":{'type':'datetime','dateTimeLabelFormats':{'day':'%m-%d'}},
                #"yAxis":{'title': {'text': ''}, 'labels':{'formatter':"formatter_function"}},                
                'plotOptions':{'line':{'marker':{'enabled':False}}},
                "series":[]
            }

    for item in values:
        options["series"].append(item)

    options = json.JSONEncoder().encode(options)    

    infile = open(temp_json_file, 'w')
    infile.write(options)
    infile.close()

    # NOTE: global.json is a local config file
    # -globaloptions global.json 
    # used for setting Y axis with 'K'
    command = "/home/work/publish/lib/phantomjs/bin/phantomjs \
                /home/work/publish/lib/phantomjs/highcharts-convert.js \
                -infile %s -outfile %s -scale %d -width 1000" % (temp_json_file, outfile_name, scale)

    ret = os.system(command)
    os.remove(temp_json_file)
    #print '%d %d' % (ret, ret>>8)
# end of def


def gen_pic_parameter(value_tuple, display_name, color=None):
    data = dict()
    data["name"] = display_name
    data["data"] = value_tuple
    data["pointStart"] = 1
    #data["pointInterval"] = 1
    #data["pointStart"] = time.mktime(start_date.timetuple())*1000
    #eight_hour_milliseconds = 8 * 3600 * 1000 # for utc time
    #data["pointStart"] = timestamp_begin * 1000 + eight_hour_milliseconds
    #data["pointInterval"] = 24 * 3600 * 1000
    if color:
        data['color'] = color

    return data
# end of def


if __name__ == '__main__':
    pic_parameters_list = list()

    value_tuple = (1, 3, 5, 7, 9)
    display_name = '奇数'
    color = '#FF0000'
    pic_parameter = gen_pic_parameter(value_tuple, display_name, color)
    pic_parameters_list.append(pic_parameter)

    value_tuple = (2, 4, 6, 8, 10)
    display_name = '偶数'
    color = '#92AB50'
    pic_parameter = gen_pic_parameter(value_tuple, display_name, color)
    pic_parameters_list.append(pic_parameter)

    value_tuple = (2, 3, 5, 7, 11)
    display_name = '质数'
    color = '#FFC000'
    pic_parameter = gen_pic_parameter(value_tuple, display_name, color)
    pic_parameters_list.append(pic_parameter)

    outfile_name = 'numbers.jpg'
    title = '奇特的数字'
    gen_picture(title, pic_parameters_list, outfile_name)       

