from flask import Flask, render_template #render template is to redirecting to particular html page


app=Flask(__name__)

@app.route("/")
def welcome():
    return "<html><h1>Hello welcome to this page<h1></html>"

@app.route("/index")
def index():
    return render_template('index.html')



if __name__=="__main__":
    app.run(debug=True)



