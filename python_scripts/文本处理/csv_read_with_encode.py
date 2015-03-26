#coding:utf-8
#-------------------------------------------------------------------------------
# Name:        csv_read_with_encode
# Purpose:
#
# Author:      TaoTianYi
#
# Created:     21/06/2014
# Copyright:   (c) TaoTianYi 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import csv


def unicode_csv_reader(utf8_data, dialect=csv.excel, **kwargs):
    csv_reader = csv.reader(utf8_data, dialect=dialect, **kwargs)
    for row in csv_reader:
        yield [unicode(cell, 'utf-8') for cell in row]

def gb2312_csv_reader(gb2312_data, dialect=csv.excel, **kwargs):
    csv_reader = csv.reader(gb2312_data, dialect=dialect, **kwargs)
    for row in csv_reader:
        yield [unicode(cell, 'gb2312') for cell in row]


def read_csv_data(csv_file_name, encode = None):
    fp = file(csv_file_name, 'rb')

    if 'utf-8' == encode:
        csv_reader = unicode_csv_reader(fp)
    elif 'gb2312' == encode:
        csv_reader = gb2312_csv_reader(fp)
    else:
        csv_reader = csv.reader(fp)

    data_list = []

    for line in csv_reader:
        data_list.append(line)
    # end of for line in csv_reader:

    fp.close()

    return data_list
# end of def
