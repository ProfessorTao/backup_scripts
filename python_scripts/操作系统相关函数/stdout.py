#!/local/bin/env python
#encoding:utf-8

# author:  taotianyi01@baidu.com
# date: 2013-10-30

import sys

class StdoutToStr():
    def __init__(self, file_path, b_realtime = False):
        self.__real_time = b_realtime
        self.__path = file_path
        self.fp = open(file_path, 'w')

    def __del__(self):
        self.fp.flush()
        self.fp.close()

    def flush(self):
        self.fp.flush()

    def write(self, buf):
        self.fp.write(buf)
        if self.__real_time:
            self.flush()
            
# end of class StdoutToStr()

class StdOut():
    def __init__(self): 
        self.old_stdout = sys.stdout
        self.old_stderr = sys.stderr

        self.__new_stderr = None
        self.__new_stdout = None


    def redirect(self, std_out_file_path = None, std_err_file_path = None, b_realtime = False):
        if std_out_file_path:
            self.__new_stdout = StdoutToStr(std_out_file_path, b_realtime)
            sys.stdout = self.__new_stdout
        if std_err_file_path:
            self.__new_stderr = StdoutToStr(std_err_file_path, b_realtime)
            sys.stderr = self.__new_stderr


    def __del__(self):
        if self.__new_stdout:
            sys.stdout = self.old_stdout
            self.__new_stdout = None
        if self.__new_stderr:
            sys.stderr = self.old_stderr
            self.__new_stderr = None

# end of class StdOut()


