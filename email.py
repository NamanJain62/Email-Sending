import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "mynjnaman008@gmail.com"  # Enter your address
receiver_email = "njnaman008@gmail.com"  # Enter receiver address
password = input("Type your password and press enter: ")
Subject="Hello"
text = """\Subject: Hi there

This message is sent from Naman."""
text+="\n"
text+="CGPA=8.5"

message = 'Subject: {}\n\n{}'.format(Subject,text)

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
