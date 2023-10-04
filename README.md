# SIREN

## Converting fiTQun Indirect Light Table

The script `root2hdf5_scattab.py` was used to convert the fiTQun 6D indirect light table from ROOT to h5. The output is stored at:

- (`gpgpu`) 192.168.156.71: `/home/pdeperio/wcte/ryom/fiTQun_tuning/TuningFiles/scattable/fiTQun_scattablesF_nuPRISMBeamTest_16cShort_mPMT.h5`
- idark: `/gpfs02/work/pdeperio/wcte/ryom/fiTQun_tuning/TuningFiles/scattable/fiTQun_scattablesF_nuPRISMBeamTest_16cShort_mPMT.h5`
- https://triumfoffice365-my.sharepoint.com/:u:/g/personal/pdeperio_triumf_ca/EcuocTIcQIZOjoVGbFh3BX8BQA96AabDT2WOdzBiFrmeMA?e=DAHt9d

## Dataloader

Files in `iotools`, an example notebook `Dataloader_example` is also provided to check if the dataloader runs fine.

- `iotools/Dataset.py`: custom dataset for the scattering tables, currently only available for WCTE.
- `iotools/samplers.py`: sampling method definitions
- `iotools/loader_factory.py`: dataloaders for the dataset