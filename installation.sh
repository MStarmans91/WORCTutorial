#!/bin/bash

# -----------------------------------------------------------------------
# WORC Installation
# -----------------------------------------------------------------------

# Install requirements: git, cmake, build-essential
echo -e "Installing git, pip, build-essential, graphviz, ipython and jupyter notebook requirements."
apt-get -y install git python-pip build-essential graphviz ipython jupyter-core

# Install jupyter when using the notebook
pip install jupyter

# Install WORC
pip install WORC

# Alternative: Clone WORC repository from Github and install
# mkdir ~/Documents/Packages
# git clone http://Github.com/MStarmans91/WORC ~/Documents/Packages/WORC
# cd ~/Documents/Packages/WORC
# git checkout development
# pip install -r requirements.txt
# python setup.py install

# Alternative: Install the PREDICT requirements and package manually
# echo -e "Installing PREDICT requirements and package itself."
# cd ~/Documents/Packages
# git clone http://Github.com/Svdvoort/PREDICTFastr PREDICT
# cd PREDICT
# git checkout develop
# pip install -r requirements.txt
# python setup.py install
