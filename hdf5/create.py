import h5py
import os
import numpy as np

# Assuming self.folder_path is defined and is a valid directory path
with h5py.File("propStructure.hdf5", 'w') as f:
    # Create a dataset or group within the file
    data = [1, 2, 3, 4, 5]
    f.create_dataset("my_dataset", data=data)
    # You can add more datasets or groups here


# Create a new HDF5 file
with h5py.File("example.hdf5", "w") as f:
    # Create a dataset
    data = np.arange(10)
    f.create_dataset("my_dataset", data=data)
    
    # Create a group
    grp = f.create_group("my_group")
    
    # Create a dataset within the group
    grp.create_dataset("nested_dataset", data=np.random.random(5))