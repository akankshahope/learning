def send_email(user, pwd, recipient, subject, body):
    import smtplib
    import sys
    
    gmail_user = user
    gmail_pwd = pwd
    
    FROM = user
    TO = recipient if type(recipient) is list else [recipient]
    SUBJECT = subject
    TEXT = body

    FROMNAME = 'SenderNameHere <senderEmailIDHere>'
    
    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\nreply-to: %s\n\n%s
    """ % (FROMNAME, ", ".join(TO), SUBJECT, FROM, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        try:
            server.login(gmail_user, gmail_pwd)
        except:
            e = sys.exc_info()[0]
            print e
        server.sendmail(FROM, TO, message)
        server.close()
        print 'successfully sent the mail'
    except:
        e = sys.exc_info()[0]
        print e
        print "failed to send mail"
    # # SMTP_SSL Example
    # server_ssl = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    # server_ssl.ehlo() # optional, called by login()
    # server_ssl.login(gmail_user, gmail_pwd)  
    # # ssl server doesn't support or need tls, so don't call server_ssl.starttls() 
    # server_ssl.sendmail(FROM, TO, message)
    # #server_ssl.quit()
    # server_ssl.close()
    # print 'successfully sent the mail'


user = 'YOUREMAILIDHERE' 
pwd = 'YOURPASSWORDHERE'
send_email(user,pwd,['EMAILID1','EMAILID2'],'SUBJECT LINE','BODY OF THE EMAIL')
