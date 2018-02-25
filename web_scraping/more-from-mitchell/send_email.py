# this differs from Mitchell's script - it uses Gmail instead of localhost 

import smtplib
from email.mime.text import MIMEText

msg = MIMEText("Howdy!\nLet's see how this works!")

msg['Subject'] = "An Email Alert"
msg['From'] = "name@mailplace.com"
msg['To'] = "someone@mailme.com"

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("name@mailplace.com", "somepassword")
s.send_message(msg)
s.quit()

# NOTE: create a new Gmail account, set up just for this purpose
# because you have to allow "less secure apps" to use it
