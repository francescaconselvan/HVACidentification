## 1. Description
### What is the model for 
The model explores different techniques and parameters for predicting if PV and HP has been installed in a house or not. This is done by using the electricity time series of the building. model receives time series of electricity consumption for one year with 15 mins time steps and predicts if PV and/or heat pump has been installed in the associated building.

### How does the model work
The model is a classifier that is trained using gradient boosting with tunes parameters.

### Python file to call
The model is saved in a pickle file named . Python file model_reader is for reading the model and creating the output.

## 2. Contact
Mohammed Haris Shamsi  
mohammadharis.shamsi@vito.be

## 3. Link to the code
https://github.com/potterheadgryffin/HVACidentification

## 4. Python version 
Python 3.10

## 5. Installation
numpy 1.26.4
pandas 2.1.4
matplotlib 3.8.0
sklearn 1.2.2
seaborn 0.12.2
h5py
tables

## 6. Input Data

## 7. Output

