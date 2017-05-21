
# coding: utf-8

# In[1]:

# Load required modules ===============================================================
get_ipython().magic(u'matplotlib inline')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


# In[2]:

# Load data/Read in CSV files ===============================================================
df= pd.read_csv('****Data****.csv')


# In[17]:

mpl.style.use('classic') # Use classic MPL layout
fig, ax = plt.subplots(ncols=2, sharey=True) # Create 2 subplots that share a common y-axis
# Create subplots with y-axis values to be the number of categories
ax[0].barh(range(0,len(df['AGE']),1), df['MALE'], color='blue', 
          align = 'center')
ax[1].barh(range(0,len(df['AGE']),1), df['FEMALE'], color='red',
          align = 'center')
fig.canvas.draw() # manually force figure to draw
ax[0].invert_xaxis() # invert x-axis so subplot looks like a pyramid when combined with other subplot
ax[0].set_yticks(range(0,len(df['AGE']),1)) # set number of ticks to be the number of categories
ax[0].set_yticklabels(df['AGE'])
ax[0].yaxis.tick_right() # move ticks to the right y-axis
ax[0].set_ylim([-1,len(df['AGE'])])
ax_0_labels = ax[0].get_xticklabels() # get original x-tick labels
ax_1_labels = ax[1].get_xticklabels()
ax[0].set_xticklabels(ax_0_labels, fontsize = 8) # plot obtained x-tick labels on x-axis but with smaller font
ax[1].set_xticklabels(ax_1_labels, fontsize = 8)
plt.suptitle('Population Pyramid\nYale School of Public Health') # Create title in between subplots
plt.tight_layout() # Ensure tight layout so legend/labels are not cut off
plt.savefig('population_pyramid.pdf') # Save plot to PDF

