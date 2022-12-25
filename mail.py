import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import openpyxl

sponsorEmail = []
sponsorFile = '< NAME OF THE EXCEL SHEET WITH EMAIL ADDRESSES >'
workbookObj = openpyxl.load_workbook(sponsorFile)
sheetObj = workbookObj.active
for row in sheetObj.iter_rows():
    sponsorEmail.append(row[1].value)
del sponsorEmail[0]

senderEmail = '<  FYI KI EMAIL ID>'
senderPass = '< FYI KI EMAIL KA PASSWORD>'

message = MIMEMultipart('alternative')
message['Subject'] = "< EK SEXY SA SUBJECT JISSE DEKH KE PRE MOTURE MONEY NIKAL JAAYE >"
message['From'] = senderEmail

messageHTML = open("content.html", "r").read()
HTMLpart = MIMEText(messageHTML, 'html')
message.attach(HTMLpart)

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login(senderEmail, senderPass)
for emailId in sponsorEmail:
    s.sendmail(senderEmail, emailId, message.as_string())
s.quit()
