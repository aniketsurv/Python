import h5py
import os
import numpy as np

with h5py.File("example.hdf5", "r") as f:
    # Fetch data from the root dataset
    data = f["my_dataset"][:]
    print("Data in my_dataset:", data)
    
    # Fetch data from a nested dataset
    nested_data = f["my_group/nested_dataset"][:]
    print("Data in nested_dataset:", nested_data)
