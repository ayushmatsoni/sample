import pandas as pd
import numpy as np
data={'NAME':['AYUSHMAT'],'age':[20],'mail id':['ayushmats@gmail.com'],'phone no.':[9882540059]}
df=pd.DataFrame(data)
print(df)
print("\n \n INFO ADDED! ")
df.loc[1]=['qwerty',22,'qwerty@gmail.com',1234567890]
print(df)


data=pd.read_csv("weather.csv")
df=pd.DataFrame(data)
print("FIRST FIVE ROWS")
print(df.head(5))
print("\n")
print("FIRST TEN ROWS->")
print(df.head(10))
print("\n")
print("BASIC STATISTICS -->")
print("AXES->\n"+str(df.axes))
print("DATATYPES->\n"+str(df.dtypes))
print("DIMENSIONS->\n"+str(df.ndim))
print("SHAPE->\n"+str(df.shape))
print("SIZE->\n"+str(df.size))
print("\n")
print("LAST FIVE ROWS->")
print(df.tail(5))
print("\n")


x=df.loc[:,'Location']
print(x)
print("BASIC STATISTICS ARE->")
print("AXES->\n"+str(x.axes))
print("DATATYPES->\n"+str(x.dtypes))
print("DIMENSIONS->\n"+str(x.ndim))
print("SHAPE->\n"+str(x.shape))
print("SIZE->\n"+str(x.size))