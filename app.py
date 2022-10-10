import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data/scrubbed.csv", low_memory=False)
print(data.head(5))
print(data.dtypes)
print(data.info())

countries = data["country"]

print(countries.head())

states = data["state"]
print(states.head())

#plt.scatter(data['city'], data['country'])

#plt.title('Scatter plot')

#plt.xlabel('city')
#plt.ylabel('country')

#plt.show()



#if __name__ == "__main__":
#    display(data.head(10))
