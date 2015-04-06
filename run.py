from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def index():
    print request
    return 'Hi, flask!'


app.run(host = '0.0.0.0', debug = True)
