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

with h5py.File("propStructure.hdf5", 'r') as file:
    for group_name in targets_dict:
        group = file[group_name]
        description = json.loads(group.attrs['description'])
        print("\n")
        print(f"Group: {group_name}")
        print(f"Description: {description}")
        dataset = file[group_name + '/Multi_d_data'][:]
        print(f"Dataset: {dataset}")
   