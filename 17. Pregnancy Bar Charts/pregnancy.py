# Load required modules ===============================================================
get_ipython().magic(u'matplotlib inline')
import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.patches as mpatches
import matplotlib.lines as mlines

# Load data/Read in CSV files ===============================================================
combined = pd.ExcelFile('For visualization.xlsm')
outcomes = combined.parse('Outcomes')
outcomes.columns = outcomes.iloc[0] # Rename column headers
outcomes = outcomes[1:] # Delete extra column heads

# Extract the data ===============================================================
unintended = outcomes.iloc[0:10,9:19].dropna() # Extract the unintended pregnancies dataset
projection_period = outcomes.iloc[0:10,30:38] # Extract the projection_period ataset
projection_period = projection_period * 100 # Convert raw numbers to percentages

# In[1]:
# Plot the unintended pregnancies ===============================================================
mpl.style.use('classic') # Use classic MPL layout
plt.bar(range(1,11), unintended.iloc[0, 0:11], align = 'center', color = 'orange')
plt.errorbar(range(1,11), unintended.iloc[1, 0:11], # Plot the error bar
             np.array([unintended.iloc[4, 0:11], unintended.iloc[5, 0:11]]), fmt = 'o')
plt.xticks(range(1,11), list(unintended.columns.values), rotation='vertical')
plt.xlim([0, 11])
plt.ylim([0,40])
circle = mlines.Line2D([],[], marker='o',
                        markerfacecolor="blue", label = 'Model - Median') # Make a circle for the legend
cdc = mpatches.Patch(color='orange', label='CDC') # Make an orange square
plt.legend(handles = [cdc, circle], numpoints = 1, # Plot the legend
           prop={'size':10}, bbox_to_anchor=(1, 1), loc = 2)
plt.title('Number of Unintended Pregnancies \n(Per 100 People)')
plt.tight_layout()
plt.savefig('unintended_pregnancies.pdf', bbox_inches='tight')

# In[2]:
# Plot the projection periods (code is modified from above)===============================================================
plt.bar(range(1,7), projection_period.iloc[0, 1:7], align = 'center', color = 'orange')
plt.errorbar(range(1,7), projection_period.iloc[0, 1:7], np.array([projection_period.iloc[3, 1:7],
                projection_period.iloc[4, 1:7]]), fmt = 'none', ecolor = 'red') # Plot CDC error bar
plt.errorbar(range(1,7), projection_period.iloc[5, 1:7], np.array([projection_period.iloc[8, 1:7],
                projection_period.iloc[9, 1:7]]), color = 'blue', fmt = 'o') # Plot the other error bar
plt.xticks(range(1,7), list(projection_period.columns.values)[1:7])
plt.xlim([0, 7])
plt.ylim([0, 20])
circle = mlines.Line2D([],[], marker='o', markerfacecolor="blue", label = 'Model - Median')
cdc = mpatches.Patch(color='orange', label='CDC')
plt.legend(handles = [cdc, circle], numpoints = 1,
           prop={'size':10}, bbox_to_anchor=(1, 1), loc = 2)
plt.title('% Pregnant at the end of projection period')
plt.tight_layout()
plt.savefig('projection_period.pdf', bbox_inches='tight')
