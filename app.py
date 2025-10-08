from flask import Flask

app=Flask(__name__)  # initialize flask app, __name__ is parameter

@app.route("/")  #by default it is a GET method
def welcome():
    return "Welcome to this flask app I want to lave all of this behind and i will fking leave thisss. i willlllll"

@app.route("/index")  #by default it is a GET method
def index():
    return "willlllll"



if __name__ =="__main__":  #entry of the application
    app.run(debug=True) # we dont have to restart the server by debug true.
