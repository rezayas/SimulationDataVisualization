import aep_plot

aep_plot.read("AEP Model (2017-09-27) - Visualization.xlsx")

aep_plot.plot_validation("Validation of model")
aep_plot.plot_aep("Estimated prevalence of AEP")
aep_plot.add_validation("Additional figures for model validation")
aep_plot.plot_distribution("Distribution of population members in age and sexual-behavior groups")
aep_plot.plot_regression("Compliance with CDC Regulation")
