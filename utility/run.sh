#!/bin/bash

if [[ $1 = "create" ]]; then
	python3 links.py
	python3 cut.py
	python3 label.py
	python3 correction.py create
fi

echo $1
if [[ $1 = "load" ]]; then
	python3 correction.py load
	cp -r name_tama_images_meta_en ../
	cp -r name_tama_images_meta_jp ../
	cp -r imag_tama_images ../
	cp -r tama_images ../
fi
