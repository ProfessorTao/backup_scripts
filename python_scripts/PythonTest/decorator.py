#coding:utf-8
#-------------------------------------------------------------------------------
# Name:        calculate_time_cost
# Purpose:
#
# Author:      TaoTianYi
#
# Created:     21/06/2014
# Copyright:   (c) TaoTianYi 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import time


def calculate_time_cost(fn):
    def wrapper():
        t1 = time.time()
        print ' ** Begin to run task, the timestamp is %f' % t1

        fn()

        t2 = time.time()
        print ' ** Finish running task, the timestamp is %f, time cost is %f' % (t2, (t2-t1))
        print
    return wrapper
# end of time_cost
