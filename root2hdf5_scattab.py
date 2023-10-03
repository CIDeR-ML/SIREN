import uproot
import numpy as np
import h5py as h5

fname_in='/home/drinkingkazu/Downloads/fiTQun_scattablesF_nuPRISMBeamTest_16cShort_mPMT.root'
fname_out='myass.h5'

with uproot.open(fname_in) as fin:
    print('Objects:',fin.keys(),'\n')
    
    with h5.File(fname_out,'w') as fout:
        
        dump_all = False
        for oname in fin.keys():
            if dump_all:
                print('Dumping key-value pairs for',oname)
                print(fin[oname].all_members)
                print('\n')
                dump_all = False
                
            # Load table and bins info
            print('Accessing table dim and values')
            nbins = np.array(fin[oname].member('nbins'))
            table = np.array(fin[oname].member('table'))

            # Create the output group
            ogroup = fout.create_group(oname)
            # Write
            print('Copying into H5 format...')
            ogroup.create_dataset('nbins',(len(nbins)),dtype='int')
            ogroup.create_dataset('table',(np.prod(nbins),),dtype='float')
            ogroup['nbins'][:] = nbins
            ogroup['table'][:] = table
            print('done.\n')




