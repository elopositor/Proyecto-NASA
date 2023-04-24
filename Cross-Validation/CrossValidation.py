# Double cross-validation
import numpy as np
import pandas as pd
from sklearn import datasets 
from random import sample

# Importing random data set for clasification
X, y = datasets.load_iris(return_X_y=True)
names = ["sepal.length", "sepal.width", "petal.length", "petal.width"]

X = pd.DataFrame(X, columns=names)
y = pd.DataFrame(y, columns=["variety"])

# Function for data partition
kFold = 0.7




nTrain = round(0.7*len(y))
allSamples = list(range(0,len(y)))
trainTest = sample(allSamples,nTrain)
pd.Series(allSamples)[trainTest]


y[nTrain:]

