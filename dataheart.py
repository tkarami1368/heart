import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data=pd.read_csv("heart.csv")
print(data.describe())
sns.pairplot(data)
plt.show()


