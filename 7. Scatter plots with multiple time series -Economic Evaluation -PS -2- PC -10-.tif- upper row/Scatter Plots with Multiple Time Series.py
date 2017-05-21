
# coding: utf-8

# In[1]:

# Load required modules ===============================================================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import matplotlib as mpl


# In[2]:

# Load data/Read in CSV files ===============================================================
best = pd.read_csv('(PS $2, PC $10)CEA - Best (PS $4, PC $4).csv')
worse = pd.read_csv('(PS $2, PC $10)CEA - Worse (PS $4, PC $4).csv')


# In[3]:

# Transform the data ===============================================================
# Get the y-values for variables (with strain replacement)
worse_prevention_1 = worse[['dQALY','Prevention 1']]
worse_prevention_1 = worse_prevention_1.dropna(axis=0, how='any') # Drop all NA values
worse_prevention_2 = worse[['dQALY','Prevention 2']]
worse_prevention_2 = worse_prevention_2.dropna(axis=0, how='any')
worse_base_prime = worse[['dQALY','Base Prime']]
worse_base_prime = worse_base_prime.dropna(axis=0, how='any')
worse_wtp = worse[['dQALY','WTP of 1 GDP Per Capita']]
worse_wtp = worse_wtp.dropna(axis=0, how='any')
worse_frontier = worse[['dQALY','Frontier']]
worse_frontier = worse_frontier.dropna(axis=0, how='any')
worse_points = worse[['dQALY','Unnamed: 0', 'Centers']]
worse_points = worse_points.dropna(axis=0, how='any')
# Get the y-values for variables (with no strain replacement)
best_prevention_1 = best[['dQALY','Prevention 1']]
best_prevention_1 = best_prevention_1.dropna(axis=0, how='any')
best_prevention_2 = best[['dQALY','Prevention 2']]
best_prevention_2 = best_prevention_2.dropna(axis=0, how='any')
best_base_prime = best[['dQALY','Base Prime']]
best_base_prime = best_base_prime.dropna(axis=0, how='any')
best_wtp = best[['dQALY','WTP of 1 GDP Per Capita']]
best_wtp = best_wtp.dropna(axis=0, how='any')
best_frontier = best[['dQALY','Frontier']]
best_frontier = best_frontier.dropna(axis=0, how='any')
best_points = best[['dQALY','Unnamed: 0', 'Centers']]
best_points = best_points.dropna(axis=0, how='any')


# In[4]:

# With Strain Replacement Plot ===============================================================
mpl.style.use('classic') # Use classic MPL layout
 # Make the scatter plots
worse_base_prime.graph = plt.scatter(worse_base_prime['dQALY'],
                                     worse_base_prime['Base Prime'],
                                     c='#FDB4AB', s=50, alpha = 0.6)
worse_prevention_1.graph = plt.scatter(worse_prevention_1['dQALY'],
                                       worse_prevention_1['Prevention 1'],
                                       c='#C2FEC2', s=50, alpha = 0.6)
worse_prevention_2.graph = plt.scatter(worse_prevention_2['dQALY'],
                                       worse_prevention_2['Prevention 2'],
                                       c='#C1C2FD', s=50, alpha = 0.6)
# Plot the frontier and centers
plt.plot(worse_frontier['dQALY'], worse_frontier['Frontier'],
         color = 'black', alpha = 0.6, linewidth = 3)
plt.scatter(worse_points['dQALY'], worse_points['Centers'], c='black', marker='x', s=100, linewidth = 3)
# Plot the annotating arrows and text
plt.annotate('Prevention 1', xy=(worse_points['dQALY'][1],
                                 worse_points['Centers'][1]),
             xytext=(1000, -10), arrowprops=dict(facecolor='black',
                                                 shrink=0.05, width = 1))
plt.annotate('Prevention 2', xy=(worse_points['dQALY'][2],
                                 worse_points['Centers'][2]),
            xytext=(40000, -5), arrowprops=dict(facecolor='black', shrink=0.05, width = 1))
plt.annotate('Base Prime', xy=(worse_points['dQALY'][3],
                               worse_points['Centers'][3]),
             xytext=(1000, 20), arrowprops=dict(facecolor='black', shrink=0.05, width = 1))
m, b = np.polyfit(worse_wtp['dQALY'], worse_wtp['WTP of 1 GDP Per Capita'], 1) # get regression line fit for WTP
wtp = plt.plot(np.array([-12500,62500]), m*np.array([-12500,62500]) + b,
               ls = '--', color = 'black') # plot the WTP regression line
plt.xlim([-12500,62500])
plt.ylim([-15,25])
plt.axvline(x=0, color='black', ls=':')
plt.axhline(y=0, color='black', ls=':')
plt.xlabel('Additional DALY Averted Per Year')
plt.ylabel('Additional Annual Cost (Million)')
plt.title('Assuming Strain Replacement')
line_handle = mlines.Line2D([], [], color='black', ls='-') # get a legend handle for a black line
plt.fill_between(np.array([-12500,62500]),  m*np.array([-12500,62500]) + b,
                 -999999, color='#F9E7DB', zorder = 0) # shade bounded area beige
plt.legend((worse_base_prime.graph, worse_prevention_1.graph, worse_prevention_2.graph, line_handle),
           ('Base Prime', 'Prevention 1', 'Prevention 2', 'Frontier'),
           loc = 4, prop={'size':7}, scatterpoints = 1)
plt.tight_layout()  # Ensure tight layout so legend/labels are not cut off
plt.savefig('Economic Evaluation (PS $2, PC $10) ~ Worse.pdf') # Save plot to PDF


# In[5]:

# With No Strain Replacement Plot (code modified from above) ===============================================================
best_base_prime.graph = plt.scatter(best_base_prime['dQALY'],
                                     best_base_prime['Base Prime'], c='#FDB4AB', s=50, alpha = 0.6)
best_prevention_1.graph = plt.scatter(best_prevention_1['dQALY'],
                                       best_prevention_1['Prevention 1'], c='#C2FEC2', s=50, alpha = 0.6)
best_prevention_2.graph = plt.scatter(best_prevention_2['dQALY'],
                                       best_prevention_2['Prevention 2'], c='#C1C2FD', s=50, alpha = 0.6)
plt.plot(best_frontier['dQALY'], best_frontier['Frontier'], color = 'black', alpha = 0.6, linewidth = 3)
plt.scatter(best_points['dQALY'], best_points['Centers'], c='black', marker='x', s=100,  linewidth = 3)
plt.annotate('Prevention 1', xy=(best_points['dQALY'][1],
                                 best_points['Centers'][1]),
             xytext=(1000, -10), arrowprops=dict(facecolor='black', shrink=0.05, width = 1))
plt.annotate('Prevention 2', xy=(best_points['dQALY'][2],
                                 best_points['Centers'][2]),
            xytext=(40000, -5), arrowprops=dict(facecolor='black', shrink=0.05, width = 1))
plt.annotate('Base Prime', xy=(best_points['dQALY'][3],
                               best_points['Centers'][3]),
             xytext=(1000, 20), arrowprops=dict(facecolor='black', shrink=0.05, width = 1))
m, b = np.polyfit(best_wtp['dQALY'], best_wtp['WTP of 1 GDP Per Capita'], 1)
wtp = plt.plot(np.array([-12500,62500]), m*np.array([-12500,62500]) + b, ls = '--', color = 'black')
plt.xlim([-12500,62500])
plt.ylim([-15,25])
plt.axvline(x=0, color='black', ls=':')
plt.axhline(y=0, color='black', ls=':')
plt.xlabel('Additional DALY Averted Per Year')
plt.ylabel('Additional Annual Cost (Million)')
plt.title('Assuming No Strain Replacement')
line_handle = mlines.Line2D([], [], color='black', ls='-')
plt.fill_between(np.array([-12500,62500]),  m*np.array([-12500,62500]) + b, -999999, color='#F9E7DB', zorder = 0)
plt.legend((best_base_prime.graph, best_prevention_1.graph, best_prevention_2.graph, line_handle),
           ('Base Prime', 'Prevention 1', 'Prevention 2', 'Frontier'),
           loc = 4, prop={'size':7}, scatterpoints = 1)
plt.tight_layout()
plt.savefig('Economic Evaluation (PS $2, PC $10) ~ Best.pdf')
