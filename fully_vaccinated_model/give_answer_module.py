import numpy as np
import API_module

# function three
def answer(df):                                     # take prediction
    minGoal = API_module.population *0.7            # 70% of population is realistic goal (fully vaccinated)
    maxGoal = API_module.population *0.9            # 90% -> unreliastic goal (at the moment)
    minIndex = ''                                   # empty placeholders: 
    dates = (df["ds"].loc[df["y"] >= minGoal]).reset_index(drop = True)                        # finds y value instance whe   # returns answer
    return dates[0]