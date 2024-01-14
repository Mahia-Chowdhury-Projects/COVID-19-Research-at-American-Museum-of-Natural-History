# The purpose of this script is to map the global positivity rates from February 2020 to the present. There is an animated feature so that users can view the dates across different periods in time. It reads in the data from owid covid data and isolates the columns "positive_rate", "location", and "date" and filters out unwanted data. Then, we use the .choropleth() function from plotly express to display the data with animation.
import pandas as pd
import plotly.express as px
import numpy as np 

def datafilter():
    df = pd.read_csv("https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv")
    df["positive_rate"] = df["positive_rate"]*100
    newdf = df.loc[:, ["positive_rate", "location", "date"]].copy()
    
    newdf["positive_rate"][0] = 0
    for n , i in enumerate(newdf["positive_rate"]):
        if n == 0: 
           continue
        if newdf["location"][n-1] != newdf["location"][n] and np.isnan(i):
            newdf["positive_rate"][n] = 0

    newdf["positive_rate"].fillna(method = "ffill")
    return newdf

def animatedChoroplethmap():
    our_df = datafilter()
    print("NOTE: Recent data may not be available")
    colors = px.colors.sequential.Jet
    fig = px.choropleth(our_df,
    locationmode= "country names",
    locations = our_df["location"],
    color = "positive_rate", # sets the color values based on the date
    color_continuous_scale = colors, # sets the colorscale based on array of HEX values
    hover_name = our_df["location"],  
    animation_frame = our_df["date"],
    title = "Global Covid-19 Positivity Rates (millions)"
    )
    fig.update_layout(
        geo = dict(
        showcoastlines = True, coastlinecolor = "blue",
        ))
    fig.write_html("positivityrate.html", auto_open = True)    
