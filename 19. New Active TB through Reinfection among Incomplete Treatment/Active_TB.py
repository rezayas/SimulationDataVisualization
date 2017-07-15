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
df = pd.read_csv('Fit-% New Active TB through Reinfection among Incomplete Treatment.csv')

# Plot the graph ===============================================================
mpl.style.use('classic') # Use classic MPL layout
plt.ticklabel_format(useOffset=False) # Plot the full year instead of in scientific form
for i in range(4, len(df.columns)): # Plot the lines
    plt.plot(df['Time (Year)'], df.iloc[0:len(df), i], color = '#787878', linewidth = '2')
plt.plot(df.iloc[:,[0, 2, 3]].dropna()['Time (Year)'], # Plot the bounding boxes
         df.iloc[:,[0, 2, 3]].dropna()['L'],
         color = '#6b77f7', linewidth = '2')
plt.plot(df.iloc[:,[0, 2, 3]].dropna()['Time (Year)'],
         df.iloc[:,[0, 2, 3]].dropna()['U'],
         color = '#6b77f7', linewidth = '2')
plt.vlines(df.iloc[:,[0, 2, 3]].dropna()['Time (Year)'],
           0, 100, color = 'black', linestyles = 'dashed') # Plot the vertical lines
plt.fill_between(df.iloc[:,[0, 2, 3]].dropna()['Time (Year)'], # Shade in between the boundaries
                 df.iloc[:,[0, 2, 3]].dropna()['L'],
                 df.iloc[:,[0, 2, 3]].dropna()['U'], color='#cccefd') # Shade in between the lines
plt.ylim([0, 100])
plt.xlim([2000, 2020])
plt.xlabel('Time (Year)')
plt.xticks([2000, df.iloc[:,[0, 2, 3]].dropna()['Time (Year)'][0],
            df.iloc[:,[0, 2, 3]].dropna()['Time (Year)'].reset_index(drop = True)[1],
            2010, 2020])
plt.title('% New Active TB through Reinfection\n among Individuals with History of\n Incomplete TB Treatment')
patch = mpatches.Patch(color='#cccefd', label='Feasible Range') # Make box
plt.legend(handles = [patch], prop={'size':10}, bbox_to_anchor=(1, 1), loc = 2) # Plot the legend
plt.tight_layout()
plt.savefig('Active_TB.pdf', bbox_inches='tight')
