
# coding: utf-8

# In[1]:

# Load required modules ===============================================================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl


# In[2]:

# Load data/Read in CSV files ===============================================================
best = pd.read_csv('Model - Cases (Best) Scattered.csv')
worst = pd.read_csv('Model - Cases (Worse) Scattered.csv')


# In[3]:

# No Strain Replacement Plot ===============================================================
mpl.style.use('classic') # Use classic MPL layout
y_axis = np.arange(0, 4*(len(best.columns) - 1), 4) # create y-axis coordinates for scatter plot (dataset) points
y_values = [y_axis[0]] * len(best) # get the first y-axis value
plt.scatter(best.iloc[:,0], y_values, s=500, marker = '|', color = '#C74EFF') # plot a scatter plot with dataset values
                                                                              # and corresponding y-values
y_values = [y_axis[1]] * len(best)
plt.scatter(best.iloc[:,1], y_values, s=500, marker = '|', color = '#C74EFF')
y_values = [y_axis[2]] * len(best)
plt.scatter(best.iloc[:,2], y_values, s=500, marker = '|', color = '#C74EFF')
y_values = [y_axis[3]] * len(best)
plt.scatter(best.iloc[:,3], y_values, s=500, marker = '|', color = '#C74EFF')
# Plot mean lines for variables
plt.scatter(np.mean(best.iloc[:,3]), y_axis[3],
            color = '#751698', marker='|', s = 1000, linewidth = 3, zorder = 10)
plt.scatter(np.mean(best.iloc[:,2]), y_axis[2],
            color = '#751698', marker='|', s = 1000, linewidth = 3, zorder = 10)
plt.scatter(np.mean(best.iloc[:,1]), y_axis[1],
            color = '#751698', marker='|', s = 1000, linewidth = 3, zorder = 10)
plt.scatter(np.mean(best.iloc[:,0]), y_axis[0],
            color = '#751698', marker='|', s = 1000, linewidth = 3, zorder = 10)
plt.axvline(x=np.mean(best.iloc[:,3]), color='black', ls=':') # Plot main mean line
plt.xticks([0,np.mean(best.iloc[:,3]),10000,20000]) # Add mean tick to plot
plt.yticks(y_axis, ('Elimination 2', 'Elimination 1', 'Base Prime', 'Base'))
plt.xlim([0,20000])
plt.title('Assuming No Strain Replacement')
plt.xlabel('Annual Number of Meningococcal Cases')
plt.tight_layout() # Ensure tight layout so legend/labels are not cut off
plt.savefig('Results – Cases (Best).pdf') # Save plot to PDF


# In[4]:

# With Strain Replacement Plot (Modified code from above) ===============================================================
y_axis = np.arange(0, 4*(len(worst.columns) - 1), 4)
y_values = [y_axis[0]] * len(worst)
plt.scatter(worst.iloc[:,0], y_values, s=500, marker = '|', color = '#C74EFF')
y_values = [y_axis[1]] * len(best)
plt.scatter(worst.iloc[:,1], y_values, s=500, marker = '|', color = '#C74EFF')
y_values = [y_axis[2]] * len(best)
plt.scatter(worst.iloc[:,2], y_values, s=500, marker = '|', color = '#C74EFF')
y_values = [y_axis[3]] * len(best)
plt.scatter(worst.iloc[:,3], y_values, s=500, marker = '|', color = '#C74EFF')
plt.scatter(np.mean(worst.iloc[:,3]), y_axis[3],
            color = '#751698', marker='|', s = 1000, linewidth = 3, zorder = 10)
plt.scatter(np.mean(worst.iloc[:,2]), y_axis[2],
            color = '#751698', marker='|', s = 1000, linewidth = 3, zorder = 10)
plt.scatter(np.mean(worst.iloc[:,1]), y_axis[1],
            color = '#751698', marker='|', s = 1000, linewidth = 3, zorder = 10)
plt.scatter(np.mean(worst.iloc[:,0]), y_axis[0],
            color = '#751698', marker='|', s = 1000, linewidth = 3, zorder = 10)
plt.axvline(x=np.mean(worst.iloc[:,3]), color='black', ls=':')
plt.xticks([0,np.mean(worst.iloc[:,3]),10000,20000])
plt.yticks(y_axis, ('Prevention 2', 'Prevention 1', 'Base Prime', 'Base'))
plt.xlim([0,20000])
plt.title('Assuming Strain Replacement')
plt.xlabel('Annual Number of Meningococcal Cases')
plt.tight_layout()
plt.savefig('Results – Cases (Worse).pdf')


# In[5]:

# Both plots in one panel (Modified code from above) ===============================================================
fig = plt.figure(figsize=[10,5]) # Create figure with x-dimension = 10 and y-dimension = 5
fig.add_subplot(122) # add first subplot
y_axis = np.arange(0, 4*(len(best.columns) - 1), 4)
y_values = [y_axis[0]] * len(best)
plt.scatter(best.iloc[:,0], y_values, s=500, marker = '|', color = '#C74EFF')
y_values = [y_axis[1]] * len(best)
plt.scatter(best.iloc[:,1], y_values, s=500, marker = '|', color = '#C74EFF')
y_values = [y_axis[2]] * len(best)
plt.scatter(best.iloc[:,2], y_values, s=500, marker = '|', color = '#C74EFF')
y_values = [y_axis[3]] * len(best)
plt.scatter(best.iloc[:,3], y_values, s=500, marker = '|', color = '#C74EFF')
plt.scatter(np.mean(best.iloc[:,3]), y_axis[3],
            color = '#751698', marker='|', s = 1000, linewidth = 3, zorder = 10)
plt.scatter(np.mean(best.iloc[:,2]), y_axis[2],
            color = '#751698', marker='|', s = 1000, linewidth = 3, zorder = 10)
plt.scatter(np.mean(best.iloc[:,1]), y_axis[1],
            color = '#751698', marker='|', s = 1000, linewidth = 3, zorder = 10)
plt.scatter(np.mean(best.iloc[:,0]), y_axis[0],
            color = '#751698', marker='|', s = 1000, linewidth = 3, zorder = 10)
plt.axvline(x=np.mean(best.iloc[:,3]), color='black', ls=':')
plt.xticks([0,np.mean(best.iloc[:,3]),10000,20000])
plt.yticks(y_axis, []) # remove ticks from this subplot as it will share a y-axis
plt.xlim([0,20000])
plt.title('Assuming No Strain Replacement')
plt.xlabel('Annual Number of Meningococcal Cases')
fig.add_subplot(121) # add second subplot
y_axis = np.arange(0, 4*(len(worst.columns) - 1), 4)
y_values = [y_axis[0]] * len(worst)
plt.scatter(worst.iloc[:,0], y_values, s=500, marker = '|', color = '#C74EFF')
y_values = [y_axis[1]] * len(best)
plt.scatter(worst.iloc[:,1], y_values, s=500, marker = '|', color = '#C74EFF')
y_values = [y_axis[2]] * len(best)
plt.scatter(worst.iloc[:,2], y_values, s=500, marker = '|', color = '#C74EFF')
y_values = [y_axis[3]] * len(best)
plt.scatter(worst.iloc[:,3], y_values, s=500, marker = '|', color = '#C74EFF')
plt.scatter(np.mean(worst.iloc[:,3]), y_axis[3],
            color = '#751698', marker='|', s = 1000, linewidth = 3, zorder = 10)
plt.scatter(np.mean(worst.iloc[:,2]), y_axis[2],
            color = '#751698', marker='|', s = 1000, linewidth = 3, zorder = 10)
plt.scatter(np.mean(worst.iloc[:,1]), y_axis[1],
            color = '#751698', marker='|', s = 1000, linewidth = 3, zorder = 10)
plt.scatter(np.mean(worst.iloc[:,0]), y_axis[0],
            color = '#751698', marker='|', s = 1000, linewidth = 3, zorder = 10)
plt.axvline(x=np.mean(worst.iloc[:,3]), color='black', ls=':')
plt.xticks([0,np.mean(worst.iloc[:,3]),10000,20000])
plt.yticks(y_axis, ('Prevention 2', 'Prevention 1', 'Base Prime', 'Base'))
plt.xlim([0,20000])
plt.title('Assuming Strain Replacement')
plt.xlabel('Annual Number of Meningococcal Cases')
plt.tight_layout()
plt.savefig('Results – Cases.pdf')
