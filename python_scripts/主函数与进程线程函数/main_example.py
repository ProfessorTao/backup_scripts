#coding:utf-8
#-------------------------------------------------------------------------------
# Name:        main_example
# Purpose:
#
# Author:      TaoTianYi
#
# Created:     2014/12/20
# Copyright:   (c) TaoTianYi 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def daily_task(date_str):
    pass
# end of def


def main():
    # 1. 组建某天时间列表，如果没有参数传入，默认昨天
    import sys
    import time_func

    if 2 == len(sys.argv):
        # 有一个参数时，就使用指定的日期，如果是today, yesterday 就用今天或昨天的日期
        if 'today' == sys.argv[1]:
            target_date_str = time_func.get_n_day_before_str(0)
        elif 'yesterday' == sys.argv[1]:
            target_date_str = time_func.get_n_day_before_str(1)
        elif 'tomorrow' == sys.argv[1]:
            target_date_str = time_func.get_n_day_before_str(-1)
        else:
            target_date_str = sys.argv[1]
        target_date_list = [target_date_str]
    elif 1 == len(sys.argv):
        # 无参数时，默认使用昨天的数据
        target_date_str = time_func.get_n_day_before_str(1)
        target_date_list = [target_date_str]
    elif 3 == len(sys.argv):
        # 有两个参数时，取两天日期之间的数据
        target_date_list = time_func.get_day_list_between_two_datestr(sys.argv[1], sys.argv[2])
    else:
        print "  Error Parameters: "
        for item in sys.argv:
            print "%s " % item
        exit(-1)

    # 2. 开始计算
    print target_date_list

    for date_str in target_date_list:
        print date_str
        daily_task(date_str)
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
       


