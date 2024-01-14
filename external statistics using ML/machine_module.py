import pandas as pd # We are working with dataframes and csv files
from fbprophet import Prophet
import matplotlib.pyplot as plt

#Read in NYT dataset
csv1 = pd.read_csv("https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv") #Any state and only cases 
csv2 = pd.read_csv("https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv")#Per day cases and positvity rates in the world 
csv3  = pd.read_csv("https://raw.githubusercontent.com/nytimes/covid-19-data/master/us.csv") #total cases and deaths U.S 

#What will be the number of cases in the future?
def plot(days):
    scope = input("Would you like to (A) view New York vs Texas cases, (B) View positivity rates in the United States (C) deaths in the U.S (D) cases per day in the U.S")
    if scope == "A": 
        df = csv1
        days = 91
    elif scope == "B":
        df = csv2 
        days = 274 
    elif scope == "C":
        df = csv3
        day = 265
    elif scope == "D":
        df = csv2
        days = 183
    else:
        print("Sorry this is not an option.")
    df_cases = df.groupby("date").sum()[info].reset_index()
    #print(df_cases.head())
    df_state = df_info.loc[df["state"]== state]
    df_info = df_state.loc[:, ["date", "cases"]]
    
    #df_cases = df_cases.loc[:, ["cases", "state" == df_cases["New York"]]
    #Renaming column names so Prophet can take the dataframe as input.
    df_info.columns = ["ds", "y"]
    print(df_cases.head())

    #Instantiate a new Prophet object.
    m = Prophet() 
    m.fit(df_info)

    #Create a space to store future dataframe (creating future dates)
    future = m.make_future_dataframe(periods= days) #periods parameter is # of days
    print(future.tail())

    # Forecasting label values (yhat)
    forecast = m.predict(future)
    print(forecast[['ds','yhat', 'yhat_lower', 'yhat_upper']].tail())


    fig1 = m.plot(forecast)
    plt.title("Number Of" + info + "in " + state)
    plt.show()

plot(days)