# -*- coding:utf8 -*-
import smtplib
import sys
from email.mime.text import MIMEText
#https://blog.csdn.net/weixin_44915703/article/details/104417030?fps=1&locationNum=2

reload(sys)
sys.setdefaultencoding('utf-8')

def send_mail(subject, toWho, message):
    # 登陆邮箱
    sent = smtplib.SMTP()
    sent.connect('smtp.qq.com', 25)
    # 发件人邮箱地址
    mail_name = "107xxxx@qq.com"
    # 填写邮箱的授权码,不是密码
    mail_pw = "bxbgubqmjuaobfcc"
    # 登陆
    sent.login(mail_name, mail_pw)

    # 编辑信息
    # 收件人邮箱地址
    to = toWho
    # 发送内容
    content = MIMEText(message)
    # 邮件标题
    content['Subject'] = subject
    # 发送人
    content['From'] = mail_name
    # 接收人(用逗号连接多个邮箱地址,实现群发邮件)
    content['To'] = ','.join(to)

    # 发送邮件
    try:
        # 发送人, 收件人, 邮件内容
        sent.sendmail(mail_name, to, content.as_string())
        print('Send email Success')
        sent.close()
    except smtplib.SMTPException:
        print('Send Email Failed')

if __name__ == '__main__':
    subject = "关于Python自动发送邮件到指定邮箱的测试"
    to = ['24754593@qq.com', "626961894@qq.com"]
    content = "关于测试Python自动发送邮件的测试, \n利用python测试法邮件功能, \n代码实现不复杂, \n但是需要发邮件的账号开启第三方客户端授权码, 才可以正常发送邮件, \n否则会提示登录失败, 或者发送邮件异常退出等."
    send_mail(subject, to, content)