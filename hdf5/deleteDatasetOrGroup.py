import h5py
import os
import numpy as np

with h5py.File("example.hdf5", "a") as f:
    # Delete a dataset
    del f["my_dataset"]
    
    # Delete a group (and all datasets within it)
    del f["my_group"]
