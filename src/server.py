from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
    
@app.route("/version")
def version():
    return "Running version: 1.0.55"
    
@app.route("/hello")
def test():
    return "Hi you!"
