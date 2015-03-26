#coding:utf-8
#-------------------------------------------------------------------------------
# Name:        build_html_table
# Purpose:     for codes collected
#
# Author:      taotianyi
#
# Created:     2014/10/13
# Copyright:   (c) baidu 2014
# Licence:     <taotianyi01@baidu.com>
#-------------------------------------------------------------------------------


import tablib

DEFAULT_STYLE_HTML_STR = '''
    <style type="text/css">
        div{ font-family: "微软雅黑"; font-size: 14px;}
        table{font-size:14px;text-align:center; font-size: 12px; background-color: #ffffff;border:1px solid #000000;font-family: "微软雅黑"; border-collapse:collapse;}

        td,th{ border:1px solid #000000; padding:2px;}
        th{font-weight: bold;}
        thead{background-color: #c6d9f1;}
    
        h1{font-size:18px }
        h2{font-size:16px }
        a{font-size: 14px; color:#7030a0;}

        .bk_ground{background-color: #c6d9f1;}
    </style>'''

DEFAULT_TABLE_STYLE_HTML_STR_BEGIN = '''<div style="overflow:auto;">'''
DEFAULT_TABLE_STYLE_HTML_STR_END = '</div>'

DEFAULT_TABLE_BORDER_HTML_STR = '''<table border="1" cellpadding="0" cellspacing="0" style="overflow:hidden;width:960px">'''


class build_html_table(object):
    def __init__(self):
        pass
    # end of def


    def __decorate_html_table(self, html_str_to_handle, border_str, header_str = None):
        replace_str = '<table>'
        html_decoreated = html_str_to_handle.replace(replace_str, border_str)

        if header_str:
            header_html = '<h1>%s</h1>' % header_str
            html_decoreated = header_html + html_decoreated

        return html_decoreated
    # end of def


    def _build_html_str_from_tablib_data(self, tablib_data, header_str = None):
        border_str = DEFAULT_TABLE_BORDER_HTML_STR
        table_str_decoreated = self.__decorate_html_table(tablib_data.html, border_str, header_str)
        
        table_style_begin, table_sytle_end = DEFAULT_TABLE_STYLE_HTML_STR_BEGIN, DEFAULT_TABLE_STYLE_HTML_STR_END
        html_str = '%s%s%s' % (table_style_begin, table_str_decoreated, table_sytle_end)
        return html_str
    # end of def


    def _add_picture(self, pic_name_in_html, header_str = None):
        border_str = DEFAULT_TABLE_BORDER_HTML_STR
        html_picture = ''

        if header_str:
            html_picture += '<h1>%s</h1>' % header_str

        html_picture += '''<img src="cid:%s">''' % pic_name_in_html
        html_picture += DEFAULT_TABLE_STYLE_HTML_STR_END
        return html_picture
    # end of def


    def _decorate_html(self, html_content, header_decorated = DEFAULT_STYLE_HTML_STR):
        html_str = header_decorated
        return html_str + html_content
    # end of def
    
# end of class
