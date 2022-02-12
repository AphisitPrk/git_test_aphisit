
import pandas as pd
import matplotlib.pyplot as plt
from pandas.core import accessor
import seaborn as sns
data = pd.read_excel(r"C:\Users\APHISIT\OneDrive\Desktop\เอกสาร Msyne\งานเดี่ยว\PYTHON\example_data_training_Mspire.xlsx")
data_clean = data.drop(['first_name' , 'last_name' , 'zip' , 'phone' , 'email' ,'address'] , axis=1) 

avg_salary_by_position = data.groupby("Position")["salary"].mean().sort_values(ascending=False)
plt.figure(figsize=(14,12))
sns.boxplot(x = data_clean["salary"], y = data_clean["Position"], order=avg_salary_by_position.index)
plt.xlabel("Average Salary", size=20)
plt.ylabel('Position', size=20)
plt.xticks(rotation=360)
plt.title("Average Salary Gruop By Position", size=25)
plt.show()
