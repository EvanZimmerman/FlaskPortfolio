import smtplib
from email.message import EmailMessage

class EmailService:
  def __init__(self, app):
    self.app = app

  def send_message(self, name, email, message):
    subject = f'Porfolio Website - New Message from {name}'
    msg = f'Subject: {subject}\n\nName: {name}\nEmail: {email}\n\n{message}'
    to = [self.app.config['EMAIL_TO_ADDR']]

    # create server and send contents
    server = smtplib.SMTP(self.app.config['SMTP_ADDR'])
    server.ehlo()
    server.starttls()
    server.login(self.app.config['GMAIL_FROM_USER'], self.app.config['GMAIL_FROM_PASS'])
    server.sendmail(self.app.config['GMAIL_FROM_USER'], to, msg)
    server.quit()