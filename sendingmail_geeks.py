import smtplib

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
s.login("vivekbnagare31@gmail.com", "ksjt vgli pbrm xqna")#first on 2 step verification and generate app password this password is used to sent mails using third party apps.this feature has came after the google disanled the less security app option

# message to be sent
message = "code from python"

# sending the mail
s.sendmail("vivekbnagare31@gmail.com", "bharatn3161@gmail.com", message)

# terminating the session
s.quit()
