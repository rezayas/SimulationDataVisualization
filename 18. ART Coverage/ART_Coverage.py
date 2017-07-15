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
df = pd.read_csv('ART Coverage (Naive).csv')

# Plot the graph ===============================================================
mpl.style.use('classic') # Use classic MPL layout
plt.ticklabel_format(useOffset=False) # Plot the full year instead of in scientific form
plt.plot(df['Time (Year)'], df['Median'], color = 'black', linewidth = '2') # Plot the lines
plt.plot(df['Time (Year)'], df['L'], color = '#6b77f7', linewidth = '2')
plt.plot(df['Time (Year)'], df['U'], color = '#6b77f7', linewidth = '2')
plt.fill_between(df['Time (Year)'], df['L'], df['U'], color='#cccefd') # Shade in between the lines
plt.ylim([0, 100])
plt.ylabel('Percentage ART, TB treatment-\nnaive HIV-infected adults')
plt.xlabel('Time (Year)')
line = mlines.Line2D([],[], color="black", label = 'Median', linewidth=2) # Make a line for the legend
patch = mpatches.Patch(color='#cccefd', label='90% Uncertainty Interval') # Make box
plt.legend(handles = [line, patch], numpoints = 1, # Plot the legend
           prop={'size':10}, bbox_to_anchor=(0, 1), loc = 2)
plt.tight_layout()
plt.savefig('ART_Coverage.pdf', bbox_inches='tight')
