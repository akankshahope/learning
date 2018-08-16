def send_email(user, pwd, recipient, subject, body):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    FROM = user
    TO = recipient if isinstance(recipient, list) else [recipient]
    SUBJECT = subject
    HTML_MSG = body

    msg = MIMEMultipart('alternative')
    msg['Subject'] = SUBJECT
    msg['From'] = FROM
    msg['To'] =  ", ".join(TO)
    part1 = MIMEText(HTML_MSG, 'html')
    msg.attach(part1)

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(user, pwd)
        server.sendmail(FROM, TO, msg.as_string())
        server.close()
        print 'successfully sent the mail'
    except:
        print "failed to send mail"

body = '''<h1>Hello Test,</h1><br/><i>Thanks</i>'''
send_email('<emailId>', 'PassWord', ['<emailId_1>', '<emailId_2>'], '<subject>', body)
