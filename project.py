from flask import  Flask, render_template, flash, redirect, url_for, request
from forms import DataInput
app = Flask(__name__)

app.config['SECRET_KEY'] = '1234567890'

@app.route("/", methods=['GET', 'POST'])
def home():
    form = DataInput()
    price = request.form.get('value')
    if type(price) == int and price > 0:
        tax = LBTT_calculator(price)
        print(tax)
        return render_template('output.html', tax=tax)
    else:
        msg = 'Wrong input type try again please'
        return render_template('home.html', msg=msg)

    return render_template('home.html', form=form)

    country = {
        'scotland' :{
            'threshold' : [0, 250000, 325000, 750000],
            'rates' : [0,0.1, 0.5, 1]
        },
        {
            'england' .... 
        }
    }

def LBTT_calculator(price):
    first = 75000 * 0.05
    second = 425000 * 0.1 
    if price < 250000:
        tax = 0
    elif price > 250000 and price < 325000:
        price = price -250000
        tax = (price * 0.05)
    elif price > 325000 and price < 750000:
        price = price - 325000
        tax = (price * 0.1) + first
    else:
        price = price - 750000
        tax = (price * 0.12) + first + second
    return tax



         