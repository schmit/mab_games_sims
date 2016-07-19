# Simulations accompanying Mean Field Equilibria for Multiarmed Bandit Games

This repo contains the Python code used to run simulations
for the Mean Field Equilibria for Multiarmed Bandit Games paper.
A preprint can be found on arXiv.


# Requirements

- Python 3
- [MCSim](https://github.com/schmit/mcsim): small framework for Monte Carlo simulations
- [Toyplot](https://github.com/sandialabs/toyplot): library used to create plots
- [Statsmodels](http://statsmodels.sourceforge.net/): statistics library used to fit LOWESS


# Notebooks

- `simulation_playground`: this notebook gives a simple example of how to
    set up a particular simulation
- `run_sims_disk`: this notebooks runs the simulations found in the paper
    and saves the outcomes as pickle objects.
    Make sure you have a `simulations/` subdirectory where simulations will be stored.
    Running all simulations will take a few hours and about 4gb of disk space.
    Also note that no seed is set so simulations may lead to different results
- `plots`: this notebook recreates the plots used in the paper.
    It reads the pickle files from the *run simulations to disk notebook*,
    so run that first.


# Questions

If you have any questions about the code or simulations, or have trouble getting things to work,
please open an Issue.
