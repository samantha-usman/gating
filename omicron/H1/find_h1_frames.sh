#!/bin/bash

set -e 

ligo_data_find --gps-start-time 1126051217 --gps-end-time 1127271617 --type H1_HOFT_C00 --lal-cache --observatory H --url-type file > frames.lcf
