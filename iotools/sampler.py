import numpy as np
import random
from torch.utils.data.sampler import RandomSampler, SequentialSampler
from iotools.Dataset import WCTEScatTable


class seqSampleWCTE(SequentialSampler):
    def __init__(self, data_source, start_frac = 0.5):
        if not isinstance(data_source, WCTEScatTable):
            raise ValueError()
        self.data_source = data_source
        self.start_frac = start_frac

    def __len__(self):
        return self.data_source.num_samples_per_load

    def __iter__(self):
        num_bins = len(self.data_source.dataset)
        num_bins_per_load = self.data_source.num_samples_per_load
        
        yield np.arange(int(num_bins*self.start_frac), int(num_bins*self.start_frac)+num_bins_per_load, 1, dtype = int)

class rndSampleWCTE(RandomSampler):
    def __init__(self, data_source):
        if not isinstance(data_source, WCTEScatTable):
            raise ValueError()
        self.data_source = data_source

    def __len__(self):
        return self.data_source.num_samples_per_load

    def __iter__(self):
        num_bins = len(self.data_source.dataset)
        num_bins_per_load = self.data_source.num_samples_per_load

        yield random.sample(range(num_bins), num_bins_per_load)
            
            
