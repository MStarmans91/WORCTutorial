# WORCTutorial
This repository contains tutorials for the WORC Python package. For more info on WORC, see
[the WORC readthedocs](https://worc.readthedocs.io/en/latest/static/quick_start.html#installation).

Most tutorials can be followed in two ways:
1. Using [Jupyter notebook](http://jupyter.org/install): see the link for installation and usage details.
   The notebook can alternatively be loaded directly in [Google Colab](https://colab.research.google.com/).
2. A .py Python script with comments.

The code examples are the same in both ways. Details on the installation can be found below. 

This repository contains the following standard tutorials:

1. WORCTutorialSimple: suitable for people new to WORC. Introduces the SimpleWORC facade, 
    an easy way to interact with WORC.
2. WORCTutorialBasic: suitable intermediate WORC uses. Introduces the BasicWORC facade,
    which extends SimpleWORC with more functionality to directly interact with the WORC object.

We also provide some extra tutorials in the ``Extra_tutorials`` folder on specific functionalities:

* WORCTutorialBasic_OwnFeatures.py: How to use your own features instead of the ones default extracted by WORC.
    See the [WORC FAQ](https://worc.readthedocs.io/en/development/static/faq.html#can-i-use-my-own-features-instead-of-the-standard-worc-features) for more info.

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
