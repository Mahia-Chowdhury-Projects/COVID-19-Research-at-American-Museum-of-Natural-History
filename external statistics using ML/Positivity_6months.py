import pandas as pd # We are working with dataframes and csv files
from fbprophet import Prophet
import matplotlib.pyplot as plt

#Read in NYT dataset
df = pd.read_csv("https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv")

#What will be the number of cases in the future?
df_positivity = df.groupby("date").sum()['positive_rate'].reset_index()
#print(df_cases.head())

#Renaming column names so Prophet can take the dataframe as input.
df_positivity.columns = ["ds", "y"]
#print(df_deaths.head())

#Instantiate a new Prophet object.
m = Prophet() 
m.fit(df_positivity)

#Create a space to store future dataframe (creating future dates)
future = m.make_future_dataframe(periods=365) #periods parameter is # of days
#print(future.tail())

# Forecasting label values (yhat)
forecast = m.predict(future)
(forecast[['ds','yhat', 'yhat_lower', 'yhat_upper']].tail())

fig1 = m.plot(forecast)
plt.show()