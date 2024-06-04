## What is the model for
Example: the code explores different techniques and parameters for predicting if PV and HP has been installed in a house or not. This is done by using the electricity time series of the building. model receives time series of electricity consumption for one year with 15 mins time steps and predicts if PV and/or heat pump has been installed in the associated building.

## How does the model work
Example: the model is a classifier that is trained using gradient boosting with tunes parameters.

## Link to github
https://github.com/potterheadgryffin/HVACidentification


## Packages installation
* better to list the packages in a requirements.txt file 
* pickle and numpy packages are not necessary to install  because it is embedded in python
* scikit-learn version ==1.4.1. version 1.2 failed to install, BUT IT IS A PROBLEM later on to import the pickle model see below - possible to install a free old scikit-learn version? see here: https://stackoverflow.com/questions/59974146/installing-an-old-version-of-scikit-learn

SOLUTION: use python version 10 and install scikit-learn 1.2.2
* install also h5py,tables, openpyxl for running HVAC_indent_model

## model_reader.py
- line 3 importing HVAC_ident model:  
"
with open('HVAC_ident_model.pkl', 'rb') as f:
    loaded_object = pickle.load(f)
"
problem with inconsistent version of scikit-learn
Can't get attribute '_PredictScorer' on <module 'sklearn.metrics._scorer' from '/Users/francesca/Desktop/e-think/MODERATE/HVACidentification/venv/lib/python3.12/site-packages/sklearn/metrics/_scorer.py'>


## HAVC_ident.py
* dataset "HP_powerTimeseries/2018_data_15min.hdf5" here: https://zenodo.org/records/5642902
* line 118, 127: rewrote fileName path 
