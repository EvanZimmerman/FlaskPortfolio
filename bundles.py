from flask_assets import Environment, Bundle

class Bundles:
  def __init__(self, app):
    self.assets = Environment(app).register({
      'layout_js': Bundle (
        'js/lib/jquery-3.4.1.min.js',
        'js/layout.js',
        output = 'gen/layout.js',
        filters = 'jsmin'
      ),
      'site_css': Bundle (
        'css/layout.css',
        'css/home.css',
        'css/contact.css',
        'css/resume.css',
        'css/skills.css',
        output = 'gen/site.css',
        filters = 'cssmin'
      )
    })