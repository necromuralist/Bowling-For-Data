# ray currently only supports python up to 3.7 (November 2, 2021)
# bullseye is the current stable version of Debian

ARG IMAGE_NAME=python
ARG TAG=3.8-slim-bullseye
FROM ${IMAGE_NAME}:${TAG}

# first do the stuff that you need to be root to do
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    rsync \
    zile \
    screen \
    byobu \
    virtualenv \
    openssh-server && \
    useradd --create-home --shell /bin/bash bravo

# this requires docker-buildkit (the cache won't keep downloading dependencies)
# unless there's a change
RUN --mount=type=cache,target=/root/.cache \
    pip install --upgrade pip

# switch from root to bravo
USER bravo
WORKDIR /home/bravo

COPY --chown=bravo:bravo authorized_keys .ssh/authorized_keys
COPY --chown=bravo:bravo requirements.txt .

# define our virtualenv paths
ENV VIRTUALENVS=.virtualenvs
ENV VIRTUALENV=$VIRTUALENVS/Bowling-For-Data

# setup the virtualenv
RUN mkdir $VIRTUALENVS
RUN python -m venv $VIRTUALENV
ENV PATH="$VIRTUALENV/bin:$PATH"

# use the virtualenv
RUN pip install -r requirements.txt

# setup the bashrc for logging in
RUN echo 'source ~/.virtualenvs/Bowling-For-Data/bin/activate' >> .bashrc
RUN echo  'export PATH=$PATH:$HOME/.local/bin' >> .bashrc

USER root
WORKDIR /
ENTRYPOINT service ssh restart && bash

