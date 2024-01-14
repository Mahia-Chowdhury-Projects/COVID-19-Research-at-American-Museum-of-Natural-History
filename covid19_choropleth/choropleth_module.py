import numpy as np # used to arrange x-axis values for bar plot
import matplotlib.pyplot as plt #to make a visualization
import pandas as pd #to read in csv files and create dataframes
import plotly.graph_objects as go # to create a colorful map visualization 
from matplotlib.dates import DateFormatter #to use matplotlib's date formatter
# %matplotlib inline 
# ^ sets the backend of matplotlib to the 'inline' backend
# With this backend, the output of plotting commands is displayed inline within frontends like 
# the Jupyter notebook, directly below the code cell that produced it.
print("HI")
nyt_df = pd.read_csv("https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv")

statesList = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado",
   "Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois",
   "Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
   "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",
   "Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York",
   "North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
   "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah",
   "Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming", "American Samoa"]

 #List of state abbreviations sorted in alphabetical order. s
stateAbbreviationList = ["AL","AK","AS","AZ","AR","CA","CO","CT","DE","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND",
 "OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY"]

 #Corresponding latitudes for each state.
latitudes = [32.361538, 58.301935,14.2710, 33.448457, 34.736009, 38.555605, 39.7391667, 41.767, 39.161921, 30.4518, 33.76,
             21.30895, 43.613739, 39.783250, 39.790942, 41.590939, 39.04, 38.197274, 30.45809, 44.323535, 38.972945,
             42.2352, 42.7335, 44.95,32.320, 38.572954,46.595805,40.809868,39.160949,43.220093, 40.221741,35.667231,
             42.659829,35.771, 48.813343,39.962245, 35.482309,44.931109, 40.269789, 41.82355, 34.000,  44.367966,36.165,
             30.266667,40.7547,44.26639, 37.54, 47.042418,38.349497,43.074722, 41.145548]

 #Corresponding longitudes for each state.
longitudes = [-86.279118,-134.419740,170.1322,-112.073844, -92.331122,-121.468926 ,-104.984167 ,-72.677 , -75.526755 ,
               -84.27277,-84.39,-157.826182 ,-116.237651 ,-89.650373 ,-86.147685 ,-93.620866 ,-95.69 , -84.86311
               ,-91.140229 ,-69.765261 ,-76.501157 ,-71.0275 ,-84.5467 , -93.094 ,-90.207 , -92.189283
               , -112.027031 ,-96.675345 ,-119.753877 ,-71.549127 , -74.756138, -105.964575 , -73.781339 ,-78.638 
               ,-100.779004 ,-83.000647 , -97.534994,-123.029159 ,-76.875613 , -71.422132, -81.035, -100.336378
               ,-86.784 ,-97.75 ,-111.892622 ,-72.57194 ,-77.46 ,-122.893077 ,-81.633294 ,-89.384444 ,-104.802042]


#Dataframe Formatter
def dfFormatter(df, selectColumn):
     #Separate df_formatted from df. Create list of states and their latitudes and longitudes.
     df_formatted = pd.DataFrame(statesList, columns = ['state'])
     df_formatted['lat'] = latitudes
     df_formatted['long'] = longitudes

     #Create columns for each date, start off by zeroing out everything.
     #previousDate = datetime.datetime(2020, 1, 1) #Commented out because datetime is no longer a type.
     previousDate = "2020-01-01"
     for i in range(len(df['date'])):
         if df['date'][i] != previousDate:
             df_formatted[df['date'][i]] = 0

     #Set index to states temporarily.
     df_formatted.set_index('state', inplace=True)


     #Select which data you want to use based on the column that you are plotting (cases or deaths)
     if selectColumn == 'cases':
         #Get number of cases from df and put them in df_formatted.  
         for i in range(len(df['state'])):
             df_formatted.loc[df['state'][i], df['date'][i]] = df['cases'][i]
             #Format for .loc : df_formatted.loc['index/row label', 'column label'] = 'value'
     elif selectColumn == 'deaths':
         for i in range(len(df['state'])):
             df_formatted.loc[df['state'][i], df['date'][i]] = df['deaths'][i]
             #Format for .loc : df_formatted.loc['index/row label', 'column label'] = 'value'


     #Reset index when done so that state becomes a column without being the index.
     df_formatted.reset_index(inplace=True)

     #Drop last 5 rows because we are focusing on the 50 states.
     df_formatted.drop([50,51,52,53,54], inplace=True)

     return df_formatted

#Call the function and assign what it returns to the dataframe variables you will be using.
cases = dfFormatter(nyt_df, "cases")
cases["State abbreviations"] = stateAbbreviationList
deaths = dfFormatter(nyt_df, "deaths")
deaths["State abbreviations"] = stateAbbreviationList

def death_map(date): # defines function
   colors =['#f7fbff','#deebf7','#c6dbef','#9ecae1','#6baed6','#4292c6','#2171b5','#08519c','#08306b'] #Hex values
   fig = go.Figure(data = go.Choropleth( # creates a figure and assigns it to a function that creates a choropleth map
                     locationmode= "USA-states", # determines the set of locations used to match entries in "locations" parameter
                     locations = deaths["State abbreviations"], # sets the coordinates via location names(abbreviations)
                     z = deaths[date], # sets the color values based on the date
                     colorscale = colors, # sets the colorscale based on array of HEX values
                     reversescale = False, # reverses the color mapping if True
                     autocolorscale = False, # reads our color scale
                     colorbar_title = "Number of COVID-19 deaths (US)" # displays title of colorbar 
     ))

   fig.update_layout(
         title_text = "Number of COVID-19 deaths (US)", # displays title of map 
         geo = dict(
             showcoastlines = True, # displays coastlines in map
             scope = "usa" # sets scope of map to the USA
         )
     )
   fig.write_html("deathsperstate.html", auto_open = True)

def caseFatalityrate_map(date):
     colors = ['#f7fcf5','#e5f5e0','#c7e9c0','#a1d99b','#74c476','#41ab5d','#238b45','#006d2c','#00441b']
     case_fatalityRate = deaths[date]/cases[date]
     fat_fig = go.Figure(data = go.Choropleth(
                     locationmode= "USA-states",
                     locations = deaths["State abbreviations"],
                     z = (case_fatalityRate * 100),
                     colorscale = colors,
                     reversescale = False,
                     autocolorscale = False, #reads our color scale
                     colorbar_title = "COVID-19 Case Fatality rates (percent)"
     ))

     fat_fig.update_layout(
         title_text = "COVID-19 Case Fatality rates (US)",
         geo = dict(
             showcoastlines = True,
             scope = "usa"
         )
     )
     fat_fig.write_html("casefatrate.html", auto_open = True)