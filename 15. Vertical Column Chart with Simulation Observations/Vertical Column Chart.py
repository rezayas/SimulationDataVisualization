
# coding: utf-8

# In[1]:

# Load required modules ===============================================================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl


# In[20]:

# Load data/Read in CSV files ===============================================================
df = pd.read_csv('*******Data**********')


# In[94]:

# Vertical column chart with simulation observations ===============================================================
mpl.style.use('classic') # Use classic MPL layout
plt.bar(df.iloc[:,0], df['Data'], color = 'grey', width = 5, align = 'center')
plt.xlim([0,max(df.iloc[:,0]) + 0.2*max(df.iloc[:,0])])
# Plot simulations
for simulation in range(2,len(df.columns)):
    plt.scatter(df.iloc[:,0], df.iloc[:,simulation], color = '#39FF14', marker = '_', zorder = 10,
             s = 1000, linewidth = 1)
# Plot medians
for row in range(1, len(df) + 1):
    plt.scatter(df.iloc[row - 1,0], np.median(df.iloc[0:row,2:len(df.columns)]), color = 'black',
                marker = '_', zorder = 10, s = 1500, linewidth = 2.5)
plt.tight_layout() # Ensure tight layout so legend/labels are not cut off
plt.savefig('Vertical Column Chart.pdf') # Save plot to PDF
