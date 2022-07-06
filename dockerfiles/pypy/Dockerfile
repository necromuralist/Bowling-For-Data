# if the version of ubuntu doesn't have the latest pypy3
# you might end up re-building the stuff you install (like pandas)
# instead of downloading it from pypi
# (actually this doesn't seem to matter for pandas, still, better to get the
# latest pypy, I guess)

ARG IMAGE_NAME=ubuntu
FROM ${IMAGE_NAME}:22.04

# Set timezone to avoid apt-get dialog asking what timezone you're in
# https://askubuntu.com/questions/909277/avoiding-user-interaction-with-tzdata-when-installing-certbot-in-a-docker-contai/1098881#1098881
RUN ln -snf /usr/share/zoneinfo/$CONTAINER_TIMEZONE /etc/localtime && echo $CONTAINER_TIMEZONE > /etc/timezone

# this will also work but it suppresses all dialog boxes instead of setting up the timezone
# ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    graphviz \
    openssh-server \
    pypy3 \
    pypy3-dev \
    pypy3-lib \
    rsync \
    screen \
    zile \
    virtualenv && \
    useradd --create-home --shell /bin/bash bravo

# this requires docker-buildkit to be turned on
# (environment variable DOCKER_BUILDKIT=1)
# (the cache won't keep downloading dependencies)
# unless there's a change 
RUN --mount=type=cache,target=/root/.cache \
    pypy3 -m pip install --upgrade pip

# *** setup user bravo *** #
# switch from root to bravo
USER bravo
WORKDIR /home/bravo

COPY --chown=bravo:bravo authorized_keys .ssh/authorized_keys
COPY --chown=bravo:bravo requirements.txt .
COPY --chown=bravo:bravo screenrc .screenrc

# define our virtualenv paths
ENV VIRTUALENVS=.virtualenvs
ENV VIRTUALENV=$VIRTUALENVS/Bowling-For-Data

# setup the virtualenv
RUN mkdir $VIRTUALENVS && \
    pypy3 -m venv $VIRTUALENV

ENV PATH="$VIRTUALENV/bin:$PATH"

RUN pypy3 -m ensurepip
# install wheel outside of the requirements file
# otherwise the other packages in the file won't be able to use it
RUN --mount=type=cache,target=/root/.cache \
    pypy3 -m pip --no-cache-dir install --upgrade pip && \
    pypy3 -m pip --no-cache-dir install --upgrade wheel && \
    pypy3 -m pip --no-cache-dir install -r requirements.txt

# setup the bashrc to activate the virtulaenv when bravo logs in
RUN echo 'source ~/.virtualenvs/Bowling-For-Data/bin/activate' >> .bashrc
RUN echo  'export PATH=$PATH:$HOME/.local/bin' >> .bashrc

# *** Go back to root or the ssh-server will fail when you start the container *** #
USER root
WORKDIR /
ENTRYPOINT service ssh restart && bash
