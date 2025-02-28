import h5py
import os
import numpy as np
import json


targets_dict = [
                "/ID1586847201334178219",
                "/ID1586847201334178219/ID1586847238903121237",
                "/ID1586847201334178219/ID1586847238903121237/ID1586847239103173289",
                "/ID1586847201334178219/ID1586847238903121237/ID1586847239103173289/ID1688720703583502154136955",
            ]

Multi_d = [
    [50008, 0, 0],
    [50009, 0, 0],
    [50010, 0, 0],
    [50011, 0, 0]
]

description = {'CML_TYPE': 'device', 
               'LEVEL': 'LEAF', 
               'allowBroadcast': True, 
               'leafDeviceType': 'MUSIC', 
               'leafParentType': 'room',
               'leafType': 'dataset'
            }

# Assuming self.folder_path is defined and is a valid directory path
with h5py.File("propStructure.hdf5", 'w') as file:
    for group_name in targets_dict:
         # Create a group
        print(group_name)
        group = file.create_group(group_name)
        group.attrs['description'] = json.dumps(description)
        dataset_name = group_name + '/Multi_d_data'
        file.create_dataset(dataset_name, data=Multi_d)