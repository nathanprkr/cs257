from flask import Flask
from flask import render_template
import random

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template("index.html")

@app.route('/fortune')
def fortune_gen():

    lst = ["you will die", 'you will have a good day', 'you will have a bad day', 'you suck', 'never get another fortune again', 
           'your code will work first try', 'you will get a cat', 'you will get a dog', 'you are going to eat at burton', 'you will eat at LDC', 'you will name your child nathan']
    num = random.randint(0, 10)

    return render_template("fortune.html", fortune = lst[num])

if __name__ == '__main__':
    my_port = 5122
    app.run(host='0.0.0.0', port = my_port) 
