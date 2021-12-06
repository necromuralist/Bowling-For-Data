#! /usr/bin/env fish

# the Docker Buildkit adds more caching for the things installed
set -lx DOCKER_BUILDKIT 1
docker build -t bowling-numba .
