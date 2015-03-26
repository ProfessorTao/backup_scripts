#coding:utf-8

import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from traceback import format_exc
#from email.mime.multipart import MIMEMultipart

default_encoding = 'utf8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

def send_mail(to_list, cc_list, sub, content, content_type = 'html', bcc_list = None):
    '''
    to_list:发给谁
    sub:主题
    content:内容
    send_mail("aaa@126.com","sub","content")

    content_type 发送邮件的类型，默认是html格式的邮件，也可以是plain格式的（纯字符形式）
    '''
    #####################
    #设置服务器，用户名、口令以及邮箱的后缀
    # mail_host = "smtp.gmail.com"
    mail_host = 'proxy-in.baidu.com'
    # mail_port = 465
    # mail_user = "backend.mail.everyday"
    mail_user = 'sw_data'
    # mail_pass = "backend123456"
    mail_postfix = 'baidu.com  '
    # mail_postfix = "gmail.com"

    me = mail_user + "<" + mail_user + "@" + mail_postfix + ">"
    # 尝试用utf8和GBK解码邮件内容和主题成unicode
    try:
        content = unicode(content, 'utf8')
        sub = unicode(sub, 'utf8')
    except UnicodeDecodeError:
        print "exception utf8"
        try:
            content = unicode(content, 'gbk')
            sub = unicode(sub, 'gbk')
        except UnicodeDecodeError:
            print format_exc()
            return False
    #已经是unicode
    except TypeError:
        pass

    msg = MIMEText(content.encode('utf-8'), '%s' % content_type, 'UTF-8')
    msg['Subject'] = sub
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    msg['Cc'] = ";".join(cc_list)

    if bcc_list:
        msg['Bcc'] = ';'.join(bcc_list)

    try:
        # s = smtplib.SMTP_SSL()
        s = smtplib.SMTP()
        s.connect(mail_host)
        # s.login(mail_user, mail_pass)
        if bcc_list:
            s.sendmail(me, to_list+cc_list+bcc_list, msg.as_string())
        else:
            s.sendmail(me, to_list+cc_list, msg.as_string())
            
        s.close()
        return True
    except Exception, e:
        print e
        print format_exc()
        return False
# end of def
