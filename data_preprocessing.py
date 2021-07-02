# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 15:28:39 2021

@author: j1013903
"""

#importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importing the dataset
dataset = pd.read_csv('Data.csv')
x= dataset.iloc[:, :-1].values
y=dataset.iloc[:,-1].values

print(x)
print(y)

#missing data
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan,strategy="mean")
imputer.fit(x[:,1:3])
x[:,1:3]=imputer.transform(x[:,1:3])

print(x)

#Encoding the independent variables
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct= ColumnTransformer(transformers=[('encoder',OneHotEncoder(),[0])],remainder='passthrough')
x= np.array(ct.fit_transform(x))

print(x)

#Encoding the dependent variables
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y=le.fit_transform(y)

print(y)

#splitting 
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test =train_test_split(x, y, test_size=0.2,random_state=1)

print("x_train \n", x_train)

print("x_train \n",x_test)

print("y_train \n",y_train)

print("y_test \n",y_test)

#feature scaling
from sklearn.preprocessing import StandardScaler
sc= StandardScaler()
x_train[:,3:]=sc.fit_transform(x_train[:,3:])
x_test[:,3:]=sc.transform(x_test[:,3:])

print(x_train)