import smtplib
from email.mime.text import MIMEText

msg = MIMEText("AlertManager 邮件测试")
msg['Subject'] = "测试告警邮件"
msg['From'] = "hyxt2014@163.com"
msg['To'] = "13537898500@139.com"

try:
    s = smtplib.SMTP("smtp.163.com", 25, timeout=10)
    s.login("hyxt2014@163.com", "huayangxintong")
    s.sendmail("hyxt2014@163.com", ["13537898500@139.com"], msg.as_string())
    s.quit()
    print("发送成功")
except Exception as e:
    print(f"发送失败: {e}")
