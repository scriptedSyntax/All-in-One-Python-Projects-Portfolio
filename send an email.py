import smtplib

##
sender = "ENTER YOUR EMAIL ADDRESS"         # use your gmail account
receiver = "ENTER RECEIVER ADDRESS"         # receiving email
password = "EMAIL PASSWORD"                 # gmail password
subject = "Python Email Test by Samuel Mwangi"
body = "This is a test email"


## Header MESSAGE
message = f"""From: {sender} 
To: {receiver}
Subject: {subject}\n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com", 587)     ## smtplib.SMTP(host, port_number)
server.starttls()

try:
    server.login(sender,password)
    print("Login Successful")
    server.sendmail(sender, receiver, message)
    print("Email Sent")

except smtplib.SMTPAuthenticationError:
    print("Unable to sign in :(")


## NOTES
## smtplib.SMTPAuthenticationError = username x pass combo not correct
## or you need to turn on "less secure app access" on your gmail account.