from flask import Flask, flash, redirect, render_template, request, session, abort

app = Flask(__name__)

@app.route("/")
def index():
    return "Index!"

@app.route("/name/<string:name>/")
def getName(name):
    return name

@app.route("/hello/<string:name>/")
def hello(name):
    return render_template('index.html', name=name)


if __name__ == "__main__":
    app.run("0.0.0.0",debug=False)