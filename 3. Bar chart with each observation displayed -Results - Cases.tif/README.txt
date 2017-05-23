# Input Files: 1. Model - Cases (Best) Scattered.csv
                    # Columns: 'Prevention 2', 'Prevention 1', 'Base Prime', 'Base', 'No Additional Intervention'
#              2. Model - Cases (Worse) Scattered.csv
                    # Columns: Ditto above.
# Summary: 1. Data read in.
        #  2. y-axis values generated for with all variable values extracted (with strain replacement).
        #  3. Scatter plot generated with above generated y-axis values with '|' marker
        #  4. Process repeated for no strain replacement dataset.
        #  5. Both scatter plot generation codes repeated to generate both scatter plots in one figure.
        #  6. Figure saved as PDF.
# Output: Stored in folder containing notebook file (PDF format).