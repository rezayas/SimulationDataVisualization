
# coding: utf-8

# Data - Distribution of Clinical Men.csv
# Columns: 'Unnamed: 0', 'Neisseria Men-A', 'Neisseria Non Men-A', 'Others'
# Summary: 1. Data read in.
        #  4. Vertical stacked bar plot plotted and saved.
# Output: Stored in folder containing notebook file (PDF format).


# In[2]:

# Load required modules ===============================================================
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[8]:

# Load data/Read in CSV files ===============================================================
clinical = pd.read_csv('Data - Distribution of Clinical Men Arif.csv')
labels = clinical['Unnamed: 0']
clinical = clinical.drop(['Unnamed: 0'], axis=1)
for row in range(0, len(clinical.iloc[:])):
    row_total = float(np.sum(clinical.ix[row]))
    for column in range(0, 3):
        clinical.ix[row, column] = float(clinical.ix[row, column]) / row_total * 100

# In[6]:

# Vertical Stacked Bar Plots ===============================================================
plot = clinical.iloc[:,[2,1,0]].plot(kind='bar', stacked=True,
                                     color=['#56db04','red','blue']) # Plot the bar plot
plot.set_xticklabels(labels)
plot.set_xlabel('Year')
plot.set_ylim([0,100])
handles, labels = plot.get_legend_handles_labels() # Get the legend handles
labels[1] = r'$\it{Neisseria}$ Non Men-A'
labels[2] = r'$\it{Neisseria}$ Men-A'
plot.legend([handles[2], handles[1], handles[0]],
           [labels[2], labels[1], labels[0]],
           loc='upper left', bbox_to_anchor=(1, 1),prop={'size':10}) # Reorder the legend handles
plt.savefig('Clinical Meningitis.pdf', bbox_inches="tight")
