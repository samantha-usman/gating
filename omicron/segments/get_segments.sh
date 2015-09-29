#!/bin/bash

set -e

ligolw_segment_query_dqsegdb --segment-url https://segments.ligo.org --query-segments --include-segments H1:DMT-ANALYSIS_READY:1 --exclude-segments H1:DCH-MISSING_H1_HOFT_C00:2 --gps-start-time 1126051217 --gps-end-time 1127271617 --output H1-SEGMENTS.xml
ligolw_segment_query_dqsegdb --segment-url https://segments.ligo.org --query-segments --include-segments L1:DMT-ANALYSIS_READY:1 --exclude-segments L1:DCH-MISSING_L1_HOFT_C00:2 --gps-start-time 1126051217 --gps-end-time 1127271617 --output L1-SEGMENTS.xml
ligolw_print -t segment -c start_time -c end_time -d " " H1-SEGMENTS.xml > H1-SEGMENTS.txt
ligolw_print -t segment -c start_time -c end_time -d " " L1-SEGMENTS.xml > L1-SEGMENTS.txt
python /home/samantha.usman/aligo/gating/splice.py
