import os
from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL
from email.mime.multipart import MIMEMultipart
from config.readconfig import ReadConfig
from datetime import datetime


# 将ReadConfig类的get_email_config方法赋值给变量read_config
read_config = ReadConfig().get_email_config


def send_report(file):
    '''发送测试报告'''
    with open(file, "rb") as f:
        mail_body = f.read()

    host_server = read_config("mail_host")
    user = read_config("mail_user")
    pwd = read_config("mail_pass")
    reciever = read_config("receiver")
    sender = read_config("sender")

    mail_title = read_config("subject")

    msg = MIMEMultipart()
    msg["Subject"] = Header(mail_title, "utf-8")
    msg["From"] = sender

    msg.attach(MIMEText(mail_body, "html", "utf-8"))

    smtp = SMTP_SSL(host_server)
    smtp.ehlo(host_server)
    smtp.login(user, pwd)

    smtp.sendmail(sender, reciever, msg.as_string())

    smtp.quit()
    print("result has send out")

def get_new_report(test_report_dir):
    '''获取最新的测试报告'''
    test_report_list = os.listdir(test_report_dir)
    new_report_list = sorted(test_report_list)
    new_report_filename = os.path.join(test_report_dir, new_report_list[-1])
    print(new_report_filename)
    return new_report_filename

if __name__ == "__main__":
    test_report_dir = "D:\\profile\\AutoTestFrame\\testreport"
    new_report = get_new_report(test_report_dir)
    send_report(new_report)