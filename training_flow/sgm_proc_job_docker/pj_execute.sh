#!/bin/bash

WORKDIR=/opt/ml/processing

cd ${WORKDIR}/ml-training-flow

jupyter nbconvert --to script notebook.ipynb
python notebook.py

cp -r CNN-Intent-Classifier-0.0.2.mlpackage ${WORKDIR}/output-data/
