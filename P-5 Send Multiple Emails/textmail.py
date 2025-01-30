import smtplib as s

ob = s.SMTP('smpt.gmail.com',587) # in this we give inside the server name and the port number
ob.ehlo() #server function
ob.starttls() #server connected

