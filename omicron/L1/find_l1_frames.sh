#!/bin/bash

set -e 

ligo_data_find --gps-start-time 1126051217 --gps-end-time 1127271617 --type L1_HOFT_C00 --lal-cache --observatory L --url-type file > frames.lcf
