
# coding: utf-8

# In[2]:

import numpy as np
import matplotlib.pyplot as plt

def plot_data(clean_data,weather_type):
    plt.plot(clean_data)
    plt.xlabel('Data Point Number')
    plt.ylabel(weather_type)
    title_str = 'A plot of '+ weather_type + ' vs. datapoint for a Natick, MA weather station'
    plt.title(title_str)
    plt.show()


# In[ ]:



