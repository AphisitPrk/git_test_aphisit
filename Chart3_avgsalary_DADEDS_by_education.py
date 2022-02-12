import pandas as pd
import matplotlib.pyplot as plt
from pandas.core import accessor
import seaborn as sns
data = pd.read_excel(r"C:\Users\APHISIT\OneDrive\Desktop\เอกสาร Msyne\งานเดี่ยว\PYTHON\example_data_training_Mspire.xlsx")
data_clean = data.drop(['first_name' , 'last_name' , 'zip' , 'phone' , 'email' ,'address'] , axis=1) 

avg_salary_by_title_DA = data[data["Position"]== 'Data Analyst'].sort_values(by=['salary'] ,ascending=False)
groupby_DA = avg_salary_by_title_DA.groupby('Education').mean()['salary'].reset_index()
avg_salary_by_title_DE = data[data["Position"]== 'Data Engineer'].sort_values(by=['salary'] ,ascending=False)
groupby_DE = avg_salary_by_title_DE.groupby('Education').mean()['salary'].reset_index()
avg_salary_by_title_DS = data[data["Position"]== 'Data Scientis'].sort_values(by=['salary'] ,ascending=False)
groupby_DS = avg_salary_by_title_DS.groupby('Education').mean()['salary'].reset_index()

plt.plot(groupby_DA['Education'], groupby_DA['salary'], label = "Data Analyst")
plt.plot(groupby_DE['Education'], groupby_DE['salary'], label = "Data Engineer")
plt.plot(groupby_DS['Education'], groupby_DS['salary'], label = "Data Scientis")
plt.ylabel("Average Salary", size=15)
plt.xlabel('Education', size=15)
plt.xticks(rotation=360)
plt.title("Average Salary of DA DE DS Group by Education", size=20)
plt.legend()
plt.show()