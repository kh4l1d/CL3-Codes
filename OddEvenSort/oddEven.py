from flask import Flask
from flask import request
from flask import render_template
import concurrentOddEven
app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def my_form_post():

    text = request.form["elements"]
    a = map(int, text.split(','))

    concurrentOddEven.oddevensort(a)

    return render_template("index.html" , a=a)

if __name__ == '__main__':
    app.run()
