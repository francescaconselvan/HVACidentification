import pandas as pd
import pickle

with open('HVAC_ident_model.pkl', 'rb') as f:
    # Load the object from the pickle file
    loaded_object = pickle.load(f)

# Now you can use the loaded_object as you normally would
print(loaded_object)