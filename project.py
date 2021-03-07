from flask import  Flask, render_template, flash, redirect, url_for, request
app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():

    return render_template('home.html')


if __name__ =='__main__':
    app.run(debug=True)