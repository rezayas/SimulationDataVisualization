
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
age = pd.read_csv('Data - Age Distribution.csv')
mortality = pd.read_csv('Data - Mortality Rates.csv', header = None)
life_expectancy = pd.read_csv('Data- Life Expectancy.csv', header = None)


# In[3]:

# Mortality Plot ===============================================================
mpl.style.use('classic') # Use classic MPL layout
mortality.plot(mortality[0], kind = 'bar', rot = 0, color = 'black', legend = False) # Plot bar plot
plt.title('B')
plt.ylim([0,80])
plt.xlabel('Age Group')
plt.ylabel('Mortality Rate per 1,000 population')
plt.savefig('Mortality Rate ~ Age Group.pdf') # Save plot to PDF


# In[4]:

# Life Expectancy Plot ===============================================================
life_expectancy.plot(life_expectancy[0], kind = 'bar', rot = 0, color = 'black', legend = False)
plt.title('C')
plt.ylim([0,80])
plt.xlabel('Age Group')
plt.ylabel('Life Expectancy')
plt.savefig('Life Expectancy ~ Age Group.pdf')


# In[5]:

# Age Distribution Plot ===============================================================
age.plot(age['Unnamed: 0'], kind = 'bar', rot = 0, color = 'black', legend = False)
plt.title('A')
plt.ylim([0,40])
plt.xlabel('Age Group')
plt.ylabel('Age Distribution')
plt.savefig('Age Distribution ~ Age Group.pdf')


# In[6]:

# Combined Panel Plot ===============================================================
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(12, 4)) # Create subplots -> 1 row, 3 columns
# Create bar plots in subplots
age_graph = age.plot(age['Unnamed: 0'], kind = 'bar', 
                     rot = 0, color = 'black', legend = False, ax=axes[0], title = 'A',
                     fontsize = 10)
age_graph.set_ylim([0,40])
age_graph.set_xlabel('Age Group')
age_graph.set_ylabel('Age Distribution')
mortality_graph = mortality.plot(mortality[0], 
                                 kind = 'bar', rot = 0, color = 'black', 
                                 legend = False, ax=axes[1], title = 'B',
                                 fontsize = 10)
mortality_graph.set_ylim([0,80])
mortality_graph.set_xlabel('Age Group')
mortality_graph.set_ylabel('Mortality Rate per 1,000 population')
life_expectancy_graph = life_expectancy.plot(life_expectancy[0], kind = 'bar', rot = 0, 
                                             color = 'black', legend = False,
                                             ax=axes[2], title = 'C', fontsize = 10)
life_expectancy_graph.set_ylim([0,80])
life_expectancy_graph.set_xlabel('Age Group')
life_expectancy_graph.set_ylabel('Life Expectancy')
plt.tight_layout() # Ensure tight layout so labels are not cut off
plt.savefig('Population.pdf')

