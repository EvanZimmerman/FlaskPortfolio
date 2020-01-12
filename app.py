# flask imports
from flask import Flask, render_template, url_for, redirect, flash
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_toastr import Toastr

# site imports
from forms import ContactForm
from bundles import Bundles
from email_service import EmailService

# initialize application and import config file
app = Flask(__name__)
app.config.from_object('config')

# initialize flask_toastr
toastr = Toastr(app)

# initialize limiter
limiter = Limiter(app,key_func=get_remote_address)

# initialize email service
email_service = EmailService(app)

# Bundle static resources
bundles = Bundles(app)

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/skills')
def skills():
  return render_template('skills.html')

@app.route('/resume')
def resume():
  return render_template('resume.html')

@app.route('/contact', methods=['GET', 'POST'])
@limiter.limit(app.config['DEFAULT_LIMIT'])
def contact():
  form = ContactForm()
  if form.validate_on_submit():
    # parse data from form and set up email details
    name = form.name.data
    email = form.email.data
    message = form.message.data

    # send email
    try:
      email_service.send_message(name=name, email=email, message=message)
      flash('Your message was sent successfully.  Thank you for your interest and I will send you a response as soon as possible!', 'success')
      return redirect(url_for('contact'))
    except:
      flash('Something went wrong sending your email, please try again later.', 'error')
      return redirect(url_for('contact'))

  return render_template('contact.html', form=form)

@app.errorhandler(404)
def error_404(error):
  return render_template('404.html')

if __name__ == '__main__':
  app.run()