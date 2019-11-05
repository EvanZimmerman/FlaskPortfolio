from flask import Flask, render_template, url_for 
from flask_assets import Bundle, Environment

app = Flask(__name__)

bundles = {
  'layout_js': Bundle(
    'js/lib/jquery-3.4.1.min.js',
    'js/layout.js',
    output = 'gen/layout.js',
    filters = 'jsmin'
  ),
  'site_css': Bundle(
    'css/layout.css',
    'css/home.css',
    'css/contact.css',
    'css/resume.css',
    'css/skills.css',
    output = 'gen/site.css',
    filters = 'cssmin'
  )
  # 'layout_css': Bundle(
  #   'css/layout.css',
  #   output = 'gen/layout.css',
  #   filters = 'cssmin'
  # ),
  # 'home_css': Bundle(
  #   'css/home.css',
  #   output = 'gen/home.css',
  #   filters = 'cssmin'
  # ),
  # 'contact_css': Bundle(
  #   'css/contact.css',
  #   output = 'gen/contact.css',
  #   filters = 'cssmin'
  # )
}

assets = Environment(app)
assets.register(bundles)

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/skills')
def skills():
  return render_template('skills.html')

@app.route('/resume')
def resume():
  return render_template('resume.html')

@app.route('/contact')
def contact():
  return render_template('contact.html')

if __name__ == '__main__':
  app.run(debug = True)