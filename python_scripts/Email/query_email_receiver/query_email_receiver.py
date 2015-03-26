# coding: utf-8

import traceback
import csv

def unicode_csv_reader(utf8_data, dialect=csv.excel, **kwargs):
    csv_reader = csv.reader(utf8_data, dialect=dialect, **kwargs)
    for row in csv_reader:
        yield [unicode(cell, 'utf-8') for cell in row]

def gb2312_csv_reader(gb2312_data, dialect=csv.excel, **kwargs):
    csv_reader = csv.reader(gb2312_data, dialect=dialect, **kwargs)
    for row in csv_reader:
        yield [unicode(cell, 'gb2312') for cell in row]

def query_email_receiver(receiver_csv_file):
    to_list, cc_list = [], [] 
    try:
        fp = open(receiver_csv_file, 'r')
        csv_reader = gb2312_csv_reader(fp)
        for line in csv_reader:
            type_str = line[0].strip().lower()
            email_receiver = line[1].strip()
            if 'to' == type_str:
                to_list.append(email_receiver)
            elif 'cc' == type_str:
                cc_list.append(email_receiver)
        fp.close()                         
    except:
        print traceback.format_exc()
    # end of try

    return to_list, cc_list
# end of def query_email_receiver(receiver_csv_file)
    
    
if __name__ == '__main__':
    receiver_csv_file = 'baidu_weishi_daily_flow_receiver.csv'
    to_list, cc_list = query_email_receiver(receiver_csv_file)
    print '  to_list: ', to_list
    print '  cc_list: ', cc_list

