
# coding: utf-8

# In[ ]:

# Input Files: 1. (PS $2, PC $10)NMB-Best (PS $4, PC $4).csv
                    # Columns: 'WTP', 'Base Prime', 'Prevention 1', 'Prevention 2'
#              2. (PS $2, PC $10)NMB-Worse (PS $4, PC $4).csv
                    # Columns: Ditto above.
# Summary: 1. Data Read In
        #  2. Columns and variables extracted from variables.
        #  3. 3 separate line plots plotted for strain replacement data.
        #  4. 3 separate line plots plotted for no strain replacement data.
        #  5. Output both plots in separate PDFs.
# Output: Stored in folder containing notebook file (PDF format).


# In[5]:

# Load required modules ===============================================================
get_ipython().magic(u'matplotlib inline')
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib as mpl


# In[8]:

# Load data/Read in CSV files ===============================================================
best = pd.read_csv('(PS $2, PC $10)NMB-Best (PS $4, PC $4).csv')
worse = pd.read_csv('(PS $2, PC $10)NMB-Worse (PS $4, PC $4).csv')


# In[3]:

# Transform the data ===============================================================
# Get the y-values for variables (with strain replacement)
worse.prevention_1 = worse[['WTP','Prevention 1']]
worse.prevention_1 = worse.prevention_1.dropna(axis=0, how='any') # Drop any NA values from the dataset
worse.prevention_2 = worse[['WTP','Prevention 2']]
worse.prevention_2 = worse.prevention_2.dropna(axis=0, how='any')
worse.base_prime = worse[['WTP','Base Prime']]
worse.base_prime = worse.base_prime.dropna(axis=0, how='any')
# Get the y-values for variables (with no strain replacement)
best.prevention_1 = best[['WTP','Prevention 1']]
best.prevention_1 = best.prevention_1.dropna(axis=0, how='any')
best.prevention_2 = best[['WTP','Prevention 2']]
best.prevention_2 = best.prevention_2.dropna(axis=0, how='any')
best.base_prime = best[['WTP','Base Prime']]
best.base_prime = best.base_prime.dropna(axis=0, how='any')


# In[4]:

# With Strain Replacement Line Plot ===============================================================
mpl.style.use('classic') # Use classic MPL layout
# Make the line plots
worse.prevention_1.graph = plt.plot(worse.prevention_1['WTP'], 
                                    worse.prevention_1['Prevention 1'], 
                                    color = 'green', linewidth = 3)
worse.prevention_2.graph = plt.plot(worse.prevention_2['WTP'], 
                                    worse.prevention_2['Prevention 2'], 
                                    color = 'blue', linewidth = 3)
worse.base_prime.graph = plt.plot(worse.base_prime['WTP'], 
                                  worse.base_prime['Base Prime'], 
                                  color = 'red', linewidth = 3)
plt.xticks([0,660,1000,2000])
plt.xlim([-0,2000])
plt.ylim([-20,60])
plt.axvline(x=660, color='black', ls='--')
plt.axhline(y=0, color='black', ls=':')
plt.axvspan(0, 660, color='#F9E7DB') # Shade everything bounded between x = 0 and  x= 660 beige
plt.xlabel('Cost Effectiveness Threshold to Avert One DALY ($\omega$)')
plt.ylabel('Expected Gain in NMB (Million)')
plt.title('Assuming Strain Replacement')
# color the plotted lines
red = mlines.Line2D([], [], color='red', ls='-')
green = mlines.Line2D([], [], color='green', ls='-')
blue = mlines.Line2D([], [], color='blue', ls='-')
plt.legend((red, green, blue), ('Base Prime', 'Prevention 1', 'Prevention 2',), 
           loc = 4, prop={'size':7})
plt.tight_layout() # Ensure tight layout so legend/labels are not cut off
plt.savefig('Economic Evaluation (PS $2, PC $10) ~ Worse.pdf') # Save plot to PDF


# In[5]:

# With No Strain Replacement Line Plot (Modified from above) ===============================================================
best.prevention_1.graph = plt.plot(best.prevention_1['WTP'], 
                                   best.prevention_1['Prevention 1'], color = 'green', linewidth = 3)
best.prevention_2.graph = plt.plot(best.prevention_2['WTP'], 
                                   best.prevention_2['Prevention 2'], color = 'blue', linewidth = 3)
best.base_prime.graph = plt.plot(best.base_prime['WTP'], 
                                 best.base_prime['Base Prime'], color = 'red', linewidth = 3)
plt.xticks([0,660,1000,2000])
plt.xlim([-0,2000])
plt.ylim([-20,60])
plt.axvline(x=660, color='black', ls='--')
plt.axhline(y=0, color='black', ls=':')
plt.axvspan(0, 660, color='#F9E7DB')
plt.xlabel('Cost Effectiveness Threshold to Avert One DALY ($\omega$)')
plt.ylabel('Expected Gain in NMB (Million)')
plt.title('Assuming No Strain Replacement')
red = mlines.Line2D([], [], color='red', ls='-')
green = mlines.Line2D([], [], color='green', ls='-')
blue = mlines.Line2D([], [], color='blue', ls='-')
plt.legend((red, green, blue), ('Base Prime', 'Prevention 1', 'Prevention 2',), loc = 4, prop={'size':7})
plt.tight_layout()
plt.savefig('Economic Evaluation (PS $2, PC $10) ~ Best.pdf')

