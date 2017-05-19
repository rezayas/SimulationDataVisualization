# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 13:26:20 2017

@author: arif
"""
import fileinput, glob
import numpy as np
import os, datetime
#import ntpath
import matplotlib.pyplot as plt
import math

# ==========================================================================================

def complexToAmplitude(myList = []):    # myList = list of complex numbers obtained from np.fft.rfft
    amps = []
    for number in myList:
        x2 = math.pow(number.real, 2)
        y2 = math.pow(number.imag, 2)
        sqrt = 2 * math.sqrt (x2 + y2)
        amps.append (int(sqrt))   # convert amplitudes from floats to ints, save
    return amps

# ==========================================================================================
# check if SOME '*.CarriagePrevalence*.txt' file exists; only proceed then; else quit.

allDataCheck = []
countAll = 0
for filename in glob.glob('*.ParametersList*.txt'):     # all runs (both completed and incomplete)
    countAll += 1
    
countCompleted = 0
for filename in glob.glob('*.CarriagePrevalence*.txt'):     # completed runs
    countCompleted += 1

if countCompleted > 0:
    print '\n', 'Completed', countCompleted, 'of', countAll, ' runs... I am proceeding...'

    # COMPUTE CasesAgeGroup ====================================================================================================================
    allDataCasesAgeGroup = [] # CasesAgeGroup
    for filename in glob.glob('*.CasesAgeGroup*.txt'):     # read all data tuples from matching files
        oneFileData = np.loadtxt(fileinput.input(filename))
    #    print oneFileData
#        sumCasesAgeGroup = np.sum(oneFileData) # get the sum of oneFileData
#        averageCasesAgeGroup = np.average(oneFileData)
#        if averageCasesAgeGroup > 0.0000000:
#            percentageCasesAgeGroup = np.multiply ( np.divide (oneFileData, sumCasesAgeGroup), 100.0 ) # normalize and percent
#            myCasesAGFormatted = [ '%.2f' % elem for elem in percentageCasesAgeGroup ]
#        else:
#            myCasesAGFormatted = oneFileData    # keep as is.. probably all are 0.0
    
        # 20170417: myCasesAGFormatted is already calculated by jar
        print 'CasesAG filename:', filename, 'CasesAG:', oneFileData  # debug
        allDataCasesAgeGroup.append (oneFileData)
    
#    print allDataCasesAgeGroup  # debug
    realDataCasesAgeGroup = [2.62, 20.83, 59.88, 13.51, 3.16]   #cases per age group = [2.62, 20.83, 59.88, 13.51, 3.16]
    mymaxCasesAgeGroup = np.max( np.array(allDataCasesAgeGroup).astype(np.float) )  # astype(np.float) : needed to avoid TypeError
    print 'CasesAgeGroup: numInputFiles =', len(allDataCasesAgeGroup), ' allData Max =', mymaxCasesAgeGroup
    
    mediansCasesAgeGroup = [] # Compute median of each ageGroup
    for ageGroupIndex in range(0, 5):   # use list comprehension
        result = [d[ageGroupIndex] for d in allDataCasesAgeGroup]
    #    print 'ageGroupIndex=', ageGroupIndex, result, 'median=', np.median(np.array(result).astype(np.float))
        mediansCasesAgeGroup.append(np.median(np.array(result).astype(np.float)))
    print 'mediansCasesAgeGroup:', mediansCasesAgeGroup, '\n'
    
    # COMPUTE CarriagePrevalence ====================================================================================================================
    allDataCP = [] # CarriagePrevalence
    counter = 0
    for filename in glob.glob('*.CarriagePrevalence*.txt'):     # Read all data tuples from matching files
        allDataCP.append (np.loadtxt(fileinput.input(filename)))
        counter += 1
    
    realDataCP = [1.80, 2.60, 4.90, 3.60, 2.60]
    mymaxCP = np.max(allDataCP)
    print 'CarriagePrevalence: numInputFiles =', len(allDataCP), ' CP Max =', mymaxCP     # counter=numInputFiles .. just checking
    
    mediansCP = [] # Compute median of each ageGroup
    for ageGroupIndex in range(0, 5):   # use list comprehension
        result = [d[ageGroupIndex] for d in allDataCP] # result=all values from index [ageGroupIndex] in allDataCP
        #print 'ageGroupIndex=', ageGroupIndex, result, 'median=', np.median(result)
        mediansCP.append(np.median(result))
    print 'mediansCP:', mediansCP, '\n'
    
    
    # COMPUTE MeningitisCases ====================================================================================================================
    allDataMeningitisCases = [] # MeningitisCases
    allAverageMeningitisCases = [] # array of average of MeningitisCases
    allStandardDeviationMeningitisCases = [] # array of standardDeviation of MeningitisCases
    allCosineOfAngles = [] # array of cosine of angles between realData_modulus and modelData_modulus
    
    # also COMPUTE Fourier on MeningitisCases
    amplitudesRealData = [591, 122, 269, 438, 421, 556, 340, 459, 671, 344, 161, 497, 932, 685, 425, 97, 116, 623, 550, 141, 572, 574, 180, 263, 309, 336, 742, 570, 93, 287, 558, 392, 291, 418, 273, 370, 387, 87, 377, 620, 366, 259, 389, 245, 255, 425, 203, 320, 486, 339, 107, 412, 369, 253, 318, 298, 226, 349, 338, 154, 423, 322, 185, 231, 252, 248, 377, 250, 113, 318, 366, 103, 227, 312, 90, 129, 276, 122, 357, 329, 74, 74, 307, 229, 167, 226, 105, 227, 231, 186, 135, 343, 181, 98, 140, 138, 177, 296, 143, 131, 252, 140, 11, 180, 203, 154, 198, 87, 35, 276, 223, 22, 166, 149, 47, 137, 119, 56, 241, 175, 56, 90, 209, 78, 163, 93, 25, 146, 152, 21, 131, 187, 52, 145, 64, 85, 174, 185, 67, 110, 155, 87, 72, 130, 54, 110, 151, 23, 64, 177, 122, 157, 125, 22, 24, 113, 52, 108, 144, 56, 73, 109, 52, 11, 150, 115, 100, 77, 93, 54, 133, 91, 37, 112, 53, 26, 87, 80, 80, 168, 71, 30, 86, 139, 46, 98, 113, 38, 61, 104, 58, 136, 146, 76, 80, 84, 86, 123, 102, 31, 86, 111, 21, 61, 162, 90, 80, 131, 49, 26, 138, 105, 81, 89, 100, 90, 96, 86, 92, 147, 88, 35, 107, 107, 101, 139, 78, 25, 123, 110, 41, 84, 160, 83, 98, 125, 79, 114, 121, 42, 69, 94, 74, 114, 105, 55, 113, 153, 70, 53, 118, 53, 38, 92, 51, 23, 106, 79, 73, 54, 116, 85, 72, 47, 38, 87, 71, 28, 38, 79, 38, 92, 54, 6, 105, 126, 22, 35, 108, 64, 41, 60, 67, 61, 95, 26, 61, 61, 101, 62, 51, 57, 60, 104, 35, 51, 107, 108, 18, 73, 20, 48, 85, 69, 10, 74, 122, 20, 13, 115, 107, 55, 40, 48, 4, 93, 57, 23, 88, 75, 36, 44, 66, 65, 112, 52, 55, 31, 60, 10, 51, 52, 25, 81, 48, 42, 46, 85, 46, 54, 23, 39, 58, 48, 9, 63, 76, 11, 59, 15, 18]
    # amplitudesRealData : obtained from bootstrapFourierNiger5Districts.py (on real data of Niger 5 Districts)
    realData_modulus = np.sqrt((np.asarray(amplitudesRealData) * np.asarray(amplitudesRealData)).sum()) # magnitude of vector; use asarray for multiplying floats
    #print 'amplitudesRealData:', amplitudesRealData, 'len:', len(amplitudesRealData), '\n'
    for filename in glob.glob('*.MeningitisCases*.txt'):     # Read all data tuples from matching files
        oneFileData = np.loadtxt(fileinput.input(filename))
        allDataMeningitisCases.append (oneFileData)
        averageOneFileData = np.mean(oneFileData)
        allAverageMeningitisCases.append(averageOneFileData)
        standardDeviationOneFileData = np.std(oneFileData)   # standard deviation
        allStandardDeviationMeningitisCases.append(standardDeviationOneFileData)
    #    print 'oneFileData:', 'avg=', averageOneFileData, 'std=', standardDeviationOneFileData, 'len=', len(oneFileData)
        
        # calculate Fourier amplitude then cosine of angle between oneFileData and realData; save in amplitudesModelData; Model=1simulationRun
        fourierModelData = np.fft.rfft(oneFileData) # oneFileData = dataModel
        amplitudesModelData = complexToAmplitude (fourierModelData)
        amplitudesModelData.pop(0)
        #print 'amplitudesModelData:', amplitudesModelData, 'len:', len(amplitudesModelData), '\n'
    
        # calculate vector
        #print 'len(amplitudesRealData):', len(amplitudesRealData), 'len(amplitudesModelData):', len(amplitudesModelData), '\n'
        dot = np.dot(amplitudesRealData, amplitudesModelData) # dot product
        if dot != 0:
            modelData_modulus = np.sqrt((np.asarray(amplitudesModelData) * np.asarray(amplitudesModelData)).sum()) # magnitude of vector; use asarray for multiplying floats 
            cos_angle = dot / realData_modulus / modelData_modulus # cosine of angle between x and y (realData_modulus and modelData_modulus)
            angle = np.arccos(cos_angle)
        else:
            cos_angle = 0.0
            angle = 0.0
        allCosineOfAngles.append(cos_angle)
        #print 'dot=', dot, 'cos_angle=', cos_angle, 'angle=', angle, '\n'
    
    #mymaxMeningitisCases = np.max(allDataMeningitisCases)
    medianAverageMeningitisCases = np.median(allAverageMeningitisCases)
    medianSDMeningitisCases = np.std(allStandardDeviationMeningitisCases)
    medianAllCosineOfAngles = np.median(allCosineOfAngles)
    
    #print 'allCosineOfAngles=', allCosineOfAngles, 'len=', len(allCosineOfAngles)
    
    #print 'MeningitisCases: numInputFiles =', len(allDataMeningitisCases), ' allData max =', mymaxMeningitisCases \
    #    , ' median of Averages =', medianAverageMeningitisCases, ' median of SD =', medianSDMeningitisCases
    
    
    # =====================================================================================================================================
    # PLOTS BELOW
    # =====================================================================================================================================
    
    # For plots: Define common variables 
    ageGroups = ['<1', '1-4', '5-14', '15-29', '30+']
    x = [0,1,2,3,4]
    fig = plt.figure(figsize=(18, 16))
    #fig2 = plt.figure(figsize=(24, 12))
    
    # Plot CasesAgeGroup =================================================================
    ax = fig.add_subplot(231)
    
    ax.plot(realDataCasesAgeGroup, marker='o', markersize=15, color='k', linewidth=2, label='Data')
    
    plt.plot(x, allDataCasesAgeGroup[0], linestyle='None', markersize=25, marker='_', color='b', label='Model Replicate') # plot the 1st one manually to add legend only once
    for index in range(len(allDataCP)):   #   print 'Current file :', allData[index]
       plt.plot(x, allDataCasesAgeGroup[index], linestyle='None', markersize=25, marker='_', color='b')
    ax.plot(mediansCasesAgeGroup, linestyle='None', marker='*', markersize=15, color='r', linewidth=5, label='Model Median')
       
    # Adjust X-axis parameters ==============================================================
    ax.set_xlim(-0.1, 4.1)
    x_pos = np.arange(len(realDataCP))
    plt.xticks(x_pos, ageGroups, fontsize=14, fontweight='bold')
    plt.xlabel(r'Age Group', fontsize=16, fontweight='bold')
    
    # Adjust Y-axis parameters ==============================================================
    y_max = 105
    y_interval = 10 # np.divide (y_max, 5)
    ax.set_ylim(-5.0, y_max)
    ax.set_yticks(np.arange(0.0, y_max, y_interval)) # set yticks in 2% intervals
    ax.set_yticklabels(np.arange(0, y_max, y_interval)) # set temporary yticklabels
    yticklabels = [item.get_text() + "%" for item in ax.get_yticklabels()] # add "%" sign to ylabels
    ax.set_yticklabels(yticklabels, fontsize=14, fontweight='bold') # set final yticklabels
    plt.ylabel(r'Age-Distribution of Meningitis Cases', fontsize=16, fontweight='bold')
    
    plt.grid()
    #plt.legend( loc='upper right', numpoints=1, frameon=False)
    
        
    # =====================================================================================================================================
    # Add text (TEMPORARY) =================================================================
    ax = fig.add_subplot(233)
    plt.axis('off')
    props = dict(boxstyle='round', facecolor='wheat', alpha=0.5) # text box in upper left in axes coords
    textstr = "Origin Directory:\n %s" % (os.getcwd()) # Add line2
    ax.text(0.01, 0.2, textstr, transform=ax.transAxes, fontsize=12, verticalalignment='top', bbox=props)
    textstr = "Completed: %d of %d runs." % (countCompleted, countAll) # Add line1    
    ax.text(0.01, 0.27, textstr, transform=ax.transAxes, fontsize=14, verticalalignment='top', bbox=props)
    
    # =====================================================================================================================================
    # Plot CarriagePrevalence =================================================================
    ax = fig.add_subplot(232)
    ax.plot(realDataCP, marker='o', markersize=15, color='k', linewidth=2, label='Data')
    
    plt.plot(x, allDataCP[0], linestyle='None', markersize=25, marker='_', color='b', label='Model Replicate') # plot the 1st one manually to add legend only once
    for index in range(len(allDataCP)):   #   print 'Current file :', allData[index]
       plt.plot(x, allDataCP[index], linestyle='None', markersize=25, marker='_', color='b')
    ax.plot(mediansCP, linestyle='None', marker='*', markersize=15, color='r', linewidth=5, label='Model Median')
       
    # Adjust X-axis parameters ==============================================================
    ax.set_xlim(-0.1, 4.1)
    x_pos = np.arange(len(realDataCP))
    plt.xticks(x_pos, ageGroups, fontsize=14, fontweight='bold')
    plt.xlabel(r'Age Group', fontsize=16, fontweight='bold')
    
    # Adjust Y-axis parameters ==============================================================
    y_max = mymaxCP + 10
    y_interval = 5.0
    ax.set_ylim(-0.5, y_max)
    ax.set_yticks(np.arange(0.0, y_max, y_interval)) # set yticks in y_interval intervals
    ax.set_yticklabels(np.arange(0, y_max, y_interval)) # set temporary yticklabels
    yticklabels = [item.get_text() + "%" for item in ax.get_yticklabels()] # add "%" sign to ylabels
    ax.set_yticklabels(yticklabels, fontsize=14, fontweight='bold') # set final yticklabels
    plt.ylabel(r'Average Carriage Prevalence', fontsize=16, fontweight='bold')
    
    plt.grid()
    #plt.legend( loc='upper right', numpoints=1, frameon=False)
    
    ax.legend(bbox_to_anchor=(1.7, 0.95), loc='upper right', numpoints=1, frameon=False) # call only once
    
    # =====================================================================================================================================
    
    # Plot MeningitisCases Average =================================================================
    ax = fig.add_subplot(234)
    realDataAverage = 0.938746438746    # obtained from : bootstrapFourierNiger5Districts.py (on real data of Niger 5 Districts)
    ax.plot(realDataAverage, marker='o', markersize=15, color='k', linewidth=2, label='Data')
    
    plt.plot(0, allAverageMeningitisCases[0], linestyle='None', markersize=25, marker='_', color='b', label='Model Replicate') # plot the 1st one manually to add legend only once
    for index in range(len(allAverageMeningitisCases)):
       plt.plot(0, allAverageMeningitisCases[index], linestyle='None', markersize=25, marker='_', color='b') # no x, only 1 x-value (bin), so use 0
    
    ax.plot(medianAverageMeningitisCases, linestyle='None', marker='*', markersize=15, color='r', linewidth=5, label='Model Median')
    
    # Adjust axis parameters ==============================================================
    ax.set_xlim(-0.05, 0.05)
    ax.xaxis.set_ticklabels([])
    y_max = np.ceil(np.max(allAverageMeningitisCases)) + 5.0
    y_interval = np.ceil(y_max / 5.0)
    gap = 0.5
    ax.set_ylim(-gap, y_max + gap)
    ax.set_yticks(np.arange(0.0, y_max, y_interval)) # set yticks in y_interval intervals
    ax.set_yticklabels(np.arange(0, y_max, y_interval), fontsize=14, fontweight='bold') # set temporary yticklabels
    plt.ylabel(r'Average Weekly Cases', fontsize=16, fontweight='bold')
    plt.grid()
    #plt.legend( loc='upper right', numpoints=1, frameon=False)
    
    # Plot MeningitisCases StandardDeviation =================================================================
    ax = fig.add_subplot(235)
    realDataSD = 3.86679304554    # obtained from : bootstrapFourierNiger5Districts.py (on real data of Niger 5 Districts)
    ax.plot(realDataSD, marker='o', markersize=15, color='k', linewidth=2, label='Data')
    
    plt.plot(0, allStandardDeviationMeningitisCases[0], linestyle='None', markersize=25, marker='_', color='b', label='Model Replicate') # plot the 1st one manually to add legend only once
    for index in range(len(allStandardDeviationMeningitisCases)):
       plt.plot(0, allStandardDeviationMeningitisCases[index], linestyle='None', markersize=25, marker='_', color='b') # no x, only 1 x-value (bin), so use 0
    
    ax.plot(medianSDMeningitisCases, linestyle='None', marker='*', markersize=15, color='r', linewidth=5, label='Model Median')
    
    # Adjust axis parameters ==============================================================
    ax.set_xlim(-0.05, 0.05)
    ax.xaxis.set_ticklabels([])
    y_max = np.ceil(np.max(allStandardDeviationMeningitisCases)) + 5.0
    y_interval = np.ceil(y_max / 5.0)
    gap = 0.5
    ax.set_ylim(-gap, y_max + gap)
    ax.set_yticks(np.arange(0.0, y_max, y_interval)) # set yticks in y_interval intervals
    ax.set_yticklabels(np.arange(0, y_max, y_interval), fontsize=14, fontweight='bold') # set temporary yticklabels
    plt.ylabel(r'Standard Deviation of Weekly Cases', fontsize=16, fontweight='bold')
    plt.grid()
    #plt.legend( loc='upper right', numpoints=1, frameon=False)
    
    
    # Plot MeningitisCases FourierCosine =================================================================
    ax = fig.add_subplot(236)
    
    plt.plot(0, allCosineOfAngles[0], linestyle='None', markersize=25, marker='_', color='b', label='Model Replicate') # plot the 1st one manually to add legend only once
    for index in range(len(allCosineOfAngles)):
       plt.plot(0, allCosineOfAngles[index], linestyle='None', markersize=25, marker='_', color='b') # no x, only 1 x-value (bin), so use 0
    
    ax.plot(medianAllCosineOfAngles, linestyle='None', marker='*', markersize=15, color='r', linewidth=5, label='Model Median')
    
    # Adjust axis parameters ==============================================================
    ax.set_xlim(-0.05, 0.05)
    ax.xaxis.set_ticklabels([])
    y_max = 1.05 # max for cos_theta
    y_interval = 0.2    #np.ceil(y_max / 5.0)
    gap = 0.05
    ax.set_ylim(-gap, y_max + gap)
    ax.set_yticks(np.arange(0.0, y_max, y_interval)) # set yticks in y_interval intervals
    ax.set_yticklabels(np.arange(0, y_max, y_interval), fontsize=14, fontweight='bold') # set temporary yticklabels
    plt.ylabel(r'Cosine of Angle', fontsize=16, fontweight='bold')
    plt.grid()
    #plt.legend( loc='upper right', numpoints=1, frameon=False)

    # =====================================================================================================================================
    # SAVE figure 
    #pathname = os.path.dirname(inputFile)
    cwd = os.getcwd()
    print 'cwd:', cwd
    now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    print now
    outputfileName = "All_" + now + "_CasesAndCP.png"
    #outputDirectory = os.path.abspath(pathname)
    outputfile = os.path.join(cwd, outputfileName)
    fig.savefig(outputfile, pad_inches=0.1)
    #fig.savefig(outputfile, bbox_inches='tight', pad_inches=0.1)
    print 'Figure saved as:', outputfile


else:
    print '\n', 'No simulation completed : I am quitting...'