import h5py
import os
import numpy as np

with h5py.File("example.hdf5", "a") as f:
    # Resize dataset to hold more data
    dset = f["my_dataset"]
    dset[-5:] = np.arange(10, 15)
