# In[1]:

# Load required modules ===============================================================
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.lines as mlines
import matplotlib.patches as mpatches
import statsmodels.api as sm

outcomes = None
analysis = None
annual = None
unintended = None
risk = None
success = None
alcohol = None
exposure = None
pathways = None
drank = None
drank_non = None
sex_non = None
probabilities = None

# In[2]:
# Load data/Read in CSV files ===============================================================
def read(_file):
    global outcomes, analysis, annual, unintended, risk, success, alcohol, exposure, pathways, drank, drank_non, sex_non, probabilities

    combined = pd.ExcelFile(_file)

    outcomes = combined.parse('Outcomes')
    outcomes.columns = outcomes.iloc[0] # Rename column headers
    outcomes = outcomes[1:] # Delete extra column heads

    analysis = combined.parse('Analysis')
    analysis.columns = analysis.iloc[0] # Rename column headers
    analysis = analysis[1:] # Delete extra column heads

    annual = outcomes.iloc[0:10, 1:7]
    unintended = outcomes.iloc[0:10, 9:17].dropna()
    risk = outcomes.iloc[0:10, 20:26] * 100 # Convert to percentages
    success = outcomes.iloc[0:10, 28:36] * 100
    alcohol = outcomes.iloc[0:10, 39:46] * 100
    exposure = outcomes.iloc[0:10, 50:57].dropna() * 100
    pathways = outcomes.iloc[0:10, 59:63].dropna() * 100
    drank = outcomes.iloc[0:10, 66:72].dropna() * 100
    drank_non = outcomes.iloc[0:10, 75:82] * 100
    sex_non = outcomes.iloc[0:10, 85:92] * 100
    probabilities = outcomes.iloc[0:15, 95:101].dropna() * 100

# In[3]:
# Plot validation model ===============================================================
def plot_validation(_output):
    global outcomes, analysis, annual, unintended, risk, success, alcohol, exposure, pathways, drank, drank_non, sex_non, probabilities

    mpl.style.use('classic') # Use classic MPL layout
    fig = plt.figure() # add plot figure

    # Unintended pregnancies plot
    fig.add_subplot(223)
    plt.title('C)', loc = 'left', fontsize = '10')
    plt.bar(range(1,9), unintended.iloc[0, 0:10], align = 'center', color = 'orange')
    plt.errorbar(range(1,9), unintended.iloc[1, 0:10], # Plot the error bar
                 np.array([unintended.iloc[4, 0:10], unintended.iloc[5, 0:10]]), fmt = 'o',
                 markersize = 4)
    plt.xticks(range(1,9), list(unintended.columns.values), rotation='vertical', fontsize = 8)
    plt.xlim([0, 9])
    plt.ylim([0,40])
    circle = mlines.Line2D([],[], marker='o',
                            markerfacecolor="blue", label = 'Model - Median') # Make a circle for the legend
    cdc = mpatches.Patch(color='orange', label='CDC') # Make an orange square
    plt.legend(handles = [cdc, circle], numpoints = 1, # Plot the legend
               prop={'size':5}, loc = 2)
    plt.title('Annual Unintended Pregnancies \n(Per 100 Women)', fontsize = 8)

    # Successful pregnancies plot
    fig.add_subplot(222)
    plt.title('B)', loc = 'left', fontsize = '10')
    plt.bar(range(1,7), success.iloc[0, 1:7], 0.35, color='orange',
           yerr=np.array([success.iloc[3, 1:7],success.iloc[4, 1:7]]),
           error_kw=dict(ecolor='red'))
    plt.bar(np.array(range(1,7)) + 0.35, success.iloc[5, 1:7], 0.35, color='#d5deec',
           yerr=np.array([success.iloc[8, 1:7], success.iloc[9, 1:7]]),
           error_kw=dict(ecolor='blue'))
    plt.xticks(range(1,7), list(success.columns.values)[1:7], fontsize = 8)
    plt.xlim(0, 7.2)
    plt.ylim(0,20)
    plt.xticks(np.array(range(1,7)) + 0.35)
    median = mpatches.Patch(color='#d5deec', label = 'Model - Median')
    cdc = mpatches.Patch(color='orange', label='CDC')
    plt.legend(handles = [cdc, median], numpoints = 1,
               prop={'size':5}, loc = 2)
    plt.title('Age Distribution of Successful Pregnancies', fontsize = 7)

    # Successful pregnancies plot
    fig.add_subplot(221)
    plt.title('A)', loc = 'left', fontsize = '10')
    plt.bar(range(1,7), risk.iloc[0, 0:7], color='orange')
    plt.errorbar(np.array(range(1,7)) + 0.4, risk.iloc[5, 0:7],
                np.array([risk.iloc[8, 0:7], risk.iloc[9, 0:7]]), fmt='o', ecolor = 'blue',
                markersize = 4)
    risk.columns.values[4] = 'Seeking\nPregnancy'
    plt.xticks(np.array(range(1,7)) + 0.4, list(risk.columns.values)[0:7], fontsize = 5)
    plt.xlim(0, 7.4)
    plt.ylim(0,50)
    circle = mlines.Line2D([],[], marker='o',
                            markerfacecolor="blue", label = 'Model') # Make a circle for the legend
    cdc = mpatches.Patch(color='orange', label='Survey')
    plt.legend(handles = [cdc, circle], numpoints = 1,
               prop={'size':5}, loc = 2)
    plt.title('Distribution in Risk Behaviour Groups', fontsize = 7)

    # Alcohol Risk plot
    fig.add_subplot(224)
    plt.title('D)', loc = 'left', fontsize = '10')
    plt.bar(range(1,8), alcohol.iloc[0, 0:7], color='orange',
           yerr=np.array([alcohol.iloc[3, 0:7],alcohol.iloc[4, 0:7]]),
           error_kw=dict(ecolor='red'))
    plt.errorbar(np.array(range(1,8)) + 0.4, alcohol.iloc[5, 0:7],
                np.array([alcohol.iloc[8, 0:7], alcohol.iloc[9, 0:7]]), fmt='o', ecolor = 'blue',
                markersize = 4)
    plt.xticks(np.array(range(1,8)) + 0.4, list(alcohol.columns.values)[0:7], fontsize = 8)
    plt.xlim(0, 8.4)
    plt.ylim(0,20)
    circle = mlines.Line2D([],[], marker='o',
                            markerfacecolor="blue", label = 'Model - Median') # Make a circle for the legend
    cdc = mpatches.Patch(color='orange', label='CDC')
    plt.legend(handles = [cdc, circle], numpoints = 1,
               prop={'size':5}, loc = 2)
    plt.title('Risk of Alcohol Exposed Pregnancy', fontsize = 7)
    plt.tight_layout()
    plt.savefig(_output + '.pdf', bbox_inches='tight')

# In[4]:
# Plot validation model ===============================================================
def plot_aep(_output):
    global outcomes, analysis, annual, unintended, risk, success, alcohol, exposure, pathways, drank, drank_non, sex_non, probabilities

    mpl.style.use('classic')
    fig = plt.figure(figsize=(9,4))

    # Exposure plot
    fig.add_subplot(121)
    plt.title('A)', loc = 'left', fontsize = 12)
    plt.errorbar(np.array(range(1,8)), exposure.iloc[0, 0:7],
                np.array([exposure.iloc[3, 0:7], exposure.iloc[4, 0:7]]), fmt='o')
    plt.xticks(np.array(range(1,8)), list(exposure.columns.values)[0:7], fontsize = 6)
    plt.xlim(0, 8)
    plt.ylim(0,120)
    plt.title('Percentage Pregnancies Exposed to Alcohol', fontsize = 9)

    # Pathways plot
    fig.add_subplot(122)
    plt.title('B)', loc = 'left', fontsize = 12)
    pathways.columns.values[3] = 'Drinking while\nAware of\nPregnancy'
    pathways.columns.values[2] = 'Contraception\nFailure'
    plt.errorbar(np.array(range(1,5)), pathways.iloc[0, 0:4],
                np.array([pathways.iloc[3, 0:4], pathways.iloc[4, 0:4]]), fmt='o')
    plt.xticks(np.array(range(1,5)), list(pathways.columns.values)[0:4], fontsize = 5)
    plt.xlim(0, 5)
    plt.ylim(0, 80)
    plt.title('Pathways to an Alcohol-Exposed Pregnancy', fontsize = 9)

    plt.tight_layout()
    plt.savefig(_output + '.pdf', bbox_inches='tight')

# In[5]:
# Plot extra validation figures ===============================================================
def add_validation(_output):
    global outcomes, analysis, annual, unintended, risk, success, alcohol, exposure, pathways, drank, drank_non, sex_non, probabilities

    mpl.style.use('classic')
    fig = plt.figure()

    # Percentage drank plot
    fig.add_subplot(221)
    plt.title('A)', loc = 'left', fontsize = '15')
    plt.bar(range(1,7), drank.iloc[0, 0:6], color='orange',
           yerr=np.array([drank.iloc[3, 0:6], drank.iloc[4, 0:6]]),
           error_kw=dict(ecolor='red'))
    plt.errorbar(np.array(range(1,7)) + 0.4, drank.iloc[5, 0:6],
                np.array([drank.iloc[8, 0:6], drank.iloc[9, 0:6]]), ecolor = 'blue',
                fmt = 'o', markersize = 4)
    drank.columns.values[4] = 'Seeking\nPregnancy'
    plt.xticks(np.array(range(1,7)) + 0.4, list(drank.columns.values)[0:6], fontsize = 5)
    plt.xlim(0, 7.4)
    plt.ylim(0, 100)
    circle = mlines.Line2D([],[], marker='o',
                            markerfacecolor="blue", label = 'Model') # Make a circle for the legend
    cdc = mpatches.Patch(color='orange', label='Survey')
    plt.legend(handles = [cdc, circle], numpoints = 1,
               prop={'size':5}, loc = 2)
    plt.title('Percentage Drank Last Month', fontsize = 9)

    # Percentage drank last month plot
    fig.add_subplot(222)
    plt.title('B)', loc = 'left', fontsize = '15')
    plt.bar(range(1,7), drank_non.iloc[0, 0:6], color='orange',
           yerr=np.array([drank_non.iloc[3, 0:6], drank_non.iloc[4, 0:6]]),
           error_kw=dict(ecolor='red'))
    plt.errorbar(np.array(range(1,7)) + 0.4, drank_non.iloc[5, 0:6],
                np.array([drank_non.iloc[8, 0:6], drank_non.iloc[9, 0:6]]), ecolor = 'blue',
                fmt = 'o', markersize = 4)
    plt.xticks(np.array(range(1,7)) + 0.4, list(drank_non.columns.values)[0:6], fontsize = 8)
    plt.xlim(0, 7.5)
    plt.ylim(0, 80)
    circle = mlines.Line2D([],[], marker='o',
                            markerfacecolor="blue", label = 'Model') # Make a circle for the legend
    cdc = mpatches.Patch(color='orange', label='CDC')
    plt.legend(handles = [cdc, circle], numpoints = 1,
               prop={'size':5}, loc = 2)
    plt.title('Percentage Drank Last Month\n(Nonpregnant, Nonsterile)', fontsize = 9)

    # Percentage had sex last month plot
    fig.add_subplot(223)
    plt.title('C)', loc = 'left', fontsize = '15')
    plt.bar(range(1,7), sex_non.iloc[0, 0:6], color='orange',
           yerr=np.array([sex_non.iloc[3, 0:6], sex_non.iloc[4, 0:6]]),
           error_kw=dict(ecolor='red'))
    plt.errorbar(np.array(range(1,7)) + 0.4, sex_non.iloc[5, 0:6],
                np.array([sex_non.iloc[8, 0:6], sex_non.iloc[9, 0:6]]), ecolor = 'blue',
                fmt = 'o', markersize = 4)
    plt.xticks(np.array(range(1,7)) + 0.4, list(sex_non.columns.values)[0:6], fontsize = 8)
    plt.xlim(0, 7.4)
    plt.ylim(0, 60)
    circle = mlines.Line2D([],[], marker='o',
                            markerfacecolor="blue", label = 'Model') # Make a circle for the legend
    cdc = mpatches.Patch(color='orange', label='CDC')
    plt.legend(handles = [cdc, circle], numpoints = 1,
               prop={'size':5}, loc = 2)
    plt.title('Percentage Had Sex Last Month\n(Nonpregnant, Nonsterile, No Contraception)', fontsize = 9)

    # Annual birth rate
    fig.add_subplot(224)
    plt.title('D)', loc = 'left', fontsize = '15')
    plt.bar(range(1,7), annual.iloc[0, 0:6], color='orange')
    plt.errorbar(np.array(range(1,7)) + 0.4, annual.iloc[5, 0:6],
                np.array([annual.iloc[8, 0:6], annual.iloc[9, 0:6]]), ecolor = 'blue',
                fmt = 'o', markersize = 4)
    plt.xticks(np.array(range(1,7)) + 0.4, list(annual.columns.values)[0:6], fontsize = 8)
    plt.xlim(0, 7.4)
    plt.ylim(0, 140)
    circle = mlines.Line2D([],[], marker='o',
                            markerfacecolor="blue", label = 'Model') # Make a circle for the legend
    cdc = mpatches.Patch(color='orange', label='CDC')
    plt.legend(handles = [cdc, circle], numpoints = 1,
               prop={'size':5}, loc = 2)
    plt.title('Annual Birth Rate (Per 1,000 Women)', fontsize = 9)
    plt.tight_layout()
    plt.savefig(_output + '.pdf', bbox_inches='tight')

# In[6]:
# Plot Population Distribution ===============================================================
def plot_distribution(_output):
    global outcomes, analysis, annual, unintended, risk, success, alcohol, exposure, pathways, drank, drank_non, sex_non, probabilities

    mpl.style.use('classic')
    fig = plt.figure()
    for i in range(6):
        fig.add_subplot(231 + i)
        plt.bar(range(1,7), probabilities.iloc[0:6, i], 0.35, color='orange')
        plt.bar(np.array(range(1,7)) + 0.35, probabilities.iloc[8:14, i], 0.35, color='blue')
        plt.xticks(range(1,7), ['Sterile', 'Inactive', 'Careful Sex', 'Unsafe Sex',
                    'Seeking Pregnancy', 'Pregnant'], fontsize = 8, rotation = 'vertical')
        plt.xlim(0, 7.2)
        plt.ylim(0,80)
        plt.yticks(fontsize = 7)
        plt.xticks(np.array(range(1,7)) + 0.35)
        median = mpatches.Patch(color='blue', label = 'Model')
        cdc = mpatches.Patch(color='orange', label='Survey')
        plt.legend(handles = [cdc, median], numpoints = 1,
                   prop={'size':5}, loc = 2)
        plt.title('Age ' + probabilities.columns[i], fontsize = 7)

        plt.tight_layout()
        plt.savefig(_output + '.pdf', bbox_inches='tight')

# In[6]:
# Plot Regression line ===============================================================
def plot_regression(_output):
    global outcomes, analysis, annual, unintended, risk, success, alcohol, exposure, pathways, drank, drank_non, sex_non, probabilities

    mpl.style.use('classic')
    fig = plt.figure()
    x = np.arange(0, 125, 25)
    y = analysis.iloc[1, 0:5]
    fit = np.polyfit(x, y, 1)
    fit_function = np.poly1d(fit)
    plt.plot(x, y, 'o', x, fit_function(x), color = 'orange')

    y = analysis.iloc[1, 6:11] * 100
    fit = np.polyfit(x, y, 1)
    fit_function = np.poly1d(fit)
    plt.plot(x, y, 'o', x, fit_function(x), color = 'blue')
    plt.xlim(0, 100)
    plt.ylim(0, 50)
    circle1 = mlines.Line2D([],[], marker='o',
                            markerfacecolor="orange", label = 'AEP Risk (CDC Definition)') # Make a circle for the legend
    circle2 = mlines.Line2D([],[], marker='o',
                            markerfacecolor="blue", label = 'AEP Prevalence') # Make a circle for the legend
    plt.legend(handles = [circle1, circle2], numpoints = 1,
               prop={'size':10}, loc = 2)
    plt.title('Compliance with CDC Recommendation')
    plt.tight_layout()
    plt.savefig(_output + '.pdf')
