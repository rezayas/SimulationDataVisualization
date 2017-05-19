# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 13:26:20 2017

@author: arif
"""
import fileinput, glob
import numpy as np
import os, datetime, sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.ioff()
import math
import matplotlib.gridspec as gridspec
from matplotlib.backends.backend_pdf import PdfPages
    
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
    
#    textstr = "Origin Directory: %s" % (os.getcwd())
#    fig2.suptitle(textstr, fontsize=12, fontweight='bold')
    
    numberOfTrajectories = countCompleted
    numberOfTrajectoriesPerPage = 5
    numberOfPages = int (np.ceil(numberOfTrajectories / numberOfTrajectoriesPerPage) + 1 )
    # we want 5 Trajectories per page

    numberOfColumns = 3
#    gs = gridspec.GridSpec(numberOfTrajectories, numberOfColumns, wspace=0.1, hspace=0.1, width_ratios=[2,1,1]) 
    
    now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    basename = os.path.basename(os.getcwd())
    outputfileName = basename + "_" + now + "_AllTrajectories.pdf"
    outputfile = os.path.join(os.getcwd(), outputfileName)
    pdf_pages = PdfPages(outputfile)

    line_width = 1.0
    ageGroups = ['<1', '1-4', '5-14', '15-29', '30+']
    x = [0,1,2,3,4]
    x_pos = np.arange(len(ageGroups))
    
    fileRealNigerCases = '/Users/arif/Documents/BatchRuns/NigerFiveDistrictsTotal.txt'
    realFileData = np.loadtxt(fileinput.input(fileRealNigerCases))
    amplitudesRealData = [591, 122, 269, 438, 421, 556, 340, 459, 671, 344, 161, 497, 932, 685, 425, 97, 116, 623, 550, 141, 572, 574, 180, 263, 309, 336, 742, 570, 93, 287, 558, 392, 291, 418, 273, 370, 387, 87, 377, 620, 366, 259, 389, 245, 255, 425, 203, 320, 486, 339, 107, 412, 369, 253, 318, 298, 226, 349, 338, 154, 423, 322, 185, 231, 252, 248, 377, 250, 113, 318, 366, 103, 227, 312, 90, 129, 276, 122, 357, 329, 74, 74, 307, 229, 167, 226, 105, 227, 231, 186, 135, 343, 181, 98, 140, 138, 177, 296, 143, 131, 252, 140, 11, 180, 203, 154, 198, 87, 35, 276, 223, 22, 166, 149, 47, 137, 119, 56, 241, 175, 56, 90, 209, 78, 163, 93, 25, 146, 152, 21, 131, 187, 52, 145, 64, 85, 174, 185, 67, 110, 155, 87, 72, 130, 54, 110, 151, 23, 64, 177, 122, 157, 125, 22, 24, 113, 52, 108, 144, 56, 73, 109, 52, 11, 150, 115, 100, 77, 93, 54, 133, 91, 37, 112, 53, 26, 87, 80, 80, 168, 71, 30, 86, 139, 46, 98, 113, 38, 61, 104, 58, 136, 146, 76, 80, 84, 86, 123, 102, 31, 86, 111, 21, 61, 162, 90, 80, 131, 49, 26, 138, 105, 81, 89, 100, 90, 96, 86, 92, 147, 88, 35, 107, 107, 101, 139, 78, 25, 123, 110, 41, 84, 160, 83, 98, 125, 79, 114, 121, 42, 69, 94, 74, 114, 105, 55, 113, 153, 70, 53, 118, 53, 38, 92, 51, 23, 106, 79, 73, 54, 116, 85, 72, 47, 38, 87, 71, 28, 38, 79, 38, 92, 54, 6, 105, 126, 22, 35, 108, 64, 41, 60, 67, 61, 95, 26, 61, 61, 101, 62, 51, 57, 60, 104, 35, 51, 107, 108, 18, 73, 20, 48, 85, 69, 10, 74, 122, 20, 13, 115, 107, 55, 40, 48, 4, 93, 57, 23, 88, 75, 36, 44, 66, 65, 112, 52, 55, 31, 60, 10, 51, 52, 25, 81, 48, 42, 46, 85, 46, 54, 23, 39, 58, 48, 9, 63, 76, 11, 59, 15, 18]
    modulusRealData = np.sqrt((np.asarray(amplitudesRealData) * np.asarray(amplitudesRealData)).sum()) # magnitude of vector; use asarray for multiplying floats
#    print 'realData_modulus =', realData_modulus
    averageRealData = np.average(realFileData)
    maxRealData = np.max(realFileData)    
    minRealData = np.min(realFileData)
    sdRealData = np.std(realFileData)
    
    w1 = 1 / 4
    w2 = 1 / (modulusRealData * modulusRealData)
    w3 = 1 / (averageRealData * averageRealData)
    w4 = 1 / (sdRealData * sdRealData)
    temp = 1.0 # np.max( 0.0, 1.0 )   # minRealData = 0.0
    w5 = 1  # 1 / (temp * temp)
    w6 = 1 / (maxRealData * maxRealData)
    
    realDataCarriagePrevalence = [1.80, 2.60, 4.90, 3.60, 2.60]
    realDataCasesAgeGroup = [2.62, 20.83, 59.88, 13.51, 3.16]
    
    print 'numberOfPages = ', int(numberOfPages)
    firstPlotIndexInPage = 1
    for page in range(1, numberOfPages+1): # page 1 to 5
        #print '\nPage ', page, '\n'
        
        # Create a figure instance (ie. a new page) on A4 page size
        fig = plt.figure(figsize=(8.27, 11.69), dpi=100)
        
        textstr = "Origin Directory: %s" % (os.getcwd())
        fig.suptitle(textstr, fontsize=10)

        gs = gridspec.GridSpec(numberOfTrajectoriesPerPage, numberOfColumns, \
                               wspace=0.2, hspace=0.4, width_ratios=[2,1,1])
        
        # using following for-loop, plot next 5 trajectories in this page
        firstPlotIndexInPage = (page - 1) * numberOfTrajectoriesPerPage + 1
        lastPlotIndexInPage = firstPlotIndexInPage + numberOfTrajectoriesPerPage
        gridspecIndex = 0 # index starts from 0 in gridspec
        # gridspecIndex = need a separate index to place the plot in the right row in gridspec
        for i in range(firstPlotIndexInPage, lastPlotIndexInPage): # sim 1 to 5
            if i <= countCompleted:
                
                fileMeningitisCases = glob.glob( str(i) + '.MeningitisCases*.txt')
                fileCarriagePrevalence = glob.glob( str(i) + '.CarriagePrevalence*.txt')                  
                fileCasesAgeGroup = glob.glob( str(i) + '.CasesAgeGroup*.txt')
                print 'Trajectory', i #, 'with :', fileMeningitisCases, fileCarriagePrevalence, fileCasesAgeGroup, '\n'
#                print 'Placing row in gridspecIndex =', gridspecIndex
                
                # ============================================================================
                # Plot Meningitis Cases
                oneFileData = np.loadtxt(fileinput.input(fileMeningitisCases))
                ax1 = plt.subplot(gs[gridspecIndex, 0])
                plt.plot(realFileData, linewidth=line_width, color='r', alpha=0.3)
                plt.plot(oneFileData, linewidth=line_width, color='b')                
                if i == firstPlotIndexInPage: plt.title('Meningitis Cases', fontsize=10)
                plt.grid()
                
                fourierModelData = np.fft.rfft(oneFileData) # oneFileData = dataModel
                amplitudesModelData = complexToAmplitude (fourierModelData)
                amplitudesModelData.pop(0)
                modulusTrajectory = np.sqrt((np.asarray(amplitudesModelData) * np.asarray(amplitudesModelData)).sum()) 
                
                averageTrajectory = np.average(oneFileData)
                maxTrajectory = np.max(oneFileData)    
                minTrajectory = np.min(oneFileData)
                sdTrajectory = np.std(oneFileData)
                
                dot = np.dot(amplitudesRealData, amplitudesModelData) # dot product
                denom = modulusRealData * modulusTrajectory
                temp1 = 1.0 - (dot / denom)
                temp2 = temp1 * temp1
                pw1 = w1 * temp2
                
                temp3 = modulusTrajectory - modulusRealData
                temp4 = temp3 * temp3
                pw2 = w2 * temp4
                
                temp5 = averageTrajectory - averageRealData
                temp6 = temp5 * temp5
                pw3 = w3 * temp6

                temp7 = sdTrajectory - sdRealData
                temp8 = temp7 * temp7
                pw4 = w4 * temp8
                
                temp9 = minTrajectory - minRealData
                temp10 = temp9 * temp9
                pw5 = w5 * temp10
                
                temp11 = maxTrajectory - maxRealData
                temp12 = temp11 * temp11
                pw6 = w6 * temp12
                
                fourierSum = pw1 + pw2 + pw3 + pw4 + pw5 + pw6
                
#                print 'RealData: modulus =', modulusRealData, 'average =', averageRealData, \
#                    'sd =', sdRealData, 'min =', minRealData, 'max =', maxRealData
#                print 'Trajectory: modulus =', modulusTrajectory, 'average =', averageTrajectory, \
#                    'sd =', sdTrajectory, 'min =', minTrajectory, 'max =', maxTrajectory
                print 'fourierSum =', fourierSum
                
                # ============================================================================
                # Plot Carriage Prevalence
                oneFileData = np.loadtxt(fileinput.input(fileCarriagePrevalence))
                mymax = np.max(oneFileData)
                ax2 = plt.subplot(gs[gridspecIndex, 1])
                plt.plot(realDataCarriagePrevalence, linewidth=line_width, color='r', alpha=0.3)
                plt.plot(oneFileData, linewidth=line_width, color='b')
                
                if i == firstPlotIndexInPage: plt.title('Carriage Prevalence', fontsize=10)
                y_max = mymax + 1
                y_interval = np.ceil(y_max / 5.0)
                ax2.set_ylim(-0.1, y_max)
                ax2.set_yticks(np.arange(0.0, y_max, y_interval)) # set yticks in y_interval intervals
                ax2.set_yticklabels(np.arange(0, y_max, y_interval)) # set temporary yticklabels
                yticklabels = [item.get_text() + "%" for item in ax2.get_yticklabels()] # add "%" sign to ylabels
                ax2.set_yticklabels(yticklabels, fontsize=8, rotation=75) # rotation anti-cw from 0
                ax2.set_xlim(-0.01, 4.01)
                plt.xticks(x_pos, ageGroups, fontsize=8)
                plt.grid()
                
                carriagePrevalenceSum = 0.0
                for k in range(0, 5): # ageGroupIndex
                    if oneFileData[k] > 0: # avoid adding if agegroup's carriagePrevalence = 0.0
                        temp1 = (oneFileData[k] - realDataCarriagePrevalence[k]) / realDataCarriagePrevalence[k]
                        temp2 = temp1 * temp1
                        carriagePrevalenceSum += temp2
#                    print '\tsimCP[k] =', oneFileData[k], ', realCP[k] =', realDataCarriagePrevalence[k]              
#                    print '\ttemp1 =', temp1, ', temp2 =', temp2, ', sum =', carriagePrevalenceSum
                print 'carriagePrevalenceSum =', carriagePrevalenceSum
                
                # ============================================================================
                # Plot Cases AgeGroup
                oneFileData = np.loadtxt(fileinput.input(fileCasesAgeGroup))
                sumCasesAgeGroup = np.sum(oneFileData) # get the sum of oneFileData
                percentageCasesAgeGroup = np.multiply ( np.divide (oneFileData, sumCasesAgeGroup), 100.0 ) # normalize and percent
                myCasesAGFormatted = [ '%.2f' % elem for elem in percentageCasesAgeGroup ]
                ax3 = plt.subplot(gs[gridspecIndex, 2])
                plt.plot(realDataCasesAgeGroup, linewidth=line_width, color='r', alpha=0.3)
                plt.plot(myCasesAGFormatted, linewidth=line_width, color='b')
                
                if i == firstPlotIndexInPage: plt.title('Cases AgeGroup', fontsize=10)
                y_max = 101
                y_interval = 25
                ax3.set_ylim(-1.0, y_max)
                ax3.set_yticks(np.arange(0.0, y_max, y_interval)) # set yticks in 2% intervals
                ax3.set_yticklabels(np.arange(0, y_max, y_interval)) # set temporary yticklabels
                yticklabels = [item.get_text() + "%" for item in ax3.get_yticklabels()] # add "%" sign to ylabels
                ax3.set_yticklabels(yticklabels, fontsize=8) # set final yticklabels
                ax3.set_xlim(-0.01, 4.01)
                plt.xticks(x_pos, ageGroups, fontsize=8)
                plt.grid()
                
                casesAGSum = 0.0
                for k in range(0, 5): # ageGroupIndex
                    temp1 = (float(myCasesAGFormatted[k]) - realDataCasesAgeGroup[k]) / realDataCasesAgeGroup[k]
                    temp2 = temp1 * temp1
                    casesAGSum += temp2
                print 'casesAGSum =', casesAGSum
                
                # ============================================================================
                # add texts
                props = dict(boxstyle='round', facecolor='wheat', alpha=0.2)

                textstr = "Fourier Sum = %0.2f" % (fourierSum) # Add line1
                ax1.text(0.0, 0.95, textstr, transform=ax1.transAxes, fontsize=8, verticalalignment='top', bbox=props)

                textstr = "Carriage Sum = %0.2f" % (carriagePrevalenceSum)
                ax2.text(0.0, 0.95, textstr, transform=ax2.transAxes, fontsize=8, verticalalignment='top', bbox=props)

                textstr = "CasesAG Sum = %0.2f" % (casesAGSum)
                ax3.text(0.0, 0.95, textstr, transform=ax3.transAxes, fontsize=8, verticalalignment='top', bbox=props)
                
                fit = fourierSum + carriagePrevalenceSum + casesAGSum
                textstr = "Fit = %0.2f" % (fit)
                ax3.text(0.75, 0.5, textstr, transform=ax3.transAxes, fontsize=10, fontweight='bold', verticalalignment='top', bbox=props)
                
                textstr = "Trajectory %d :" % (i)
                ax1.text(-0.2, 1.15, textstr, transform=ax1.transAxes, fontsize=8, fontweight='bold', verticalalignment='top', bbox=props)
                # ============================================================================
                
                gridspecIndex += 1
                
                # ============================================================================        

        pdf_pages.savefig(fig) # save the page
        
    # Write the PDF document to the disk
    pdf_pages.close()
    print 'Figure saved as:', outputfile
    globalFigureDirectory = sys.argv[1]
    import shutil 
    shutil.copy2(outputfile, globalFigureDirectory)
        
else:
    print '\n', 'No simulation completed : I am quitting...'
    

# =====================================================================================
# NOTES:
# gridspec.GridSpec:    
    # (numberOfRows, numberOfColumns, )
    # width_ratios: controls the width of columns; must provide numberOfColumns values    
    
# gridspecIndex = I needed a separate index to place the plot in the right spot in gridspec