from flask import  Flask, render_template, flash, redirect, url_for, request
from forms import DataInput
app = Flask(__name__)

app.config['SECRET_KEY'] = '1234567890'

@app.route("/", methods=['GET', 'POST'])
def home():
    form = DataInput()
    if form.validate_on_submit():
        price = form.house_price.data
        tax = LBTT_calculator(price)
        print(tax)
        return render_template('output.html', tax=tax)

    return render_template('home.html', form=form)

def test(price):
    
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


country = {
        'scotland': {
    'threshold' : [0, 250000, 325000, 750000],
    'rate' :[0, 0.05, 0.1, 0.12]
    }}

def LBTT_calculator(price):
    thres = country.get('scotland').get('threshold')
    rate = country.get('scotland').get('rate')
    first = (thres[2] - thres[1]) * rate[1]
    second = (thres[3] - thres[2]) * rate[2]
    if price < thres[0]:
        tax = 0
    elif price > thres[0] and price < thres[1]:
        price = price - thres[0]
        tax = (price * rate[1])
    elif price > thres[1] and price < thres[2]:
        tax = (price * rate[2]) + first
    else:
        price = price - 750000
        tax = (price * rate[3]) + first + second
    return tax

         