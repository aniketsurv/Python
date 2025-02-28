import h5py
import os
import numpy as np


with h5py.File("example.hdf5", "a") as f:
    # Update specific elements in the dataset
    f["my_dataset"][0:3] = [100, 101, 102]
    
    # Print updated data
    updated_data = f["my_dataset"][:]
    print("Updated data in my_dataset:", updated_data)
