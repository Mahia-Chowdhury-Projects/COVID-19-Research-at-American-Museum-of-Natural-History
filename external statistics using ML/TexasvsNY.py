import pandas as pd # We are working with dataframes and csv files
from fbprophet import Prophet
import matplotlib.pyplot as plt

#Read in NYT dataset
df = pd.read_csv("https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv")

#What will be the number of cases in the future?
def state(state):
    df_cases = df.groupby("date").sum()['cases'].reset_index()
    #print(df_cases.head())
    df_state = df_cases.loc[df["state"]== state]
    df_cases = df_state.loc[:, ["date", "cases"]]
    
    #df_cases = df_cases.loc[:, ["cases", "state" == df_cases["New York"]]
    #Renaming column names so Prophet can take the dataframe as input.
    df_cases.columns = ["ds", "y"]
    print(df_cases.head())

    #Instantiate a new Prophet object.
    m = Prophet() 
    m.fit(df_cases)

    #Create a space to store future dataframe (creating future dates)
    future = m.make_future_dataframe(periods=365) #periods parameter is # of days
    print(future.tail())

    # Forecasting label values (yhat)
    forecast = m.predict(future)
    print(forecast[['ds','yhat', 'yhat_lower', 'yhat_upper']].tail())


    fig1 = m.plot(forecast)
    plt.title("Number Of Cases in " + state)
    plt.show()

state("New York") 
state("Texas")