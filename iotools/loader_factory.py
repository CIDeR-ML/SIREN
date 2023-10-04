import torch
from torch.utils.data import DataLoader
import iotools.Dataset as dt
from iotools.sampler import *

def loader_factory(dataset, batch_size, shuffle=True, sampler = None, num_workers = 0, pin_memory=False, drop_last=False, timeout=0, worker_init_fn=None, **args):
    ds = getattr(dt,dataset)(**args)

    if sampler is not None and shuffle is True:
        shuffle = False
        
    loader = DataLoader(ds,
                        batch_size  = batch_size,
                        shuffle     = shuffle,
                        sampler     = sampler,
                        num_workers = num_workers,
                        pin_memory  = pin_memory,
                        drop_last   = drop_last,
                        timeout     = timeout, 
                        worker_init_fn = worker_init_fn,
                        )

    return loader
