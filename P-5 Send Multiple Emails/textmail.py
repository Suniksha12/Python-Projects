import smtplib as s

ob = s.SMTP('smpt.gmail.com',587) # in this we give inside the server name and the port number
ob.ehlo() #server function
ob.starttls() #server connected

ob.login('suni71561@gmail.com','sunikSha17@')

#now we want to create the subject
subject = "TEST"
body = "I am a Student."
message = "subject:{}\n\n{}".format(subject,body)
listadd=['sunikshabenpatel@gmail.com',
         'suniksha814@gmail.com']