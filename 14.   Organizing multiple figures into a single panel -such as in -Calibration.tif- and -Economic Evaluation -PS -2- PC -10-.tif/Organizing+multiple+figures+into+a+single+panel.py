
# coding: utf-8

# In[1]:

# Load required modules ===============================================================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib as mpl


# In[ ]:

# Load data/Read in CSV files ===============================================================
df= pd.read_csv('****Data****.csv')


# In[2]:

mpl.style.use('classic') # Use classic MPL layout
fig = plt.figure() # add plot figure
# add sublots with 2 columns and 2 rows
fig.add_subplot(221)
fig.add_subplot(222)
fig.add_subplot(223)
fig.add_subplot(224)
plt.tight_layout() # Ensure tight layout so legend/labels are not cut off
plt.savefig("filename.pdf") # Save plot to PDF
