# 46320: a0pack and A0 code

Template for the HAWC files and Python code used in the design exercise in
46320: Loads, Aerodynamics and Control of Wind Turbines.

## Quick-start guide

These steps assume (1) you have installed Python, VS Code, HAWC2/HAWCStab2, etc.,
per the instructions given in the course and (2) that you are familiar with
conda environments, installing Python packages, etc.

1. (Recommended) Create and activate a venv or conda environment called `lac` with Python 3.13.
1. Install `a0pack` editably. In the same directory as `pyproject.toml`, `pip install -e .`.
1. Change into scripts folder: `cd scripts`  
1. Run the Python script: `python make_hawc2s.py`. This generates a HAWC2S input file
   `htc_hawc2s/dtu_10mw_hawc2s_1wsp.htc`.  
1. Run HAWC2S on the newly generated input file:  `hawc2s htc_hawc2s/dtu_10mw_hawc2s_1wsp.htc`
1. If file `res_hawc2s/dtu_10mw_hawc2s_1wsp.pwr` is created with 1 line of data,
   it's working!