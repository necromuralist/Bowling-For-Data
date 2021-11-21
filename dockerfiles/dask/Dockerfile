ARG IMAGE_NAME=python
# numba only supports up to python 3.9 according to pypi
#ARG TAG=latest
ARG TAG=3.9-bullseye

FROM ${IMAGE_NAME}:${TAG}

# first do the stuff that you need to be root to do

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    rsync \
    zile \
    screen \
    byobu \
    openssh-server && \
    useradd --create-home --shell /bin/bash bravo

# # switch from root to bravo
USER bravo
WORKDIR /home/bravo

# copy over some files
COPY --chown=bravo:bravo authorized_keys .ssh/authorized_keys
COPY --chown=bravo:bravo requirements.txt .

# define our virtualenv paths
ENV VIRTUALENVS=.virtualenvs
ENV VIRTUALENV=$VIRTUALENVS/Bowling-For-Data

# setup the virtualenv
RUN mkdir $VIRTUALENVS && \
    python -m venv $VIRTUALENV

# use the virtualenv
ENV PATH="$VIRTUALENV/bin:$PATH"
RUN --mount=type=cache,target=/root/.cache \
    pip --no-cache-dir install --upgrade pip && \
    pip --no-cache-dir install -r requirements.txt

# setup the bashrc for logging in
RUN echo 'source ~/.virtualenvs/Bowling-For-Data/bin/activate' >> .bashrc && \
    echo  'export PATH=$PATH:$HOME/.local/bin' >> .bashrc

# switch back to root or the ssh-server won't work right
USER root
WORKDIR /
ENTRYPOINT service ssh restart && bash

