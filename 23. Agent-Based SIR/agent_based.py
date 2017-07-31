# In[1]:

# Load required modules ===============================================================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib as mpl
import sys
reload(sys)
sys.setdefaultencoding('utf8')

# In[2]:

# Load data/Read in CSV files ===============================================================
data_distribution = pd.ExcelFile('Age-distribution of cases - data.xlsx')
data_distribution = data_distribution.parse('Sheet1')
model_distribution = pd.ExcelFile('Age-distribution of cases - model.xlsx')
model_distribution = model_distribution.parse('Sheet1')
data_weekly = pd.ExcelFile('Weekly cases - data.xlsx')
data_weekly = data_weekly.parse('Sheet1')
model_weekly = pd.ExcelFile('Weekly cases - model.xlsx')
model_weekly = model_weekly.parse('Sheet1')
I = pd.ExcelFile('I - model.xlsx')
I = I.parse('Sheet1')
R = pd.ExcelFile('R - model.xlsx')
R = R.parse('Sheet1')
S = pd.ExcelFile('S - model.xlsx')
S = S.parse('Sheet1')

# In[3]:

mpl.style.use('classic') # Use classic MPL layout
fig = plt.figure() # add plot figure
# add sublots with 2 columns and 2 rows
fig.add_subplot(231)
plt.plot(R['Time'], R['Replicate 1'])
plt.plot(R['Time'], R['Replicate 2'])
plt.title('R')
fig.add_subplot(232)
plt.plot(I['Time'], R['Replicate 1'])
plt.plot(I['Time'], R['Replicate 2'])
plt.title('I')
fig.add_subplot(233)
plt.plot(S['Time'], R['Replicate 1'])
plt.plot(S['Time'], R['Replicate 2'])
plt.title('S')
fig.add_subplot(234)
plt.plot(model_weekly['Time'], model_weekly['Replicate 1'])
plt.plot(model_weekly['Time'], model_weekly['Replicate 2'])
plt.title('Model')
ax = fig.add_subplot(235)
x_axis = np.arange(0, 20) # create y-axis coordinates for scatter plot (dataset) points
for i in range(0, len(model_distribution)):
    plt.scatter(x_axis[i], model_distribution['Replicate 1'][i], marker = '_', color = '#C74EFF') # plot a scatter plot with dataset values
    plt.scatter(x_axis[i], model_distribution['Replicate 2'][i], marker = '_', color = '#C74EFF') # plot a scatter plot with dataset values
ax.set_xticklabels(model_distribution['Age'],  fontsize = 5)
y_labels = ax.get_yticklabels()
ax.set_yticklabels(y_labels, fontsize = 5)
plt.savefig('Agent-BASED.pdf')
