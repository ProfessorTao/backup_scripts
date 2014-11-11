#!/usr/bin/python
#coding:utf-8
import time
import smtplib

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from traceback import format_exc

class Email(object):
    """使用百度邮件服务器发送邮件
    """

    def __init__(self, me, to_list, bcc_list, sub, content):
        '''
        to_list:发给谁
        sub:主题
        content:内容
        send_mail("aaa@126.com","sub","content")
        '''
        #####################
        #设置服务器，用户名、口令以及邮箱的后缀
        self.mail_user = me
        self.to_list = to_list
        self.bcc_list = bcc_list

        self.mail_host = 'proxy-in.baidu.com'
        self.mail_postfix = 'baidu.com'

        self.me = self.mail_user + "<" + self.mail_user + "@" + self.mail_postfix + ">"
        # 尝试用utf8和GBK解码邮件内容和主题成unicode
        try:
            content = unicode(content, 'utf8')
            sub = unicode(sub, 'utf8')
        except UnicodeDecodeError:
            try:
                content = unicode(content, 'gbk')
                sub = unicode(sub, 'gbk')
            except UnicodeDecodeError:
                print format_exc()
                return False
        #已经是unicode
        except TypeError:
            pass

        self.msg = MIMEMultipart('related')
        self.msg['Subject'] = sub
        self.msg['From'] = self.me
        self.msg['To'] = ";".join(self.to_list)
        self.msg['Bcc'] = ";".join(self.bcc_list)
        
        txt = MIMEText(content.encode('utf-8'), 'html', 'UTF-8')
        self.msg.attach(txt)

    #####public#####
    def add_image(self, file_name, cid_tag):

        image = MIMEImage(open(file_name, 'rb').read())
        image.add_header('Content-ID', '<'+cid_tag+'>')
        #image.add_header("Content-Disposition", "inline", filename=file_name)
        #image.add_header('Content-Disposition', 'attachment', filename=file_name)
        self.msg.attach(image)

    def send_mail(self):
        retry_times = 0
        # 每隔三秒重试一次 100次后退出
        while retry_times <= 100:
            result = self._send_mail()
            if result == True:
                break
            time.sleep(3) # 等待3s
            retry_times += 1

    #####private####
    def _send_mail(self):
        try:        
            s = smtplib.SMTP()
            s.connect(self.mail_host)        
            s.sendmail(self.me, self.to_list+self.bcc_list, self.msg.as_string())
            s.close()
            return True
        except Exception, e:
            print e
            print format_exc()
            return False

if __name__ == "__main__":
    pass
