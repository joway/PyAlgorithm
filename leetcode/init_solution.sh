#!/usr/bin/env bash
if [ $# -eq 2 ]
then
  filename=$1/$2.py
else
  filename=$1.py
fi
sed 's/{{ method }}/'$2'/' code_temp.txt >> $filename

