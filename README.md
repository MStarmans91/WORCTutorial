# WORCTutorial
This is a tutorial for the WORC Package. For installing WORC, see
[the WORC readthedocs](https://worc.readthedocs.io/en/latest/static/quick_start.html#installation).
This tutorial can be followed in two ways:
1. Using [Jupyter notebook](http://jupyter.org/install): see the link for installation and usage details.
2. A .py Python script with comments.

Details on the usage can be found below. The code examples are the same in both
ways. This repository contains the following tutorials:

1. The "Simple" tutorial: suitable for users new to WORC and mostly interested in using WORC.
   Makes use of SimpleWORC.

    * Jupyter: WORCTutorialSimple.ipynb
    * Script: WORC_example_simple.py

2. The "Intermediate" tutorial: still suitable for users new to WORC, but
  contains more detail on how to interact directly with WORC and does not use
  SimpleWORC. This is currently disabled, as it has to be upgraded to WORC3.1.0.

3. The "Advanced" tutorial: contains more complicated workflows. This is still WIP.

Futher documentation can be found on [the WORC readthedocs](https://worc.readthedocs.io/).

## Installation

### Windows
On Windows, please install the required python packages either through pip or conda:
    pip install jupyter
    pip install PREDICT
    pip install WORC

Optionally, you may install [Graphviz](http://www.graphviz.org/).

### Ubuntu
Installation of all requirements for this tutorial can be done through the
*installation.sh* shellscript provided in this repository. In order to make
the script executable, on Ubuntu, please run the following:

    chmod -R 777 /path/to/installation.sh

Alternatively, you can use the following commands:

    echo -e "Installing git, pip, build-essential, graphviz, ipython and jupyter notebook requirements."
    apt-get -y install git python-pip build-essential graphviz ipython jupyter-core

    pip install jupyter
    pip install PREDICT
    pip install WORC

NOTE: Graphviz installation is optional.

## No Installation: Google Colab

If you want to actively use WORC, we advice you to install it locally. However,
for a quick test demonstration without installation, you can use [Google Colab](https://colab.research.google.com/).
Just launch the relevant Jupyter notebook from this repository and uncomment the relevant lines.

## WIP
- We are updating the Intermediate Tutorial to be compatible with WORC3.1.0.
- We are working improving the notebook for Advanced Flows.
