# Input Files: 1. Model - Vaccines Used  (Worse).csv
                    # Columns: 'Unnamed: 0', 'MenAfriVac®', 'MenAfriVac®.1', 'PMP-Reactive', 
                    #          'PMP-Reactive.1', 'PMC-Routine', 'PMC-Routine.1', 'PMC-Preventive', 
                    #          'PMC-Preventive.1', 'PMC-Reactive', 'PMC-Reactive.1'
#              2. Model - Vaccines Used  (Best).csv
                    # Columns: Ditto above.
#              3. Data - Distribution of Clinical Men.csv
                    # Columns: 'Unnamed: 0', 'Neisseria Men-A', 'Neisseria Non Men-A', 'Others'
# Summary: 1. Data read in.
        #  2. Horizontal stacked bar plots each plotted separately and saved. (First with strain replacement, then without)
        #  3. Horizontal stacked bar plots plotted side by side and saved (subplots created).
        #  4. Vertical stacked bar plot plotted and saved.
# Output: Stored in folder containing notebook file (PDF format).

================================================================================

.iloc function:

Target specific rows and columns by their indexes. This may be useful in cases where column names change (although it takes away from the readability of the code). The colon before the indexes is the separator between the row and column indexes. There’s nothing to the left of the colon since we wish to retain all rows.


legend and handles:

The handle indexes that are generated are, by default, generated in increasing order of the column indexes, that is, if column ‘Red’ is column 1 and column ‘Blue’ is column 2, then the ‘Red’ is plotted in the legend before ‘Blue’. If you wish to see the original order, you could delete everything to do with handles and the legend will plot the original order.
