import pandas as pd
# import matplotlib.pyplot as plt
import numpy as np

pd.Series([1, 2, 3])  # retorna uma serie de um dt
np.array([1, 2, 3])  # retorna um array numpy
print(pd.Series([1, 2, 3]).values)  # retorna um array
arr = np.array([1, 2, 3])  # monta um array
print(arr != 2)  # retona array([ True, False,  True])
print(arr[arr != 2])  # retona array([1, 3]). Ele eliminou o 2 conforme condição de filtro
