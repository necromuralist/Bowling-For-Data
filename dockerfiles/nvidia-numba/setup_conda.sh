#! /usr/bin/env sh

conda create --name bowling-numba jupyter
conda config --add channels conda-forge
conda config --set channel_priority strict
conda update -n base -c defaults conda
conda install mamba
mamba -c conda-forge install numba numpy pandas holoviews hvplot
echo "conda activate bowling-numba" >> .bashrc
