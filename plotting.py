"""
Contains functions to create toyplot graphs to visualize simulations
"""

import numpy as np
import toyplot as tp

import statsmodels.api as sm

def smooth_plot(x, y, axes, frac=0.1, **kwargs):
    lowess = sm.nonparametric.lowess(y, x, frac=frac)
    axes.plot(lowess[:, 0], lowess[:, 1])


def scatter_evo_population(outcomes, axes, **kwargs):
    pop_profs = np.array(outcomes["pop_profile"]).T
    narms, steps = pop_profs.shape

    for idx, row in enumerate(pop_profs[:-1]):
        axes.scatterplot(row, **kwargs)


def plot_evo_population(outcomes, axes, frac=0.1):
    pop_profs = np.array(outcomes["pop_profile"]).T
    narms, steps = pop_profs.shape

    for idx, row in enumerate(pop_profs[:-1]):
        t = np.arange(len(row))
        smooth_plot(t, row, axes, frac)
