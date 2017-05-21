
# coding: utf-8

# In[1]:

# Load required modules ===============================================================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns


# In[2]:

# Load data/Read in CSV files ===============================================================
df = pd.read_csv('****Data****.csv')


# In[ ]:

# Transform the data ===============================================================
df = df.drop('Unnamed: 0', axis=1) # drop the indexing column
df = df.pivot('Age Group','Age Group','Frequency') # transform the dataset to matrix form


# In[1]:

mpl.style.use('classic') # Use classic MPL layout
sns.heatmap(df, cmap='spectral', cbar_kws = {'label':'Contacts per Day'}) # Plot heatmap with legend label, Contacts
                                                                          # per Day and color palette, spectral
plt.xlabel('Age Group')
plt.ylabel('Age Group')
plt.title('Contact Matrix')
plt.tight_layout() # Ensure tight layout so legend/labels are not cut off
plt.savefig('Contract Matrix.pdf') # Save plot to PDF
