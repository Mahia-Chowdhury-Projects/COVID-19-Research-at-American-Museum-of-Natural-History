from fbprophet import Prophet #We are working with dataframes and csv files
import pandas as pd # We use pandas libary to read into OWID
from  matplotlib import pyplot as plt #we use pyplot for stylistic purposes 
import numpy as np #some fbprophet uses in our code require np
import data_filter #our module that filters the data into dates (ds column) and fully vaccinated people (y colomun)
import API_module


def format_forecast(df):
    new = pd.DataFrame({"ds":df["ds"], "y":df["yhat"]})
    return new

def vaccination_rate_prediction(days, df): # Function that generates predictions for fully vaccinated people 
    df['cap'] = API_module.population 
    m = Prophet(growth='logistic')
    m.fit(df)
    future = m.make_future_dataframe(periods=days)
    future['cap'] = API_module.population 
    future['floor'] = min(df["y"])
    forecast = m.predict(future)
    fig = m.plot(forecast)
    plt.title("Fully Vaccinated People in " + str(days) + " days")
    plt.xlabel("Date")
    plt.ylabel("Vaccinated People")
    plt.show()
    return format_forecast(forecast)


# vaccination_rate_prediction(7)
# vaccination_rate_prediction(30)
# vaccination_rate_prediction(90)
# vaccination_rate_prediction(90 *3)



