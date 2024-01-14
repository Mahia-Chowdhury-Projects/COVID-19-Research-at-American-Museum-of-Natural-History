import pandas as pd # we use the pandas library to read into OWID

def US_vaccinated_OWID_filter(df = False): #the function header 
    df = pd.read_csv("https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv") #reading into the data
    df_us = df.loc[df["location"]== "United States"] #using the .loc operator we created the df_us datafile which only contains data from the US 
    df_vaccinated = df_us.groupby('date', dropna= True).sum()["people_fully_vaccinated"].reset_index() #using the .groupby() method we made sure that there are no repeats in the data and dropped all of the NAN values and replaced them with 0 
    df_vaccinated.columns = ["ds", "y"] #this renames the colomuns -- "date" is now called "ds" and "people_fully_vaccinated" is now called "y"
    #this prepares the file for machine leanring where these labels are needed to make plots
    return df_vaccinated #returns the finished dataframe
   