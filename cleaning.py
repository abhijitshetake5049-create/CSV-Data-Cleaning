import numpy as np
import pandas as pd
df=pd.read_csv("employee_data_cleaning_100_rows_proper.csv")
print(df)

print(df.isnull().sum())


print(df)
print(df.dtypes)




#this used to repclace the -inf and inf to Nan
df.replace([np.inf,-np.inf],np.nan,inplace=True)

#this used put fill specific value using the fillna
df["Age"]=df["Age"].fillna(df["Age"].median())
df['Salary (INR)']=df['Salary (INR)'].fillna(df['Salary (INR)'].mean())
df["Performance Rating"]=df["Performance Rating"].fillna(df["Performance Rating"].median())
df["City"]=df["City"].fillna("Unkown_city")
df["Experience (Years)"]=df["Experience (Years)"].fillna(df["Experience (Years)"].median())



#for the duplicates values removing bro
df.drop_duplicates(inplace=True)
print(df)


#need to work on the outliers right 
#outlier we can give the condtion make the outlier right 
df["Age"]=np.where(df["Age"]<0,df["Age"].mean(),df["Age"])

age_mean=df["Age"].mean()
age_std=df["Age"].std()
lower_bound=age_mean-(3*age_std)
upper_bound=age_mean+(3*age_std)
df=df[(df["Age"]>=lower_bound)&(df["Age"]<=upper_bound)]


#this process for the otileries removing 
df["Salary (INR)"]=np.where(df["Salary (INR)"]<0,df["Salary (INR)"].mean(),df["Salary (INR)"])
mean_slaray=df["Salary (INR)"].mean()
salary_std=df["Salary (INR)"].std()
lower_bound1=mean_slaray-(3*salary_std)
upper_bound1=mean_slaray+(3*salary_std)
df=df[(df["Salary (INR)"]>=lower_bound1)&(df["Salary (INR)"]<=upper_bound1)]

#this new cleaned file 
df.to_csv("new.csv")

