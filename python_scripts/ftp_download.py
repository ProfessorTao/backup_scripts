#coding:utf-8

import os, sys, time
reload(sys)
sys.setdefaultencoding('utf8')

CUR_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.append(CUR_PATH + "/../common")

import getopt
import traceback
import ftplib
from ftplib import FTP 

from multiprocessing import Process

import time_func
from comdef import *


def get_type_list(type_file_name):
    fp = open(type_file_name)
    type_list = []
    for line in fp:
        type = line.strip()
        type_list.append(type)
    # end of for
    fp.close()
    return type_list
# end of def


#def ftp_up(file_name = "20120904.rar"): 
#    ftp=FTP() 
#    ftp.set_debuglevel(2)#打开调试级别2，显示详细信息;0为关闭调试信息 
#    ftp.connect('192.168.0.1','21')#连接 
#    ftp.login('admin','admin')#登录，如果匿名登录则用空串代替即可 
#    #print ftp.getwelcome()#显示ftp服务器欢迎信息 
#    #ftp.cwd('xxx/xxx/') #选择操作目录 
#    bufsize = 1024#设置缓冲块大小 
#    file_handler = open(filename,'rb')#以读模式在本地打开文件 
#    ftp.storbinary('STOR %s' % os.path.basename(filename),file_handler,bufsize)#上传文件 
#    ftp.set_debuglevel(0) 
#    file_handler.close() 
#    ftp.quit() 
#    print "ftp up OK" 
 
def ftp_down(ftp, remote_host, remote_log_path, local_dir, cmdid, filter_str): 
    #ftp.set_debuglevel(2) 
    #ftp.cwd(remote_log_path) #选择操作目录 

    remote_file_list = ftp.nlst(remote_log_path)

    bufsize = 1024
    ftp.voidcmd('TYPE I')  # 以二进制模式传输信息，否则有编码问题

    mid_folder = remote_log_path.replace('/', '_')
    midfix = 'cmdid_%s/%s' % (cmdid, mid_folder)

    for remote_file_name in remote_file_list:
        if not filter_str in remote_file_name:
            # 过滤此文件
            continue
        
        if 0 == ftp.size(remote_file_name):
            # 文件大小是0
            continue

        file_name = remote_file_name.split('/')[-1]
        local_folder = "%s/%s/%s" % (local_dir, remote_host, midfix)
        if not os.path.exists(local_folder):
            os.system("mkdir -p %s" % local_folder)
        local_file_name = "%s/%s" % (local_folder, file_name)

        fp = open(local_file_name, 'wb')
        file_handler = fp.write #以写模式在本地打开文件

        print "REMOTE: %s  =>  LOCAL: %s" % (remote_file_name, local_file_name)
        try:
            #ftp.retrbinary('RETR %s' % os.path.basename(remote_file_name), file_handler, bufsize)#接收服务器上文件并写入本地文件 
            ftp.retrbinary('RETR %s' % remote_file_name, file_handler, bufsize)#接收服务器上文件并写入本地文件
        except:
            print traceback.format_exc()

        fp.close() 
    # end of for remote_file_name in remote_file_list


    ##ftp.set_debuglevel(0) 
# end of def ftp_down(remote_host, remote_dir, local_dir, cmdid, filter_str, ftp_port = 21)


def download_log(ftp, remote_host, remote_dir, local_dir, cmdid_list, filter_str):
    folder_filter = 'data'

    remote_folder_list = ftp.nlst(remote_dir)
    for each_folder in remote_folder_list:
        if folder_filter not in each_folder:
            continue

        #print '  target: %s' % each_folder
        remote_log_storing_dir = each_folder

        for cmdid in cmdid_list:
            try:
                remote_log_path = "%s/%s" % (remote_log_storing_dir, cmdid)
                ftp.cwd(remote_log_path)            
            except ftplib.error_perm:
                # 不存在此目录
                continue
            except:
                print traceback.format_exc()
                continue
            
            ftp_down(ftp, remote_host, remote_log_path, local_dir, cmdid, filter_str)
        # end of for cmdid in cmdid_list
    # end of for each_folder in remote_folder_list
# end of def download_log(remote_host, remote_dir, local_dir, cmdid_list, filter_str)


def process_task(target_date, remote_host, run_method, *arg_list):
    # check parameters
    b_incorrect = True
    arg_length = len(arg_list)
    
    filter_str_list = []
    if "day" == run_method:
        if 0 == arg_length:
            b_incorrect = False

            filter_str = target_date
            filter_str_list.append(filter_str)
    elif "hour" == run_method:
        if 1 == arg_length:
            target_hour = arg_list[0]
            b_incorrect = False

            filter_str = "%s%02d" % (target_date, target_hour)
            filter_str_list.append(filter_str)
    elif "with" == run_method:
        if 2 == arg_length:
            hour_start, hour_end = arg_list[0], arg_list[1]
            b_incorrect = False

            s, e = hour_start, hour_end 
            for i in range(s, e):
                filter_str = "%s%02d" % (target_date, i)
                filter_str_list.append(filter_str)
    # end of if

    if b_incorrect:
        # 参数错误
        print "Error Parameter in function process_task: ", arg_list
        return -1        

    # 参数正确，继续执行
    type_file_name = FILE_TYPE_LIST
    cmdid_list = get_type_list(type_file_name)

    remote_dir = REMOTE_LOGS_PATH
    local_dir = FILE_LOGS_PATH

    user_name = "work"
    user_passwd = "xf_server@baidu"
    ftp_port = 21

    ftp=FTP() 
    ftp.connect(remote_host,ftp_port) 
    ftp.login(user_name, user_passwd) 

    print " -- Ftp (%s) download has started --" % (remote_host)

    #print ftp.getwelcome()#显示ftp服务器欢迎信息 


    for filter_str in filter_str_list:
        # print filter_str
        download_log(ftp, remote_host, remote_dir, local_dir, cmdid_list, filter_str)

    ftp.quit()
    print " -- Ftp (%s) download has finished --" % (remote_host)
# end of def process_task



def main():    
    try:
        options, args = getopt.getopt(sys.argv[1:], "hdwt:s:e:",["hourly", "dayly", "with", "target=", "start=","end="])
    except getopt.GetoptError:
        exit(-1) 

    target_date = None
    run_method = INTERVAL_TYPE
    hour_start = None
    hour_end = None

    for item_tuple in options:
        if "-t" == item_tuple[0] or "--target" == item_tuple[0]:
            target_date = item_tuple[1]
        if "-h" == item_tuple[0] or "--hourly" == item_tuple[0]:
            run_method = "hour"
        if "-d" == item_tuple[0] or "--dayly" == item_tuple[0]:
            run_method = "day"
        if "-w" == item_tuple[0] or "--with" == item_tuple[0]:
            run_method = "with"
        if "-s" == item_tuple[0] or "--start" == item_tuple[0]:
            hour_start = int(item_tuple[1])
        if "-e" == item_tuple[0] or "--end" == item_tuple[0]:
            hour_end = int(item_tuple[1])
    # end of for item_tuple in options
    
    cmd_id_tuple = args
    print cmd_id_tuple
    return
    
    if "hour" == run_method:
        # 以每小时运行一次的模式运行
        # 获取前一个小时的小时数
        now = int(time.time())
        one_hour_ago = now - 60*60
        tm_one_hour_ago = time.localtime(one_hour_ago)
        hour_one_hour_ago = tm_one_hour_ago.tm_hour

        target_hour = hour_one_hour_ago
        target_date = time.strftime('%Y%m%d', tm_one_hour_ago) # 使用一个小时之前的日期

    elif "day" == run_method:
        # 以每天运行一次的模式运行
        # 如果没有指定日期，就默认使用先前获取的昨天日期
        if not target_date:
            # 没有指定日期，默认使用昨天
            target_date = time_func.get_n_day_str(1) # 默认使用昨天的日期
        target_hour = None

    elif "with" == run_method:
        if None == target_date or None == hour_start or None == hour_end or hour_end < hour_start:
            print "Error Parameters!"
            exit(-1)    
    else:
        print "  Error run method: %s" % run_method
        exit(-1)


    # 获取日志主机名
    remote_host_file_name = FILE_REMOTE_LIST
    remote_host_list = get_type_list(remote_host_file_name)

    print remote_host_list

    process_list = []
    for remote_host in remote_host_list:
        if "day" == run_method:
            proc = Process( target=process_task, args=(target_date, remote_host, run_method) )
        elif "hour" == run_method:
            proc = Process( target=process_task, args=(target_date, remote_host, run_method, target_hour) )
        elif "with" == run_method:
            proc = Process( target=process_task, args=(target_date, remote_host, run_method, hour_start, hour_end) )
        else:
            continue
        process_list.append(proc)
    # end of for remote_host in remote_host_list

    t1 = time.time()
    for item in process_list:
        item.start()
    for item in process_list:
        item.join()
    t2 = time.time()
    delta_t = t2 - t1

    download_path = FILE_LOGS_PATH
    print '\n! %s: All logging files have been downloaded to %s, and total time consuming is %fs' % (target_date, download_path, delta_t)
# end of def main()



if __name__ == '__main__':

    split_line = '=' * 100
    print split_line
    now_str = time.ctime()
    print '  *** Begin: %s ***' % now_str

    main()

    now_str = time.ctime()
    print '  *** End: %s ***\n\n' % now_str
    

