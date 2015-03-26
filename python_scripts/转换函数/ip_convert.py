#encoding:utf-8
#-------------------------------------------------------------------------------
# Name:        ip_convert
# Purpose:
#
# Author:      taotianyi
#
# Created:     09/01/2014
# Copyright:   (c) taotianyi 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def ip_int_to_str(ip_int):
    ip_str_list = []
    base = 0xff
    for i in range(4):
        number = (ip_int & (base<<(i*8)) ) >> (i*8)
        ip_str_list.append(str(number))

    ip_str_list.reverse()
    return '.'.join(ip_str_list)


def ip_str_to_int(ip_str):
    ip_str_list = ip_str.split('.')
    if 4!=len(ip_str_list):
        raise 'Error Input!'

    ip_str_list.reverse()
    ip_int = 0
    for n, item in enumerate(ip_str_list):
        ip_element = int(item)
        ip_int |= (ip_element << n*8)

    return ip_int


if __name__ == '__main__':
    print ip_int_to_str(3689901706)
    print ip_str_to_int('219.239.110.138')
