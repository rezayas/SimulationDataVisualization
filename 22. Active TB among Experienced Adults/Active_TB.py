# In[1]:

# Load required modules ===============================================================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.patches as mpatches
import matplotlib.lines as mlines

# In[2]:

# Load data/Read in CSV files ===============================================================
temp = pd.read_csv('Fit-Active TB among Experienced Adults.csv')
df = temp.iloc[:,0:4]
for i in range(4, len(temp.columns), 3): # Clean the data; delete columns without any values
    df[i] = temp[temp.columns[i]]

# Plot the graph ===============================================================
mpl.style.use('classic') # Use classic MPL layout
plt.ticklabel_format(useOffset=False) # Plot the full year instead of in scientific form
for i in range(4, len(df.columns)): # Plot the lines
    plt.plot(df['Time (Year)'], df.iloc[0:len(df), i], color = '#787878', linewidth = '2')
plt.plot(list(df.iloc[:,[0, 1]].dropna()['Time (Year)']) * 2, # Plot the target bounds
         df.iloc[:, 2:4].dropna().iloc[0], color = 'black', linewidth = '5', marker = '_',
         markersize = '15', mew = '5')
plt.plot(df.iloc[:,[0, 1]].dropna()['Time (Year)'], # Plot the mean
         df.iloc[:, 1].dropna(), color = 'black', marker = 'o', markersize = '9')
plt.vlines(df.iloc[:,[0, 4, 5]].dropna()['Time (Year)'],
           0, 100, color = 'black', linestyles = 'dashed') # Plot the bounding vertical lines
plt.ylim([0, 6])
plt.xlim([2000, 2020])
plt.xlabel('Time (Year)')
plt.title('TB Prevalence (%),\nTreatment-Experienced Adults')
plt.tight_layout()
plt.savefig('Active_TB.pdf', bbox_inches='tight')
