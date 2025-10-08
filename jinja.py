from flask import Flask, render_template, request

app=Flask(__name__)

## Variable Rule
@app.route('/success/<int:score>')
def success(score):
    return "your followers are " + str(score)

##Builing Dynamic URLs
@app.route('/influencer/<int:count>')
def influencer(count):
    res=""
    if count>=10000:
        res="Passed"
    else:
        res="Not Passed"

    return render_template('result.html', results=res)



if __name__=="__main__":
    app.run(debug=True)


