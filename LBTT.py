country = {
        'scotland': {
    'threshold' : [0, 250000, 325000, 750000],
    'rate' :[0, 0.05, 0.1, 0.12]
    }, 
    'england': {
        'threshold': [0, 1000000, 250000, 750000],
        'rate' : [0, 0.05, 0.1, 0.12]
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
