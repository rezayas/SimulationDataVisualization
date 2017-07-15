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
df = pd.read_csv('Fit-Notified Naive Adult Cases.csv')

# Plot the graph ===============================================================
mpl.style.use('classic') # Use classic MPL layout
plt.ticklabel_format(useOffset=False) # Plot the full year instead of in scientific form
for i in range(2, len(df.columns)): # Plot the lines
    plt.plot(df['Time (Year)'], df.iloc[0:len(df), i], color = '#787878', linewidth = '2')
plt.plot(df.iloc[:,[0, 1]].dropna()['Time (Year)'], # Plot the target lines
         df.iloc[:,[0, 1]].dropna()['Target'],
         color = 'black', linewidth = '5', marker = 'o', markersize = '10')
plt.vlines([min(df.iloc[:,[0, 1]].dropna()['Time (Year)']),
            max(df.iloc[:,[0, 1]].dropna()['Time (Year)'])],
           0, 400, color = 'black', linestyles = 'dashed') # Plot the bounding vertical lines
plt.ylim([0, 400])
plt.xlim([2000, 2020])
plt.xlabel('Time (Year)')
plt.title('TB Case Notifications (N),\n Treatment-Naive Adults')
plt.tight_layout()
plt.savefig('Adult_Cases.pdf', bbox_inches='tight')
