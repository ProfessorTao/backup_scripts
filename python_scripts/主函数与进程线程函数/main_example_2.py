#coding:utf-8
#-------------------------------------------------------------------------------
# Name:        main_example
# Purpose:
#
# Author:      TaoTianYi
#
# Created:     21/06/2014
# Copyright:   (c) TaoTianYi 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def whole_task(target_date_list):
    pass
# end of def    

def daily_task(date_str):
    pass
# end of def

def run_task(task_type, target_date_list):
    if 1 == task_type:
        # 每天运行一次
        for date_str in target_date_list:
            print date_str
            daily_task(date_str)
    elif 2 == task_type:
        # 一次性运行
        whole_task(target_date_list)
# end of def run_task


def build_date_list(target_date_str, begin_date_str, end_date_str):
    import time_func

    input_list = [target_date_str, begin_date_str, end_date_str]
    for index, date_str in enumerate(input_list):
        # 如果是today, yesterday 就用今天或昨天的日期
        if 'today' == date_str:
            input_list[index] = time_func.get_n_day_before_str(0)
        elif 'yesterday' == date_str:
            input_list[index] = time_func.get_n_day_before_str(1)
        elif 'tomorrow' == date_str:
            input_list[index] = time_func.get_n_day_before_str(-1)
    # end of for   

    [target_date_str, begin_date_str, end_date_str] = input_list

    if target_date_str:
        # 使用指定的某天日期
        date_list = [target_date_str]
        return date_list

    if begin_date_str and end_date_str:
        # 使用指定的日期范围
        date_list = time_func.get_day_list_between_two_datestr(begin_date_str, end_date_str)
        return date_list

    if None == target_date_str and None == begin_date_str and None == end_date_str:
        # 没有任何日期作为输入，就默认使用昨天的日期
        target_date_str = time_func.get_n_day_before_str(1)
        date_list = [target_date_str]
        return date_list

    # 其他情况，视为输入错误
    return list() # error input
# end of def


def main():
    # 1. 组建某天时间列表，如果没有参数传入，默认昨天
    import sys
    from getopt import getopt    

    options, args = getopt(sys.argv[1:], "b:e:d:", ["begin=", 'end=', 'date='])
    begin_date_str, end_date_str, target_date_str = None, None, None

    for element in options:
        left, right = element[0], element[1]
        if '-b' == left or '--begin' == left:
            begin_date_str = right
        if '-e' == left or '--end' == left:
            end_date_str = right
        if '-d' == left or '--date' == left:
            target_date_str = right
    # end of for

    args_length = len(args)
    if None == target_date_str and args_length > 0:
        target_date_str = args[0]    

    target_date_list = build_date_list(target_date_str, begin_date_str, end_date_str)
    if not target_date_list:
        print "  Error Parameters: "
        for item in sys.argv:
            print "%s " % item
        exit(-1)
        

    # 2. 开始计算
    print target_date_list
    task_type = 1
    run_task(task_type, target_date_list)
    # end of for        
# end of main

if __name__ == '__main__':
    import time
    split_line = '=' * 100
    print split_line

    now_str = time.ctime()
    print '  *** Begin: %s ***' % now_str

    main()      

    now_str = time.ctime()
    print '  *** End: %s ***\n\n' % now_str    
       


