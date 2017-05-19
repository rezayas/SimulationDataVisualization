# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 18:13:37 2016

@author: arif

input: data = MeningitisCases.txt: weekly Meningitis Cases
Step 1. Compute Fourier transform on data (as fourier) and amplitudes (as amplitudes)
Step 2. Compute periods (as periods)
Step 3. Identify the Significant Periods of amplitudes (as thresholded_amplitudes)
Step 4. Truncate periods (upto truncateValue=24) and thresholded_amplitudes
Step 5. Plot periods (xaxis) vs thresholded_amplitudes (yaxis)

"""
import numpy as np
import math
from matplotlib import pyplot as plt


# ==========================================================================================

def complexToAmplitude(myList = []):    # myList = list of complex numbers obtained from np.fft.rfft
    amps = []
    for number in myList:
        x2 = math.pow(number.real, 2)
        y2 = math.pow(number.imag, 2)
        sqrt = 2 * math.sqrt (x2 + y2)
    #    print x2, y2, sqrt
        amps.append (int(sqrt))   # convert amplitudes from floats to ints, save
    return amps

# ==========================================================================================
# Step 1. Compute Fourier transform on data (as fourier) and amplitudes (as amplitudes)

inputFile = 'NigerFiveDistrictsTotalWeeklyCases.txt'
data = np.genfromtxt(inputFile, usecols=(0), dtype=int)
fourier = np.fft.rfft(data) # get 1-dimensional real FFT; = orig_cvalued_fft
#print 'rf = ', rf

realDataAverage = np.mean(data)
realDataSD = np.std(data)

print 'len(data) =', len(data), 'realDataAverage=', realDataAverage, 'realDataSD=', realDataSD
print 'len(fourier) =', len(fourier), '\n'   # got: 728, 365

# amplitude[i] = 2 * Math.Sqrt(Math.Pow(data[i].x, 2) + Math.Pow(data[i].y, 2));
amplitudes = complexToAmplitude (fourier)
# in the following, we need to ignore/remove the 1st items in amplitudes
amplitudes.pop(0) # remove the first item from amplitudes
print 'amplitudes:', amplitudes, 'len:', len(amplitudes), '\n'

# ==========================================================================================
# Step 2. Compute periods (as periods)

periods = []
for k in range(len(amplitudes)):
    if k != 0:
        period = len(data) / k
        # print 'index', k, ' : period', period
        periods.append(period)
# remove the first item from periods; then, copy the last item as a new item, appending it at the last (just to keep the sizes same)
periods.pop(0), periods.append(periods[len(periods)-1])
print 'periods:', periods, 'len:', len(periods)

# ==========================================================================================
# Step 3. Bootstrap: Identify the Significant Periods of amplitudes (as thresholded_amplitudes)

#len_amplitudes = len(amplitudes)
num_shuffles = 1000  # number of re-samples (shuffles)
amplitudes2D = [[0 for x in range(len(amplitudes))] for y in range(num_shuffles)]
temp_data = []
#print amplitudes2D   # a [len] x [num_shuffles] 2D array to store temp amplitudes

import random
# amplitudes2D: each row = 1 shuffle of entire amplitudes[]
# amplitudes2D: each col = n shuffled values of a single amplitude
for i in range(num_shuffles): # i = for each row
#    print 'Shuffle', (i+1), '... ',
#    random.shuffle(data) # changes the list in place 
    temp_data = random.sample(data, len(data))  # create a new randomly-shuffled list (don't change the existing one)
#    print 'Shuffle', (i+1), 'orig:\n', data
#    print  'shuffled:\n', temp_data
    temp_fourier = np.fft.rfft(temp_data)
#    print 'temp_fourier', (i+1), temp_fourier
    temp_amplitudes = complexToAmplitude (temp_fourier)
    temp_amplitudes.pop(0)
    amplitudes2D[i] = temp_amplitudes
#    print  'temp_amplitudes:\n', amplitudes2D[i], '\n'
#print 'after shuffles, amplitudes:\n', amplitudes2D   # a [len] x [n] 2D array to store temp amplitudes
#print '\nnum_shuffles=', num_shuffles


#print amplitudes2D[3][2] # works as amplitudes2D[i][i]... SA!
# check if amplitudes calculated for the original time-series is greater than 99% of the amplitudes 
# calculated from the n bootstrap samples

thresholded_amplitudes = [] # will store the final, thresholded amplitudes
#print '\n\nSorted amplitudes2D:'
for j in range(len(amplitudes)):
    count = 0
    for i in range(num_shuffles): # i = for each row
        if amplitudes[j] > amplitudes2D[i][j] :
            count += 1
    percentage = float (count) / float (num_shuffles)
#    print 'j =', (j+1), ': amps[j] =', amplitudes[j], ': count =', count, ', % =', percentage
    if percentage > 0.99 :
        thresholded_amplitudes.append(amplitudes[j])    # this amplitude is significant
    else :
        thresholded_amplitudes.append(0)

#print 'Original amplitudes:', amplitudes
print '\nthresholded amplitudes:', thresholded_amplitudes, 'len =', len(thresholded_amplitudes)
# IMPORTANT: since thresholded_amplitudes is coming from temp_amplitudes (already popped(0)), 
# you do NOT need to pop anything from thresholded_amplitudes


# ==========================================================================================
# Step 4. Truncate periods (upto truncateValue=24) and thresholded_amplitudes
# copy first ~52 elements of periods (as long as periods[i] >= truncateValue)
truncate_period_value = 24
periods_truncated = [value for value in periods if value >= truncate_period_value]
print '\nperiods_truncated =', periods_truncated, 'len =', len(periods_truncated)

# now, copy the first len(periods_truncated) elements of thresholded_amplitudes
#thresholded_amplitudes = amplitudes # DELETE it if using shuffle above
amplitudes_truncated = thresholded_amplitudes[:len(periods_truncated)]
print 'amplitudes_truncated =', amplitudes_truncated, 'len =', len(amplitudes_truncated)

## ======================================================================================================
# Step 5. Plot periods (xaxis) vs thresholded_amplitudes (yaxis)

fig = plt.figure(figsize=(24, 6))
plt.xscale('log') # helps to spread out the last few data points on the xaxis
plt.plot(periods_truncated, amplitudes_truncated, 'bo', )

for i, j in zip(periods_truncated, amplitudes_truncated):    
    plt.vlines(i, 0, j, linestyles='-', colors='b') # Plot vertical lines

xmax = np.max(periods_truncated)
xmin = np.min(periods_truncated)
ymax = np.max(amplitudes_truncated)
print '\nfor figure: xmax =', xmax, ', xmin =', xmin, ', ymax =', ymax    # xmax = 728, xmin = 24, ymax = 173820
#digits_in_ymax = len(str(ymax)), print 'digits_in_ymax =', digits_in_ymax  ... do later
plt.axis([xmax + 5, xmin - 1, 0, ymax + 1000]) # get some space at the beginning of xaxis

plt.xlabel(r'Period (Weeks)', fontsize=24, fontweight='bold')
plt.ylabel(r'Coefficient Amplitude', fontsize=24, fontweight='bold')

plt.xticks(periods_truncated, rotation='vertical')
ax = plt.gca()
ax.set_xticklabels(periods_truncated, fontsize=12, fontweight='bold')
ax.yaxis.set_tick_params(labelsize=12)

plt.grid()

#fig.savefig('FourierWithBootstrap_Niger5Districts_WeeklyMeningitisCases_WithA_702Weeks.png', bbox_inches='tight', pad_inches=0.1)

# SA! thisworked with BootStrap! Proof: compare: 
# amplitudeFFT-RY2-BootStrap.png vs. amplitudeFFT-RY2-NOBootStrap.png


# ====================================================================================================================================
# NOTES: =============================================================================================================================

# Plot vertical lines at each x from ymin to ymax: vlines(x, ymin, ymax, colors='k', linestyles='solid')
#    http://matplotlib.org/api/axes_api.html?highlight=vlines#matplotlib.axes.Axes.vlines
#    http://stackoverflow.com/questions/19481427/customising-line-styles-in-python-using-vlines

# how to set unequal x axis intervals in Matplotlib:
# http://stackoverflow.com/questions/8604002/how-to-set-unequal-x-axis-intervals-in-matplotlib