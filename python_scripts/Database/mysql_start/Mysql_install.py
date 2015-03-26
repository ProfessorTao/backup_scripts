#!/usr/bin/python
#coding=utf-8

import sys
import os
import glob
import datetime
from subprocess import call
import pprint
import traceback
import time
import re

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage



class MysqlInstall():
	def __init__(self):
# 		self.cnx = MySQLdb.connect(unix_socket="/tmp/mysql.sock",user="root")
# 		self.cnx = MySQLdb.connect(host="10.52.172.56",user="root",passwd="root9527",db='',port=8306,charset="utf8")
# 		self.cursor = self.cnx.cursor(MySQLdb.cursors.DictCursor)
		
		self.basedir = '/home/work/local/mysql'
		self.datadir = '/home/work/data/mysql_tty/data'
		self.tmpdir = '/home/work/data/mysql_tty/tmp'
		self.logdir = '/home/work/data/mysql_tty/log'
		self.filename = 'mysql-5.6.17-linux-glibc2.5-x86_64.tar.gz'
		self.install()
		
	def install(self):
# 		subprocess.call("tar -zxvf %s" % self.filename,shell=True)
		if os.path.exists(self.datadir):
			print 'Error! %s already exists' % self.datadir
			sys.exit(1)
		if os.path.exists(self.basedir):
			print ' %s already exists' % self.basedir
		else:
			call("tar -zxf %s" % self.filename,shell=True)
			call("mv %s %s" % (self.filename[:-7],self.basedir),shell=True)
		
		call("mkdir -p %s" % self.datadir,shell=True)
		os.mkdir(self.tmpdir)
		os.mkdir(self.logdir)
		
		if not os.path.exists('my.cnf'):
			print 'Error! my.cnf is not exists'
			sys.exit(1)
		call("cp %s %s" % ('my.cnf',self.datadir),shell=True)
		os.chdir(self.basedir)
		call("./scripts/mysql_install_db --defaults-file=%s/my.cnf" % self.datadir,shell=True)
# 		call("echo 'export PATH=/home/work/local/mysql/bin:$PATH' >> ~/.bashrc && source ~/.bashrc \
# 			  && mysqld_safe --defaults-file=%s/my.cnf --ledir=/home/work/local/mysql/bin/ &" % self.datadir,shell=True)
		
# 		call("mysqld_safe --defaults-file=%s/my.cnf --ledir=/home/work/local/mysql/bin/ &" % self.datadir,shell=True)
# 		call("ln -s %s/mysql.sock /tmp/mysql.sock" % self.datadir,shell=True)
		


if __name__== '__main__':
	mysqlInstall = MysqlInstall()





