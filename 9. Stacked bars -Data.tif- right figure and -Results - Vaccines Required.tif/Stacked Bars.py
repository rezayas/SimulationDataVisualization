
# coding: utf-8

# In[1]:

# Input Files: 1. Model - Vaccines Used  (Worse).csv
                    # Columns: 'Unnamed: 0', 'MenAfriVac®', 'MenAfriVac®.1', 'PMP-Reactive', 
                    #          'PMP-Reactive.1', 'PMC-Routine', 'PMC-Routine.1', 'PMC-Preventive', 
                    #          'PMC-Preventive.1', 'PMC-Reactive', 'PMC-Reactive.1'
#              2. Model - Vaccines Used  (Best).csv
                    # Columns: Ditto above.
#              3. Data - Distribution of Clinical Men.csv
                    # Columns: 'Unnamed: 0', 'Neisseria Men-A', 'Neisseria Non Men-A', 'Others'
# Summary: 1. Data read in.
        #  2. Horizontal stacked bar plots each plotted separately and saved. (First with strain replacement, then without)
        #  3. Horizontal stacked bar plots plotted side by side and saved (subplots created).
        #  4. Vertical stacked bar plot plotted and saved.
# Output: Stored in folder containing notebook file (PDF format).


# In[2]:

# Load required modules ===============================================================
get_ipython().magic(u'matplotlib inline')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import pylab


# In[8]:

# Load data/Read in CSV files ===============================================================
worse = pd.read_csv('Model - Vaccines Used  (Worse).csv')
best = pd.read_csv('Model - Vaccines Used  (Best).csv')
clinical = pd.read_csv('Data - Distribution of Clinical Men.csv')


# In[3]:

# Assuming Strain Replacement Bar Plot ===============================================================
mpl.style.use('classic') # Use classic MPL layout
plot = worse.iloc[:,[0,3,1,9,7,5]].plot(kind='barh', stacked=True, 
                                 color = ['#c10d0d', '#4f42dd', '#f7950c', '#9b14bc', '#34af18']) # plot bar plot
plot.set_yticklabels(worse['Unnamed: 0']) # Set labels to be categories
plot.set_xlabel('Number of Vaccines Used per Year (Thousands)')
handles, labels = plot.get_legend_handles_labels() # get labels of original legend
plot.legend([handles[1], handles[0], handles[4], handles[3], handles[2]],
           [labels[1], labels[0], labels[4], labels[3], labels[2]], 
            loc='upper left', bbox_to_anchor=(1, 1),prop={'size':10}) # reorder the labels
plot.set_title('Assuming Strain Replacement')
plt.tight_layout() # Ensure tight layout so legend/labels are not cut off
plt.savefig('Results - Vaccines Required ~ Worse.pdf', bbox_inches="tight") # Save plot to PDF


# In[4]:

# Assuming No Strain Replacement Bar Plot (Modified code from above) ===============================================================
plot = best.iloc[:,[0,3,1,9,7,5]].plot(kind='barh', stacked=True, 
                                 color = ['#c10d0d', '#4f42dd', '#f7950c', '#9b14bc', '#34af18'])
plot.set_yticklabels(best['Unnamed: 0'])
plot.set_xlabel('Number of Vaccines Used per Year (Thousands)')
handles, labels = plot.get_legend_handles_labels()
plot.legend([handles[1], handles[0], handles[4], handles[3], handles[2]],
           [labels[1], labels[0], labels[4], labels[3], labels[2]],
           loc='upper left', bbox_to_anchor=(1, 1),prop={'size':10})
plot.set_title('Assuming No Strain Replacement')
plt.tight_layout()
plt.savefig('Results - Vaccines Required ~ Best.pdf', bbox_inches="tight")


# In[5]:

# Both Bar Plots in One Figure ===============================================================
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 4)) # Initialise figure with 1 row and 2 columns
plot = worse.iloc[:,[0,3,1,9,7,5]].plot(kind='barh', stacked=True, 
                                 color = ['#c10d0d', '#4f42dd', '#f7950c', '#9b14bc', '#34af18'], ax=axes[0],
                                       legend = None) # Plot the first subplot
plot.set_yticklabels(worse['Unnamed: 0'])
plot.set_xlabel('Number of Vaccines Used per Year (Thousands)')
plot.set_title('Assuming Strain Replacement')
plot = best.iloc[:,[0,3,1,9,7,5]].plot(kind='barh', stacked=True, 
                                 color = ['#c10d0d', '#4f42dd', '#f7950c', '#9b14bc', '#34af18'], 
                                       ax=axes[1]) # Plot the second subplot
plot.set_yticklabels([]) # Remove tick labels as it will share tick labels with the other subplot
plot.set_xlabel('Number of Vaccines Used per Year (Thousands)')
handles, labels = plot.get_legend_handles_labels()
plot.legend([handles[1], handles[0], handles[4], handles[3], handles[2]],
           [labels[1], labels[0], labels[4], labels[3], labels[2]],
           loc='upper left', bbox_to_anchor=(1, 1),prop={'size':10})
plot.set_title('Assuming No Strain Replacement')
plt.tight_layout()
plt.savefig('Results - Vaccines Required.pdf', bbox_inches="tight")


# In[6]:

# Vertical Stacked Bar Plots ===============================================================
plot = clinical.drop(['Unnamed: 0'], axis=1).iloc[:,[2,1,0]].plot(kind='bar', stacked=True,
                                                                  color=['#56db04','red','blue']) # Plot the bar plot
plot.set_xticklabels(clinical['Unnamed: 0'])
plot.set_xlabel('Year')
plot.set_ylim([0,100])
handles, labels = plot.get_legend_handles_labels() # Get the legend handles
plot.legend([handles[2], handles[1], handles[0]],
           [labels[2], labels[1], labels[0]],
           loc='upper left', bbox_to_anchor=(1, 1),prop={'size':10}) # Reorder the legend handles
plt.tight_layout()
plt.savefig('Data.pdf', bbox_inches="tight")

