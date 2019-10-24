#!/bin/sh
# $1 <- constraints file, $2 <- student preferences 
python3 main.py $1 $2 schedule.out
perl is_valid.pl $1 $2 schedule.out
