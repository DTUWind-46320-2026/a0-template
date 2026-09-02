# 46320: a0pack and A0 code

Template for the HAWC files and Python code used in the design exercise in
46320: Loads, Aerodynamics and Control of Wind Turbines.

## Quick-start guide

These steps assume (1) you have installed Python, VS Code, HAWC2/HAWCStab2, etc.,
per the instructions given in the course and (2) that you are familiar with
conda environments, installing Python packages, etc.

### Create virtual environment

1. Create a venv or conda environment called `lac` with Python 3.13.  
   * E.g., in conda: `conda create -n lac python=3.13 -y`.
1. Activate the virtual environment.
   * E.g., in conda:  `conda activate lac`.

### Use Python to make a HAWC2S htc file

1. Install package editably: 
   * Navigate to folder containing `pyproject.toml`.
   * Installation command: `pip install -e .`
1. Change into scripts folder: `cd scripts`  
1. Run the Python script: `python make_hawc2s.py`. This generates a HAWC2S input file
   `htc_hawc2s/dtu_10mw_hawc2s_1wsp.htc`.  

## Run HAWC2S on the generated file

NB: Be careful that you run HACW2S from the correct working directory!

1. CD into the `hawc_files` folder.
1. Run HAWC2S on the generated input file:  `hawc2s htc_hawc2s/dtu_10mw_hawc2s_1wsp.htc`
1. If file `res_hawc2s/dtu_10mw_hawc2s_1wsp.pwr` is created with 1 line of data,
   it's working!