import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read the csv file

from google.colab import files   
uploaded = files.upload()

df = pd.read_csv("flights.csv")

df.head()

# show column name in the dataset
print(df.columns)

# show the index in dataset
print(df.index)

# statistical operation
print(df.describe())

# show count of dataset
print(df.count(axis=0))
# show shape of dataset
print(df.shape)

# datatypes
print(df.dtypes)

# dataframe converted to numpy array
print(df.to_numpy())

# Transpose of matrix
print(df.T)

# sorting data in reverse order axis =0 = row
print(df.sort_index(axis=0, ascending=False))

# sorting data in reverse order axis =1 = column
print(df.sort_index(axis=1, ascending=False))

# find info of all dataset
print(df.info)

# changing / Set the columns name
df.columns = list(["sr_no","Experience","Salary"])
print(df.head())

# drop some columns or row value (axis =0 -> row, axis =1 ->columns)

print(df.drop(0,axis=0))

# print some specific value
print(df.loc[[1,2],['Experience','Salary']])

# slicing
print(df.loc[20:,['Experience','Salary']])

# modified value to NONE
df['Salary'] = None
print(df['Salary'])
print(df['Salary'].isnull())

# checking NA value
print(df.isna())

import seaborn as sns
import matplotlib.pyplot as plt

a = sns.load_dataset("flights")
sns.relplot(x="passengers",y="month",hue="year",data=a)

# Bar graph 
sns.catplot(x="month",y="passengers",data=a,hue="year" ,kind='bar')

# Line Plot 
b = sns.load_dataset("flights")
sns.relplot(x="passengers",y="month",data=b,kind="line")

# Ploting categorical data with seaborn
# violin catplot
sns.catplot(x="month",y="passengers",kind="violin",data=b)

sns.catplot(x="month",y="passengers",kind="boxen",data=b)

# Univariate Distribution
from scipy import stats
c=np.random.normal(loc=5, size=100,scale=2)
plt.title=("Univariate Distribution")
sns.displot(c)



sns.set(style="dark")
a = sns.load_dataset("flights")
b = sns.PairGrid(a)
b.map(plt.scatter)

# plot box plot
sns.set(style="white",color_codes=True)
a=sns.load_dataset('flights')
sns.boxplot(x='month',y='passengers',data=a)

