import pandas as pd
import matplotlib.pyplot as plt
from pandas.core import accessor
import seaborn as sns
data = pd.read_excel(r"C:\Users\APHISIT\OneDrive\Desktop\เอกสาร Msyne\งานเดี่ยว\PYTHON\example_data_training_Mspire.xlsx")
data_clean = data.drop(['first_name' , 'last_name' , 'zip' , 'phone' , 'email' ,'address'] , axis=1) 

import pandas as pd
import matplotlib.pyplot as plt
from pandas.core import accessor
import seaborn as sns
data = pd.read_excel(r"C:\Users\APHISIT\OneDrive\Desktop\เอกสาร Msyne\งานเดี่ยว\PYTHON\example_data_training_Mspire.xlsx")
data_clean = data.drop(['first_name' , 'last_name' , 'zip' , 'phone' , 'email' ,'address'] , axis=1)

group = data_clean.groupby('Position')['id'].count()
print(group)
a = ('Data Analyst','Data Engineer','Data Scientis','Hardware Engineer','Network Engineer','Software Engineer','Software QA','Software Tester','Solution Architect')
b = (52,65,58,58,54,42,66,49,56)
explode = (0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05,0.05) 
fig1, ax1 = plt.subplots()
ax1.pie(b,explode=explode,labels=a, autopct='%1.1f%%',  startangle=90,pctdistance=0.85)
centre_circle = plt.Circle((0,0),0.70,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
ax1.axis('equal') 
ax1.set(title="Position")
plt.tight_layout()
plt.show()

