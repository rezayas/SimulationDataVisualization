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
# Take out the relevant age groups
model_distribution = model_distribution[0:5]
data_distribution = data_distribution[0:5]

# In[3]:

# Plot the graphs ===============================================================
mpl.style.use('classic') # Use classic MPL layout
fig = plt.figure() # add plot figure
fig.add_subplot(233)
# Plot all columns for R
for i in range(1, len(R.columns)):
    plt.plot(R['Time'], R.iloc[:, i], color = '#787878')
plt.xlabel('Time')
plt.title('R')
fig.add_subplot(232)
# Plot all columns for I
for i in range(1, len(I.columns)):
    plt.plot(I['Time'], I.iloc[:, i], color = '#787878')
plt.xlabel('Time')
plt.title('I')
fig.add_subplot(231)
# Plot all columns for S
for i in range(1, len(S.columns)):
    plt.plot(S['Time'], S.iloc[:, i], color = '#787878')
plt.xlabel('Time')
plt.title('S')
fig.add_subplot(234)
# Plot all columns for weekly data and overlay model
for i in range(1, len(model_weekly.columns)):
    plt.plot(model_weekly['Time'], model_weekly.iloc[:, i], color = '#787878')
for i in range(1, len(data_weekly.columns)):
    plt.plot(data_weekly['Time'], data_weekly.iloc[:, i], color = 'black',
             linewidth = '2', marker = 'o', markersize = '5')
plt.xlabel('Time')
plt.title('Model')
ax = fig.add_subplot(235)
x_axis = np.arange(1, 6) # create y-axis coordinates for scatter plot (dataset) points
# Plot all columns for age distribution data
for i in range(0, len(model_distribution)):
    for j in range(1, len(model_distribution.columns)):
        plt.scatter(x_axis[i], model_distribution.iloc[:, j][i], marker = '_', color = '#C74EFF', s = 200) # plot a scatter plot with dataset values
        plt.scatter(x_axis[i], data_distribution['%'][i], marker = '_', color = '#C74EFF', s = 200) # plot a scatter plot with dataset values
ax.set_xticks(x_axis)
ax.set_xticklabels(model_distribution['Age'],  fontsize = 6)
plt.yticks(fontsize = 6)
plt.xlabel('Age Group')
plt.ylabel('Age Distribution')
plt.title('Distribution')
plt.tight_layout()
plt.savefig('Agent-BASED.pdf')
