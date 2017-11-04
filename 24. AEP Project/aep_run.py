import aep_plot

aep_plot.read("AEP Model.xlsm")

aep_plot.plot_validation("Figures/Validation of model")
aep_plot.plot_aep("Figures/Estimated prevalence of AEP")
aep_plot.add_validation("Figures/Additional figures for model validation")
aep_plot.plot_distribution("Figures/Distribution of population members in age and sexual-behavior groups")
aep_plot.plot_regression("Figures/Compliance with CDC Regulation")
