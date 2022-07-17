

import pandas as pd


data = pd.read_excel(r'D:\challenge_5.xlsx')
df = pd.DataFrame(data, columns= ['age'])
df1=df.mean()                                 # obtaining average age 

       

df2=data[data['name'].duplicated() == True]      #obtaining dublicate

         

df3= pd.DataFrame(data,columns=['nationality']) #obtaining diffrent nationality 


data.sort_values("name",inplace= True) # sorting all names
data.drop_duplicates(subset="name",keep=False,inplace=True) # removing all duplicate values 
df4= pd.DataFrame(data,columns=['name']) 





