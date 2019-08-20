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