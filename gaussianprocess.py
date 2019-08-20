import requests
import pandas as pd

# Forecasting years, number of years to use for out-of-sample 
num_years = 15
# number of lags to use for regression
lags = 5
# Indicator labels/names in World Bank API
indicators  = {"gdp"        : "NY.GDP.MKTP.CD",
               "population" :    "SP.POP.TOTL",
               "inflation"  : "FP.CPI.TOTL.ZG"}
num_indicators = len(indicators)
# target variable to forecast
target_variable = "gdp"
# Specified countries included in data using ISO country codes
countries  = ['au','ca','de','es','fr']
num_countries = len(countries)
# Start and end year for the data set
start_year = 2000
end_year   = 2015

template_url = "http://api.worldbank.org/v2/countries/{0}/indicators/{1}?date={2}:{3}&format=json&per_page=999"

# Countries indicated as ISO identifiers separated by semi-colons
country_str = ';'.join(countries)
raw_data = pd.DataFrame()
for label, indicator in indicators.items():
# fill in url with necessary data
    url = template_url.format(country_str, indicator, 
                                  start_year, end_year)
    
    # request data from WB url
    json_data = requests.get(url)
    
    # convert JSON string to python object
    json_data = json_data.json()
    
    # returns list where the first element is meta-data, and the second element is actual data
    json_data = json_data[1]
    
    # Loop over all data points, pick out the values and append them to the data frame
    for data_point in json_data:
        country = data_point['country']['id']
        # Create a variable for each country and indicator pair
        item    = country + '_' + label
        year    = data_point['date']  
        value   = data_point['value']
        
        # Append to data frame
        new_row  = pd.DataFrame([[item, year, value]],
                                columns=['item', 'year', 'value'])
        raw_data = raw_data.append(new_row)
# Pivot the data to get unique years along the columns,
# and variables along the rows
raw_data = raw_data.pivot('year', 'item', 'value')
# Let's look at the first few rows and columns
print('\n', raw_data.iloc[:10, :5], '\n')