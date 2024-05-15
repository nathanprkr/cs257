from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def welcome():
    message = message + "Welcome to the random number and color generator!"
    return render_template("homepage.html", someText = message)

if __name__ == '__main__':
    my_port = 5122
    app.run(host='0.0.0.0', port = my_port) 
