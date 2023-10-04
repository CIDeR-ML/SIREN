import numpy as np
import torch
import h5py
import os

from torch.utils.data import Dataset, DataLoader
from torchvision import transforms, utils

# Define dict for tank region
tankregion = {'top': 'topscattable', 'TOP': 'topscattable', 'Top': 'topscattable',
              'bar': 'sidescattable', 'BAR': 'sidescattable', 'Bar': 'sidescattable', 'side': 'sidescattable', 'Side': 'sidescattable', 'SIDE': 'sidescattable',
              'bot': 'botscattable', 'BOT': 'botscattable', 'Bot': 'botscattable'}

class WCTEScatTable(Dataset):
    def __init__(self, h5_file, region = 'top', num_samples_per_load=10, target_transform=None, dataset_transform=None):
        #region: the region you want to load, .e.g 'top'/'bot'/'bar'
        self.infile = h5_file
        self.regionname = tankregion[region]
        f = h5py.File(self.infile, mode = 'r')
        self.tab_names = ['topscattable','botscattable', 'sidescattable']        
        assert self.regionname in self.tab_names            
        grp_scat = f[self.regionname+';1']
        assert 'nbins' in grp_scat.keys() and 'table' in grp_scat.keys()

        self.dataset = np.array(grp_scat['table']).squeeze()
        f.close()
        
        self.num_samples_per_load = num_samples_per_load
        self.table_shape = None
        if self.regionname == 'sidescattable':
            self.tableshape = (35, 16, 16, 16, 16, 16)
        else:
            self.tableshape = (35, 16, 8, 16, 16, 16)        
        

    def __len__(self): 
        sum_dim = 1
        for dim in self.tableshape:
            sum_dim *= dim
        assert self.dataset_shape[0] == sum_dim

        return self.dataset.shape[0]
       
    def __getitem__(self, index):
        if isinstance(index, int):
            raise ValueError('The index of a `WCTEScatTable` must be a tuple of integers, and not an integer. ')
        assert len(index) == self.num_samples_per_load
        datasets = np.array([self.dataset[i] for i in index])
        
        assert self.tableshape is not None
        dataset_reshaped = np.array(self.dataset.reshape(self.tableshape))
        unrav_indices = np.array(np.unravel_index(index, self.tableshape)).T
        
        return unrav_indices, datasets

