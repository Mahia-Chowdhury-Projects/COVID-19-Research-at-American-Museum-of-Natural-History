import choropleth_module

decision = str(input("Type \'A\' to view a map of COVID-19 case fatality rates or \'B\' to view a map of COVID-19 deaths. "))
if decision is "A":
  user_caseFat_date = str(input("Which date would you like to view COVID-19 case fatality rates of (YYYY-MM-DD, the latest date is 2023-03-23)? "))
  choropleth_module.caseFatalityrate_map(user_caseFat_date)
elif decision is "B":
  user_date = str(input("Which date would you like to see COVID-19 deaths for (YYYY-MM-DD, the latest date is 2023-03-23)? "))
  choropleth_module.death_map(user_date)
