#!/bin/bash

python covid19.py
rm -Rf out
mkdir out
mv *.csv out/
