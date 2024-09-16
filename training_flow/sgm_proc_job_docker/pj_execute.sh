#!/bin/bash

WORKDIR=/opt/ml/processing

cd ${WORKDIR}/ml-training-flow

echo "Transforming notebook into script..."
jupyter nbconvert --to script notebook.ipynb
echo "Executing notebook..."
python notebook.py

echo "Saving results to local S3 Bucket dir..."
cp -r CNN-Intent-Classifier-0.0.2.mlpackage ${WORKDIR}/output-data/
