#!/bin/bash

# rsc name: ml-training-flow-sgm-lc

# Exit immediately if non-zero return value
set -e


# INSTALL MISSING PYTHON DEPENDENCIES
### Activate the Conda environment where Jupyter is installed
###  (like `conda activate` but gets the correct env automatically):
eval "$(conda shell.bash hook)"
pip install coremltools
conda deactivate


# CLONE GITHUB REPO
### Define variables
SECRET_NAME="ml-training-flow-github-creds"
REPO_URL="https://github.com/LeandroVidal555/ml-training-flow.git"
FOLDER_NAME="ml-training-flow"

if [ ! -d "$FOLDER_NAME" ]; then
  echo 'COMMAND: git clone $REPO_URL'
  git clone $REPO_URL
else
  cd $FOLDER_NAME
  git pull
  echo "Directory '$FOLDER_NAME' already exists. Skipping clone."
fi
