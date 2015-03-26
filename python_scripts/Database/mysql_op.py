#!/usr/bin/python
#coding=utf-8

import MySQLdb
#import DataOp

class MySql_Operation():
    '''
    def __init__(self, db_host_name='mysql00', db_name = None):
        self.__conn = DataOp.GetDBConnect(db_host_name)
        self.__cur = self.__conn.cursor()
        self.__sscur = None  # SSCursor

        if db_name:
            self.change_db(db_name)
    # end of def __init__
    '''
    
    def __init__(self, db_host, db_port, db_user, db_passwd = '', db_name = ''):
        #from comdef import IS_TESTING
        #if IS_TESTING:
        #    from warnings import filterwarnings
        #    # 测试环境，捕捉警告信息
        #    filterwarnings('error', category = MySQLdb.Warning)

        self.__host = db_host
        self.__port = db_port
        self.__user = db_user
        self.__passwd = db_passwd
        self.__name = db_name

        self.__conn = None
        self.__cur = None
        self.__sscur = None  # SSCursor

        self.__get_conn()
    # end of __init__

    def __del__(self):
        if self.__conn:
            if self.__cur:
                self.__cur.close()
                self.__cur = None
            # end of if self.__cur
            
            if self.__sscur:
                self.__sscur.close()
                self.__sscur = None
            # end of if self.__sscur

            self.__conn.close()
            self.__conn = None
        # end of if self.__conn
    # end of __del__

    
    def __get_conn(self):
        try:
            self.__conn = MySQLdb.connect(host=self.__host, user=self.__user, passwd=self.__passwd, db=self.__name, port=self.__port, charset="utf8", local_infile = 1)
            self.__cur = self.__conn.cursor()
            print "client cursor connect ok---%s" % self.__host
        except MySQLdb.Error, e:
            print("mysql_error, %s: %s", e.args[0], e.args[1])
        except Exception, e:
            print("mysql_error, %s:", e)
    # end of def __get_conn
    

    def change_db(self, db_name):
        if self.__cur:
            self.__cur.close()
            self.__cur = None

        self.__conn.select_db(db_name)
        self.__cur = self.__conn.cursor()
    # end of change_db

    '''
    def fetchmany(self, sql_cmd, size=5000):
        cursor = self.__conn.cursor(MySQLdb.cursors.SSDictCursor) 
        cursor.execute(sql_cmd)
        while True:
            results = cursor.fetchmany(size)
            if not results:
                break
            for row in results:
                yield row
        cursor.close()
    '''
    
    def execute_sql(self, sql, param = (), bSSCursor = False):
        # print("execute sql:%s", sql)
        try:
            if not bSSCursor:
                if None == self.__cur:
                    self.__cur = self.__conn.cursor()
                self.__cur.execute(sql, param)
                self.__conn.commit()
            else:
                # with sscursor
                self.__sscur.execute(sql, param)
        except MySQLdb.Warning, w:
            sqlWarning =  "Mysql Warning: %s" % str(w)
            print "%s, sql is %s" % (sqlWarning, sql)
        except MySQLdb.Error, e:
            print "Mysql Error %s: %s, sql is \n%s" % (e.args[0], e.args[1], sql)
        except Exception, e:
            print "Mysql Error %s, sql is \n%s" % (e, sql)
    # end of def execute_sql(self, sql, param = ())


    def traverse_table(self, sql):
        self.__cur.execute(sql)
        self.execute_sql(sql)
        rows = self.__cur.fetchall()
        return rows
    # end of def traverse_table

    def traverse_table_with_sscursor(self, sql):
        # with sscursor
        if self.__sscur :
            # reopen sscursor firstly
            self.__sscur.close()
            self.__sscur = None

        self.__sscur = self.__conn.cursor(MySQLdb.cursors.SSCursor)
        self.execute_sql(sql, bSSCursor = True)
        return self.__sscur
    # end of traverse_table_with_sscursor

    def load_data_to_db(self, path, db_name, tb_name, split_char):
        sql = "load data CONCURRENT local infile '%s' replace into table %s.%s fields terminated by '%s'" % (path, db_name, tb_name, split_char)
        print("load file sql:%s", sql)
        self.execute_sql(sql)
    # end of def load_data_to_db

# end of class MySql_Operation

