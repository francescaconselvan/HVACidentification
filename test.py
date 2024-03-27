import pandas as pd
import pickle

with open('HVAC_ident_model.pkl', 'rb') as f:
    loaded_object = pickle.load(f)

print(loaded_object)