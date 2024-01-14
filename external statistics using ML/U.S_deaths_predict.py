import pandas as pd # We are working with dataframes and csv files
from fbprophet import Prophet
import matplotlib.pyplot as plt

#Read in NYT dataset
df = pd.read_csv("https://raw.githubusercontent.com/nytimes/covid-19-data/master/us.csv")

#What will be the number of cases in the future?
df_deaths = df.groupby("date").sum()['deaths'].reset_index()
#print(df_cases.head())

#Renaming column names so Prophet can take the dataframe as input.
df_deaths.columns = ["ds", "y"]
#print(df_deaths.head())

#Instantiate a new Prophet object.
m = Prophet() 
m.fit(df_deaths)

#Create a space to store future dataframe (creating future dates)
future = m.make_future_dataframe(periods=365) #periods parameter is # of days
#print(future.tail())

# Forecasting label values (yhat)
forecast = m.predict(future)
(forecast[['ds','yhat', 'yhat_lower', 'yhat_upper']].tail())

fig1 = m.plot(forecast)
plt.show()