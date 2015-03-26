#coding:utf-8
#-------------------------------------------------------------------------------
# Name:        time_func
# Purpose:     for codes collected
#
# Author:      taotianyi
#
# Created:     2015/01/06
# Copyright:   (c) baidu 2015
# Licence:     <taotianyi01@baidu.com>
#-------------------------------------------------------------------------------

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import time
import datetime
from datetime import date, datetime, timedelta

import traceback

# datetime to timestamp
datetime_to_timestamp = lambda x: time.mktime(x.timetuple())

# date to date_str
date_to_date_str = lambda date_info, format_str="%d%02d%02d": format_str % (date_info.year, date_info.month , date_info.day)

# datetime to date_str
datetime_to_date_str = lambda date_time, format_str="%d%02d%02d": format_str % (date_time.year, date_time.month , date_time.day)

# 获取从指定日期零时的时间戳
get_date_zero_timestamp = lambda date_str, format_str="%Y%m%d": int( time.mktime( time.strptime(date_str, format_str) ) )

# 获取从当天起第n前天的日期格式，第0天为当天，第1天为昨天，默认当天，第-1天为明天
get_n_day_before_str   = lambda nBefore=0, format_str="%Y%m%d": time.strftime(format_str, time.localtime(int(time.time()) - nBefore*86400))


# date_str -> date
def date_str_to_date(date_str, format_str="%Y%m%d"):
    try:
        t = time.strptime(date_str, format_str)
        date_info = date(t.tm_year, t.tm_mon, t.tm_mday)
        return date_info
    except:
        print '** The input Parameters is Incorrect!'
        print traceback.format_exc()
        return None
# end of def date_str_to_date


# date_str -> datetime
def date_str_to_datetime(date_str, format_str="%Y%m%d"):
    try:
        t = time.strptime(date_str, format_str)
        date_info = datetime(t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec)
        return date_info
    except:
        print '** The input Parameters is Incorrect!'
        print traceback.format_exc()
        return None        
# end of def date_str_to_date


# 获取指定的日期的后n天的时间日期，默认第0天，即当天，第-1天为昨天
def get_datestr_after_target_datestr(date_str, nAfter = 0, format_str = '%Y%m%d'):
    try:
        t = time.strptime(date_str, format_str)
        t_stamp = time.mktime(t)
        t_stamp = t_stamp + nAfter * 86400
        t = time.localtime(t_stamp)
        return time.strftime(format_str, t)
    except:
        print '** The input Parameters is Incorrect!'
        print traceback.format_exc()
        return None
# end of def get_datestr_after_target_datestr


# 获取指定的日期的后n天的时间日期，默认第0天，即当天，第-1天为昨天
def get_datestr_after_target_date(year, month, day, nAfter = 0, format_str = '%Y%m%d'):
    try:
        time_struct_tuple = (year, month, day, 0, 0, 0, 0, 0, 0)
        t = time.struct_time(time_struct_tuple)
        t_stamp = time.mktime(t)
        t_stamp = t_stamp + nAfter * 86400
        t = time.localtime(t_stamp)
        return time.strftime(format_str, t)
    except:
        print '** The input Parameters is Incorrect!'
        print traceback.format_exc()
        return None
# end of def get_datestr_after_target_date


# 获取两个指定日期之间的所有日期
def get_day_list_between_two_date(date_begin, date_end):
    if not isinstance(date_begin, date) or not isinstance(date_end, date):
        print '** The input Parameters is not Type Date!'
        return None

    date_list_between = list()
    one_day_timespan = timedelta(days = 1)
    while date_begin <= date_end:
        date_list_between.append(date_begin)
        date_begin += one_day_timespan
    # end of while

    return date_list_between
# end of def get_day_list_between_two_date


# 获取两个指定日期之间的所有日期，日期默认为形如20140401数字形式
def get_day_list_between_two_datestr(date_str_begin, date_str_end, format_str = '%Y%m%d'):
    try:
        t1 = time.strptime(date_str_begin, format_str)
        t2 = time.strptime(date_str_end, format_str)
    except:
        print '** The input Parameters is Incorrect!'
        print traceback.format_exc()
        return None

    date_begin = date(t1.tm_year, t1.tm_mon, t1.tm_mday)
    date_end = date(t2.tm_year, t2.tm_mon, t2.tm_mday)
    
    date_list_between = get_day_list_between_two_date(date_begin, date_end)
    date_str_list_between = list()

    for date_info in date_list_between:
        date_str = date_info.strftime(format_str)
        date_str_list_between.append(date_str)

    return date_str_list_between
# end of get_day_list_between_two_datestr


# 获取两个指定日期之间的天数, 日期默认为形如20140401数字形式
def get_day_count_between_two_datestr(date_str_begin, date_str_end, format_str="%Y%m%d"):
    timestamp_begin = int( time.mktime( time.strptime(date_str_begin, format_str) ) )
    timestamp_end = int( time.mktime( time.strptime(date_str_end, format_str) ) )

    return (timestamp_end - timestamp_begin) / 86400
# end of def


def get_seconds_between_two_timestamp(time_based, time_judged):
    # 限制传入的两个参数都是datetime.datetime类型
    if not isinstance(time_based, datetime) or not isinstance(time_judged, datetime):
        print '** The input Parameters is not Type Datetime!'
        return None

    timestamp_1 = int( time.mktime(time_based.timetuple()) )
    timestamp_2 = int( time.mktime(time_judged.timetuple()) )
    return abs(timestamp_2 - timestamp_1)
# end of def


# 获取指定日期当月的所有日期信息
def get_month_date(target_date):
    # 限制传入的参数是datetime.date类型
    if not isinstance(target_date, date):
        print 'Parameters are incorrect in get_month_date!'
        return None

    year, month = target_date.year, target_date.month
    day_list = range(1, 32, 1)

    month_date_list = []
    for each_day in day_list:
        try:
            each_date = date(year, month, each_day)
            month_date_list.append(each_date)
        except ValueError:
            break
    # end of for

    return month_date_list
# end of def


