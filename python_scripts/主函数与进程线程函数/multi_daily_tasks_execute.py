#coding:utf-8
#-------------------------------------------------------------------------------
# Name:        multi_daily_tasks_execute
# Purpose:
#
# Author:      taotianyi
#
# Created:     2015/01/06
# Copyright:   (c) baidu 2015
# Licence:     <taotianyi01@baidu.com>
#-------------------------------------------------------------------------------


PROCESS_NUM = 10

from multiprocessing import Pipe
from multiprocessing import Process

import main_example

def daily_process_task(date_str):
    main_example.daily_task(date_str)
# end of def


def each_process_task(child_pipe):
    date_array = child_pipe.recv()
    for date_str in date_array:
        daily_process_task(date_str)
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

    day_number = len(target_date_list)
    if day_number < PROCESS_NUM:
        process_num = day_number
    else:
        process_num = PROCESS_NUM

    each_process_day_number = day_number / process_num
    remain_process_number = day_number % process_num

    # Build a pipe
    parent_pipe, child_pipe = Pipe()

    process_list = []
    begin, end = 0, 0
    for i in range(process_num):
        begin = end
        end = begin + each_process_day_number
        if remain_process_number > 0:
            end += 1
            remain_process_number -= 1

        if i != (process_num - 1):
            each_date_list = target_date_list[begin:end]
        else:
            each_date_list = target_date_list[begin:]

        print 'Task No. %d, Date List: ' % i, each_date_list

        parent_pipe.send(each_date_list)
        each_task = Process( target=each_process_task, args=(child_pipe, ) )
        process_list.append(each_task)
    # end of for

    print 'Number of Process List is %d' % len(process_list)

    
    for each_task in process_list:
        each_task.start()

    for each_task in process_list:
        each_task.join()
    
    print '** All Process Tasks Finish! **'       
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
       
                
                