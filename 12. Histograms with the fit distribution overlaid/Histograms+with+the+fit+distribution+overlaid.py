
# coding: utf-8

# In[1]:

# Load required modules ===============================================================
get_ipython().magic(u'matplotlib inline')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns


# In[9]:

# Load data/Read in CSV files ===============================================================
df = pd.read_csv('*****Data*****.csv', header = None)


# In[17]:

mpl.style.use('classic') # Use classic MPL layout
sns.distplot(df, color = 'black'); # Plot histogram with overlay
plt.title('Histogram with Distribution Overlay')
plt.xlabel('Value')
plt.ylabel('Probability')
plt.tight_layout() # Ensure tight layout so legend/labels are not cut off
plt.savefig('histogram.pdf') # Save plot to PDF

