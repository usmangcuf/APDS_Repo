# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 23:16:06 2023

@author: Adeel
"""

import pandas as pd
import scipy.stats
def func():
    df=pd.read_csv("e://data1.csv")
    df1=df[["Country Name","Indicator Name"]]
    df2=df[["Country Name","Country Code"]]
    df3=df.melt(id_vars=['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code'], 
        var_name="Year", 
        value_name="Value")

    
    return df1,df2,df3
d1,d2,d3=func()
d1
d2
d3
d3.Year=d3.Year.astype(int)
d4=d3[(d3.Year >= 1980) & (d3.Year <= 1985)]
d5=d3[(d3.Year >= 1986) & (d3.Year <= 1991)]

d4=d4.fillna(0)
d5=d5.fillna(0)
d4
d5
print(d4.describe())
print(d5.describe())
#print(d4.isnull())
d4_group = d4.groupby(by="Year")["Value"].sum()
d5_group = d5.groupby(by="Year")["Value"].sum()
print(d4_group)
print(d5_group)
print(scipy.stats.pearsonr(d4_group,d5_group))
