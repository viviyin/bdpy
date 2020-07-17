import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df1 = pd.DataFrame(np.random.normal(1.0, 0.08, (100, 8)))
print(df1.head())
cumulated = df1.cumprod()
print(cumulated.head())
cumulated.plot()
plt.show()
