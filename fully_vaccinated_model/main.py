import data_filter
import model
import give_answer_module

user_days = int(input("How many days into the future?: "))
df_vaccinated = data_filter.US_vaccinated_OWID_filter()
prediction = model.vaccination_rate_prediction(user_days,df_vaccinated)
date = give_answer_module.answer(prediction)
print("Covid restrictions are expected to lift on", date)