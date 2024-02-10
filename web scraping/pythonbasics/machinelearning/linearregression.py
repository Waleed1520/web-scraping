import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model



df = pd.read_csv('data.csv')
print(df)

#plt.xlabel('area(sqr ft)')
#plt.ylabel('prices($)')
#plt.scatter(df.area,df.prices,color='red',marker='+')

#reg = linear_model.LinearRegression()
#reg.fit(df[['area']],df.prices)



