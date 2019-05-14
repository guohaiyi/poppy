# -*- coding: UTF-8 -*-
import smtplib
import os
from email.mime.text import MIMEText
from email.header import Header

email_host = "smtp.163.com"
send_user = "omgtest_haiyi"
send_user_pw = "omgtest789"
send_user_em = "omgtest_haiyi@163.com"

class SendEmail:
    def __init__(self):
        self.email_host = email_host  # 邮箱服务器
        self.send_user = send_user  # 发件人用户名
        self.send_user_pw = send_user_pw  # 发件人邮箱授权码，非登录密码
        self.send_user_em = send_user_em  # 发件人邮箱
        self.user_list = ["496527978@qq.com"]
        self.title = "报告"
        self.test_report = "D:\\www\poppy\\report"

    def send_email(self):
        file_new = self.get_new_report()
        f = open(file_new, 'rb')
        content = f.read()
        f.close()

        message = MIMEText(content, _subtype='html', _charset='utf-8')  # 内容，格式，编码
        message['From'] = "{}".format(self.send_user_em)  # 发件人
        message['To'] = ",".join(self.user_list)  # 收件人
        message['Subject'] = Header(self.title, 'utf-8')  # 标题

        try:
            server = smtplib.SMTP()
            server.connect(self.email_host)
            server.login(self.send_user, self.send_user_pw)  # 登录验证
            server.sendmail(self.send_user_em, self.user_list, message.as_string())  # 发送
            server.quit()  # 关闭
            print("邮件发送成功！")
        except smtplib.SMTPException as e:
            print("邮件发送失败！")
            print(e)

    def get_new_report(self):
        lists = os.listdir(self.test_report)
        lists.sort(key=lambda fn: os.path.getmtime(self.test_report + '\\' + fn))
        file_new = os.path.join(self.test_report, lists[-1])
        print(file_new)
        return file_new


if __name__ == "__main__":
    s = SendEmail()
    s.send_email()
