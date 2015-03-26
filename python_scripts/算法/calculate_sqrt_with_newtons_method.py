# coding:utf-8

def calculate_iteratively(N, x0, total_times):
    begin = 1;
    x = x0

    for i in range(begin, total_times):
        x = (x + N/x) / 2

    return x
# end of def


def calculate_sqrt(number):
    ## 算平方根 -> y = x^2 - number
    x0 = 1 ## 猜测的初始值，与迭代次数一起，影响结果的精度
    N = float(number)
    total_times = 1000
    return calculate_iteratively(N, x0, total_times)
# end of def

print calculate_sqrt(1000)

