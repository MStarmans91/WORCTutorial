# WORCTutorial
This is a tutorial for the WORC Package. For more info on WORC, see
[the WORC readthedocs](https://worc.readthedocs.io/en/latest/static/quick_start.html#installation).

This tutorial can be followed in two ways:
1. Using [Jupyter notebook](http://jupyter.org/install): see the link for installation and usage details.
   The notebook can alternatively be loaded directly in [Google Colab](https://colab.research.google.com/).
2. A .py Python script with comments.

Details on the usage can be found below. The code examples are the same in both
ways. This repository contains a tutorial suitable for users new to WORC,
which makes use of the SimpleWORC facade. Two formats are provided:

    * Jupyter: WORCTutorialSimple.ipynb
    * Script: WORCTutorialSimple.py

Futher documentation can be found on [the WORC readthedocs](https://worc.readthedocs.io/).

## Installation

### Windows
On Windows, please install the required python packages either through pip or conda:
    pip install jupyter
    pip install WORC

Jupyter is only required when using the notebood. Optionally, you may
install [Graphviz](http://www.graphviz.org/).

### Ubuntu
Installation of all requirements for this tutorial can be done through the
*installation.sh* shellscript provided in this repository. In order to make
the script executable, on Ubuntu, please run the following:

    chmod -R 777 /path/to/installation.sh

Alternatively, you can use the following commands:

    echo -e "Installing git, pip, build-essential, graphviz, ipython and jupyter notebook requirements."
    apt-get -y install git python-pip build-essential graphviz ipython jupyter-core

    pip install jupyter
    pip install WORC

NOTE: Graphviz installation is optional.

## No Installation: Google Colab
If you want to actively use WORC, we advice you to install it locally. However,
for a quick test demonstration without installation, you can use [Google Colab](https://colab.research.google.com/).
Just launch the relevant Jupyter notebook from this repository and uncomment the relevant lines.

## WIP
- We are working on the notebooks for Intermediate and Advanced workflows.
