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
df = pd.read_csv('Baseline - TB Incidence.csv')

# Plot the graph ===============================================================
mpl.style.use('classic') # Use classic MPL layout
plt.ticklabel_format(useOffset=False) # Plot the full year instead of in scientific form
for i in range(4, len(df.columns)): # Plot the lines
    plt.plot(df['Time (Year)'], df.iloc[0:len(df), i], color = '#8f8f8f', linewidth = '0.5')
plt.plot(df['Time (Year)'], # Plot the upper and lower boundaries
         df['L'],
         color = '#6b77f7', linewidth = '2')
plt.plot(df['Time (Year)'],
         df['U'],
         color = '#6b77f7', linewidth = '2')
plt.plot(df['Time (Year)'],
         df['Median'],
         color = 'black', linewidth = '2')
plt.fill_between(df.iloc[:,[0, 2, 3]].dropna()['Time (Year)'],  # Shade in between the boundaries
                 df['L'],
                 df['U'], color='#cccefd')
plt.ylim([0, 2500])
plt.xlim([2000, max(df['Time (Year)']) + 2])
plt.xlabel('Time (Year)')
plt.ylabel('Incident TB cases\n per 100,000 population')
line = mlines.Line2D([],[], color="black", label = 'Median', linewidth=2) # Make a line for the legend
plt.legend(handles = [line, patch], prop={'size':10}, bbox_to_anchor=(0, 0), loc = 3) # Plot the legend
plt.tight_layout()
plt.savefig('Baseline_TB.pdf', bbox_inches='tight')
