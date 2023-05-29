# ds_helper

Some code to help with looking up datasets as needed for ATLAS.

Due to the complex way that ATLAS builds it environments, getting this to run is not trivial.

## Usage

Do not activate a local python environment - you must exist within the `rucio` one:

1. `source setup.sh` (this is isn't done for you automatically)
1. `setupATLAS`
1. `lsetup rucio`
1. `voms-proxy-init -voms atlas`
1. `source .venv/bin/activate`

and then you can finally type `python ds_finder.py`!

## Development

Testing does not work yet - it will run, but only in an environment that has access to AMI and rucio!
