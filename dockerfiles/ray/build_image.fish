#! /usr/bin/env fish
set -lx DOCKER_BUILDKIT 1
docker build -t bowling-ray .
