
# real life use an actual database not in code. 
# Store JSON in database, of country specific rules that may be needed. JSON allows flexibility that SQL columns may not.

# tax_details - used for calculation on backend
# input_details - request so frontend knows which additional details are needed for the country selected.

# On the Front End 
# Request database['england']['input_details'] for what additional fields are needed for this location 

database = {
    'scotland': {    
        'tax_details': {
                'thresholds': [100000, 200000, 300000],
                'rates': [0.1, 0.2, 0.3]
        },
        'input_details': ['First Time Buyer']
    },
    'england': {
        'tax_details': {
            'thresholds': [100000, 200000, 300000],
            'rates': [0.1, 0.2, 0.3],
            'covid_rate': 0.1               
        },
        'input_details': ['Residential', 'In London']
    } 
}

# Define Generic Country Class which others will extend. 

class Country():
    
    def __init__(self, country):
        super().__init__()
        self.get_details(country)

    def get_details(self, country):
        self.details = database[country]['tax_details']     # Query database for tax details

class Scotland(Country):

    def __init__(self):
        super().__init__('scotland')

    def calculate(self, price, first_time_buyer=False):
        # calculation formula for this country
        return price * len(self.details['thresholds']) * self.details['rates'][0]

class England(Country):

    def __init__(self):
        super().__init__('england')

    def calculate(self, price, residential=True, in_london=False):
        # calculation formula for this country
        if (in_london):
            return max(price * self.details['rates'][1], 100000)
        else:
            return price * 0.01

# Store a mapping from country to Calculations
tax_mapping = {
    'england': England(),
    'scotland': Scotland()
}


# .... define specific code for other countries


# Example of Request object, where three fields are passed (common and details which contains country specific).

# http calls.
request_data_one = {
    'location': 'england',          # Common Field
    'price': 2e07,                  # Common Field
    'details': {                    # Country Specific Details
        'in_london': False,
    }
}

# Pass kwargs in a generic way for details. 
result = tax_mapping[request_data_one['location']].calculate(request_data_one['price'], **request_data_one['details'])
print(result)


# Another example. 
request_data_two = {
    'location': 'england',
    'price': 2e07,
    'details': {                    # Country Specific Details
        'in_london': True,
    }
}

result = tax_mapping[request_data_two['location']].calculate(request_data_two['price'], **request_data_two['details'])
print(result)

# Another example. 
request_data_two = {
    'location': 'england',
    'price': 2e07,
    'details': {                    # Country Specific Details
        'in_london': True,
    }
}

result = tax_mapping[request_data_two['location']].calculate(request_data_two['price'], **request_data_two['details'])
print(result)

