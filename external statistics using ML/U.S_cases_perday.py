import pandas as pd # We are working with dataframes and csv files
from fbprophet import Prophet
import matplotlib.pyplot as plt

#Read in NYT dataset
df = pd.read_csv("https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv")

#What will be the number of cases in the future?
df_cases = df.groupby("date").sum()['new_cases'].reset_index()
#print(df_cases.head())

#Renaming column names so Prophet can take the dataframe as input.
df_cases.columns = ["ds", "y"]
#print(df_deaths.head())

#Instantiate a new Prophet object.
m = Prophet() 
m.fit(df_cases)

#Create a space to store future dataframe (creating future dates)
future = m.make_future_dataframe(periods=274) #periods parameter is # of days
#print(future.tail())

# Forecasting label values (yhat)
forecast = m.predict(future)
(forecast[['ds','yhat', 'yhat_lower', 'yhat_upper']].tail())

fig1 = m.plot(forecast)
plt.show()