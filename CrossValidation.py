# Double cross-validation
import numpy as np
import pandas as pd
from sklearn import svm

# Creating data frame
Xrand = np.random.randn(1000, 40)
X = pd.DataFrame(Xrand)
X.head(10)

Y = np.array([0, 1])

# Filas: muestras / registros
# Columnas: variables / features
X.np.sp
