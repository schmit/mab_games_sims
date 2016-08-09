# Simulations accompanying Mean Field Equilibria for Multiarmed Bandit Games

This repo contains the Python code used to run simulations
for the Mean Field Equilibria for Multiarmed Bandit Games paper.
A preprint can be found on [SSRN](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=2045842).


# Requirements

- Python 3
- Jupyter notebooks
- [MCSim](https://github.com/schmit/mcsim): small framework for Monte Carlo simulations
- [Toyplot](https://github.com/sandialabs/toyplot): library used to create plots
- [Statsmodels](http://statsmodels.sourceforge.net/): statistics library used to fit LOWESS


# Notebooks

High level code to run simulations and plot results are Jupyter notebooks:

- `simulation_playground`: this notebook gives a simple example of how to
    set up a particular simulation, and useful if you want to simulate a specific scenario
- `run_sims_disk`: this notebooks runs the simulations found in the paper
    and saves the outcomes as pickle objects.
    Before using this notebook, run `setup.sh` to create subdirectories used to store simulations and plots.
- `plots`: this notebook recreates the plots used in the paper.
    It reads the pickle files from the `run_sims_disk`, so run that first.


# Questions

If you have any questions about the code or simulations, or have trouble getting things to work,
please open an Issue.
