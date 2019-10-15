# WORCTutorial
This is a tutorial for the WORC Package. For installing WORC, see
[the WORC readthedocs](https://worc.readthedocs.io/en/latest/static/quick_start.html#installation).
This tutorial can be followed in two ways:
1. Using [Jupyter notebook](http://jupyter.org/install): see the link for installation and usage details.
2. A .py Python script with comments.

Details on the usage can be found below. The code examples are the same in both
ways. This repository contains the following tutorials:

1. The "Simple" tutorial: suitable for users new to WORC and mostly interested
  in using WORC.

  * Jupyter:
  * Script: WORC_example_simple.py

2. The "Intermediate" tutorial: still suitable for users new to WORC, but
  contains a bit more detail on how to interact with WORC and does not use a
  facade.

  * Jupyter: WORCTutorialIntermediate.py
  * Script: WORC_tutorial_intermediate.py

3. The "Advanced" tutorial: contains more complicated workflows. This is still WIP.

* Jupyter: WORCTutorialAdvanced.py
* Script: WORC_tutorial_Advanced.py

Futher documentation can be found on [the WORC readthedocs](https://worc.readthedocs.io/).

## Installation

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

### Windows
On Windows, please install the required python packages either through pip or conda:
    pip install jupyter
    pip install PREDICT
    pip install WORC

Optionally, you may install [Graphviz](http://www.graphviz.org/).

## WIP
- We are working improving the notebook for Advanced Flows.
