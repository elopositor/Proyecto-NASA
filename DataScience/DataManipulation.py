import numpy as np
import pandas as pd
import sklearn
from sklearn.datasets import load_iris

# Dataframes de pandas
df = pd.DataFrame(data=load_iris().data, columns=load_iris().feature_names)

df.info() # Info dataset
datos.shape # ncol & nrow 
datos.isna().sum().
