import pandas as pd
import graphs


def read_data(filename):
    df = pd.read_csv(filename, skiprows=4)
    
    # transpose
    df_year = df.set_index('Country Name').T
    # clean up column headers
    df_year.columns.name = ''
    # transpose
    df_country = df_year.T
    df_country.columns.name = 'Country Name'
    # clean up
    df_year.fillna('', inplace=True)
    df_country.fillna('', inplace=True)
    # return
    return df_country, df_year

df_country, df_year = read_data('world_bank_climate.csv')

# print data
print(df_country,df_year)


# Read
df = pd.read_csv('world_bank_climate.csv', skiprows=4)
# clean
df.fillna('', inplace=True)

# Countries of interest
countries_array = ['China','Ecuador','France','India','Nigeria','South Africa','Romania','Switzerland','United Kingdom','United States']


# Indicators of interest
indicators_array = ['Energy use (kg of oil equivalent per capita)', 'Renewable energy consumption (% of total final energy consumption)','Agricultural land (% of land area)','Access to electricity (% of population)', 'Forest area (% of land area)', 'CO2 emissions from liquid fuel consumption (% of total)']


# Subset the data
df_sub = df[(df['Country Name'].isin(countries_array)) & (df['Indicator Name'].isin(indicators_array))]

# Calculate statistics with describe
stats = df_sub.groupby(['Country Name', 'Indicator Name']).describe()

# Print the statistics
print(stats)

# get years from column
year = [col for col in df_sub.columns if col.isdigit()]

# graphs
graphs.bar_graph(df_sub, year, 'Energy use (kg of oil equivalent per capita)', 'Country Name', '')
graphs.bar_graph(df_sub, year, 'CO2 emissions from liquid fuel consumption (% of total)', 'Country Name', '')
graphs.heatmap(df_sub, 'China', indicators_array,'BrBG')
graphs.heatmap(df_sub, 'France', indicators_array,'crest')
graphs.heatmap(df_sub, 'India', indicators_array,'YlGnBu')
