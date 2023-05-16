import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

%matplotlib inline

df=pd.read_csv("Pecan.csv")

df.head()

df.info()

plt.scatter(df["Fertilizer per acre"],df["Pecan Production"])

from sklearn.linear_model import LinearRegression

X=df.values[:, range(0,3)]

y=df.values[:,3]

model=LinearRegression().fit(X, y)

print(model.coef_)

print(model.intercept_)

clientData=[[120, 5, 80],
          [50, 1, 150],
          [100, 80, 100],
           [99, 78, 105]
        ]
print(model.predict(clientData))


