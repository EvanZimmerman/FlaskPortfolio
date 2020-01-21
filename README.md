# Portfolio Website - Flask

I wanted to create a portfolio website to outline the skills that I have obtained from both my professional and personal (self-taught) career.  After finishing a Python Flask tutorial on Udemy, I wanted to practice my new skillset by developing a simple, static portfolio website.  I was yearning to create this site for quite a long time, but wanted to find a very simple framework to have minimal backend development and found Flask to fit my use case perfectly!

Live website: https://evanzimm.com/

## Dependencies

The following is a list of some packages used for this website:

* `CSSMin` --  minify css files
* `Flask-Assets` -- bundling static files (css/js)
* `Flask-Limiter` -- limit the amount of times a user can submit the contact form
* `Flask-SendGrid` -- SendGrid API for sending the contact information to my email
* `Flask-Toastr` -- flash message after submitting contact information
* `Flask-WTF` -- flask specific package for WTForms
* `JSMin` -- minify js files

## Development Instructions

### Install and activate virtualenv

It is recommended to install a virtual environment before installing all dependencies needed to run this application in order to not clutter your locally installed python instance / libraries.  To do so, ensure you have python and pip installed and run the following command:

`pip install virtualenv`

After the installation is complete, activate the virtual environment by running the following command:

`python -m venv env`

A directory should be created in the project directory named `env`.  Activate the virtual env by running the following command:

Windows: `./env/Scripts/activate`
Unix-Based OS: `source env/lib/activate`

### Install project dependencies

Once your virtual environment is activated install the project dependencies by running the following command:

`pip install -r requirements.txt`

### Running the application

Once all dependencies are installed in your virtual environment, run the following command to start the development server and visit http://127.0.0.1/. The app will automatically reload if you change any of the source files.

`python app.py`