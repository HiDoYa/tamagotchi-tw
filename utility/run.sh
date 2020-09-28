#!/bin/bash
make
python3 links.py > temp
./tama.out temp
rm temp
