#coding:utf-8
#-------------------------------------------------------------------------------
# Name:        build_html_string
# Purpose:     for codes collected
#
# Author:      taotianyi
#
# Created:     13/10/2014
# Copyright:   (c) baidu 2014
# Licence:     <taotianyi01@baidu.com>
#-------------------------------------------------------------------------------

import tablib
from build_html_table import build_html_table


def build_html_string():
    class_email = build_html_table()
    count = 0
    email_html_str = ''

    #### 1. 表格一
    table_header = ('国家', 'GDP(美元)', '人均GDP(美元)')
    table_content = [   ('美国',   '16,768,050', '53,001'),
                        ('中国',   '9,469,124',  '6,959'),                          
                        ('日本',   '4,898,530',  '38,468'), 
                        ('德国',   '3,635,959',  '44,999'),
                        ('新加坡', '276,520',    '55,182')  ]

    tablib_data = tablib.Dataset(*table_content, headers = table_header)

    count += 1
    form_header = '%d. 2013年各国家GDP状况' % count

    form_html_str = class_email._build_html_str_from_tablib_data(tablib_data, form_header)
    email_html_str += form_html_str


    #### 2. 表格二
    table_header = ('日期', '数据', '状态', '结论')
    table_content = [   ('2014-10-05', 23013, True, '需要改进'),
                        ('2014-10-04', 1387123, False, '需要改进'),                          
                        ('2014-10-03', 4898, False, '不需要改进'), 
                        ('2014-10-02', 612143, False, '不需要改进'),
                        ('2014-10-01', 56083, True, '需要改进')  ]

    tablib_data = tablib.Dataset(*table_content, headers = table_header)

    count += 1
    form_header = '%d. 表格二' % count

    form_html_str = class_email._build_html_str_from_tablib_data(tablib_data, form_header)
    email_html_str += form_html_str

    #### 构造html文本
    email_html_str = class_email._decorate_html(email_html_str)
    return email_html_str    
# end of build_html_string


if __name__ == '__main__':
    html_str = build_html_string()

    file_name = 'display.html'
    fp = open(file_name, 'w')
    fp.write('%s\n' % html_str)
    fp.close()

