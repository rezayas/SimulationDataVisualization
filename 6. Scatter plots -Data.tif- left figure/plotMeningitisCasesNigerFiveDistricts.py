# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 18:56:34 2016

@author: arif
"""
import numpy as np
import matplotlib.pyplot as plt
import os

float_formatter = lambda x: "%.2f" % x

# This is for real plot of NigerFiveDistrictsTotal.txt ================================================================
inputFile = 'NigerFiveDistrictsTotal.txt' #sys.argv[1] # command line argument
print 'Inputfile: ', inputFile
pathname = os.path.dirname(inputFile)

meningitisCases = np.genfromtxt(inputFile, usecols=(0), dtype=int)  # , skip_header=53
average = np.average(meningitisCases)
maximum = np.max(meningitisCases)

fig = plt.figure(figsize=(24, 8))
ax = fig.add_subplot(111)
plt.plot(meningitisCases, label='Niger 5 Districts Total', linewidth=2)
print 'input.size =', meningitisCases.size, '=', (meningitisCases.size/52), 'years'

# Adjust x-axis parameters ==============================================================
ax.set_xlim(1, meningitisCases.size + 1.0)
ax.set_xticks(np.arange(1, meningitisCases.size + 52.0, 52.0)) # set xticks in yearly intervals; this = eg 1-60years data ("year0-1" omitted)
#ax.set_xticklabels(np.arange(1, 21, 1)) # set xticklabels in yearly intervals (omit "year0-1" interval; print years 1...19)
ax.set_xticklabels(np.arange(2002, 2002 + (meningitisCases.size/52) + 2, 1)) # set xticklabels in yearly intervals (print years 1...max_year)
plt.xlabel(r'Year', fontsize=16, fontweight='bold')

# Adjust y-axis parameters ==============================================================
#yticks = np.arange(0, 24, 2)
#plt.yticks(yticks)
# Adjust y-axis parameters ==============================================================
max_val = 60
y_interval = 5.0
#y_top_margin = 5.0
ax.set_ylim(0, max_val)
ax.set_yticks(np.arange(0.0, max_val + y_interval, y_interval)) # set yticks in 0.1 intervals
ax.set_yticklabels(np.arange(0, max_val + y_interval, y_interval)) # set yticklabels
plt.ylabel(r'Meningitis Cases', fontsize=16, fontweight='bold')

# Add average text
textstr = "average Niger5D = %0.2f\nmax = %0.2f" % (average, maximum)
print 'Niger5D meningitisCases: average =', float_formatter(average), 'maximum =', maximum
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
ax.text(0.02, 0.5, textstr, transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props) # average text

# Adjust Plot parameters ==============================================================
#plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.grid()
    
# Save output file =======================================
# name output file after inputFile (omit extension)
filenameWithoutExtension, file_extension = os.path.splitext(inputFile)
outputfileName = os.path.basename(filenameWithoutExtension) + "_WithAverage.png"
outputDirectory = os.path.abspath(pathname)
outputfile = os.path.join(outputDirectory, outputfileName)
fig.savefig(outputfile, bbox_inches='tight', pad_inches=0.1)
print 'Figure saved as:', outputfile
