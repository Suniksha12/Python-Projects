# import smtplib as s

# ob = s.SMTP('smtp.gmail.com',587) # in this we give inside the server name and the port number
# ob.ehlo() #server function
# ob.starttls() #server connected

# ob.login('suni71561@gmail.com','sunikSha17@')

# #now we want to create the subject
# subject = "TEST"
# body = "I am a Student."
# message = "subject:{}\n\n{}".format(subject,body)
# listadd=['sunikshabenpatel@gmail.com',
#          'suniksha814@gmail.com']

# ob.sendmail('sunikshabenpatel@gmail.com',listadd,message)
# print("Email sent successfully")
# ob.quit()

import smtplib
from email.mime.text import MIMEText

# Email credentials
sender_email = "suni71561@gmail.com"
receiver_email = "sahimkhan637@gmail.com"
app_password = "hsen wqtr qnwl imdx"  # Use App Password instead of your Gmail password

# Email content
msg = MIMEText("Hello! This is a test email from Python.")
msg["Subject"] = "Test Email"
msg["From"] = sender_email
msg["To"] = receiver_email

# Connect to Gmail SMTP server
try:
    ob = smtplib.SMTP('smtp.gmail.com', 587)
    ob.starttls()  # Secure connection
    ob.login(sender_email, app_password)  # Use App Password
    ob.sendmail(sender_email, receiver_email, msg.as_string())
    print("✅ Email sent successfully!")
    ob.quit()
except Exception as e:
    print(f"❌ Error: {e}")
