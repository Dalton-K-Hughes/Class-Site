from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/intro-business')
def intro_business():
    pass

@app.route('/foundations-interactive')
def foundations_interactive():
    pass

@app.route('/foundations-investing')
def foundations_investing():
    pass

@app.route('intro-software')
def intro_software():
    pass

@app.route('web-design')
def web_design():
    pass

