
# coding: utf-8

# In[1]:

# Load required modules ===============================================================
get_ipython().magic(u'matplotlib inline')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl


# In[2]:

# Load data/Read in CSV files ===============================================================
response_time = pd.read_csv('Data - Response Time.csv')


# In[3]:

mpl.style.use('classic') # Use classic MPL layout
fig = plt.figure() # Create plot figure
scatter_plot = fig.add_subplot(111) # add first subplot
bar_plot = scatter_plot.twinx() # add second subplot - will use the same x-axis on the same figure
bar_plot.set_ylabel('Probability')
bar_plot.set_ylim([0.0,0.2])
scatter_plot.set_ylabel('Counts')
scatter_plot.set_ylim([0,9])
scatter_plot.set_xlabel('Response Time (Days)')
plt.xlim([0,80])
plt.xticks(response_time.iloc[:,[0,3]]['Unnamed: 0']) # Set x-ticks to be the response time variable
plot_1 = bar_plot.bar(response_time.iloc[:,[0,3]]['Unnamed: 0'], 
                      response_time.iloc[:,[0,3]]['Uniform Distribution'], 
                      color = 'grey', width = 5, align = 'center') # Add bar plot
plot_2 = scatter_plot.scatter(response_time.iloc[:,[0,3]]['Unnamed: 0'], 
                              response_time.iloc[:,[2]], s = 100) # Add scatter plot
# Plot scatter plot on top of bar plot by setting graphing order
bar_plot.set_zorder(0)
scatter_plot.set_zorder(1)
scatter_plot.patch.set_visible(False) # Set the scatter plot background to be invisible
bar_plot.legend([plot_2, plot_1], ['Data', 'Uniform Distribution'], loc = 2, scatterpoints = 1)
plt.tight_layout() # Ensure tight layout so legend/labels are not cut off
plt.savefig('Response Time.pdf') # Save plot to PDF

