import pandas as pd

XYZ_web={'Day':[1,2,3,4,5,6],"Visitors":[1000,700,6000,1000,400,350],"Bounce Rate":[20,20,23,15,10,34]}
df=pd.DataFrame(XYZ_web)
#Slicing
print(df.head(2)),df.tail(2)

#Merging
df1=pd.DataFrame({"HPI":[80,90,70,60],"Int_Rate":[2,1,2,3],"IND_GDP":[50,45,45,67]},
                 index=[2001,2002,2003,2004])
df2=pd.DataFrame({"HPI":[80,90,70,60],"Int_Rate":[2,1,2,3],"IND_GDP":[50,45,45,67]},
                  index=[2005,2006,2007,2008])
merge=pd.merge(df1,df2,on="HPI")
print(merge)

#Joining

df1=pd.DataFrame({"Int_Rate":[2,1,2,3],"IND_GDP":[50,45,45,67]},
                 index=[2001,2002,2003,2004])
df2=pd.DataFrame({"Low_Tier_HPI":[50,45,67,34],"Unemployment":[1,3,5,6]},
                  index=[2001,2003,2004,2004])

joined=df1.join(df2)
print(joined)

#Changing the index and column headers
"""import matplotlib.pyplot as plt
from matplotlib import style
style.use("fivethirtyeight")

df=pd.DataFrame({"Day":[1,2,3,4],"Visitors":[200,100,230,300],"Bounce Rate":[20,45,60,10]})
df.set_index("Day",inplace=True)
df.plot()
plt.show()"""

df=pd.DataFrame({"Day":[1,2,3,4],"Visitors":[200,100,230,300],"Bounce Rate":[20,45,60,10]})
df=df.rename(columns={"Visitors":"Users"})
print(df)

#Concatenation

df1=pd.DataFrame({"Int_Rate":[2,1,2,3],"IND_GDP":[50,45,45,67]},
                 index=[2001,2002,2003,2004])
df2=pd.DataFrame({"Low_Tier_HPI":[50,45,67,34],"Unemployment":[1,3,5,6]},
                  index=[2001,2003,2004,2004])
Concat=pd.concat([df1,df2])
print(Concat)

#Data Munging

