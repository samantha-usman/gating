#!/bin/bash

set -e

source /home/samantha.usman/src/gwpw/bin/activate
source /home/dbrown/projects/aligo/pycbc-1.2.0/opt/lalsuite/etc/lalsuiterc 

ls -1 /home/samantha.usman/aligo/er8b/omicron/H1/triggers/H1\:GDS-CALIB_STRAIN/*xml | lalapps_path2cache > omicron.lcf

/home/samantha.usman/aligo/gating/make_gating_from_omicron --start 1126051217 --end 1127271617 --ifo H1 --min-snr 300 --zeros 0.25 --pad 0.25 --cache-file omicron.lcf --verbose 2>&1 | tee make_gating_from_omicron.$$.log
