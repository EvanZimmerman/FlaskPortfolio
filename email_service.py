from flask_sendgrid import SendGrid

class EmailService:
  def __init__(self, app):
    self.app = app

  def send_message(self, name, email, message):
    subject = f'New Message from {name} - Porfolio Website'
    msg = f'Name: {name}\n\nEmail: {email}\n\n{message}'

    # send email via sendgrid
    mail = SendGrid(self.app)
    mail.send_email(to_email=self.app.config['EMAIL_TO_ADDR'],
                         subject=subject,
                         from_email='evanzimm.portfolio@gmail.com', text=msg) 