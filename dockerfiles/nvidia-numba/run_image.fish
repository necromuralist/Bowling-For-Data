#! /usr/bin/env fish
docker run --gpus all -p 2224:22 --name bowling-numba-conda \
       --mount type=bind,source=$HOME/projects/Bowling-For-Data,target=/home/bravo/Bowling-For-Data \
       --mount type=bind,source=/media/data,target=/home/bravo/data \
       --mount type=bind,source=$HOME/projects/graeae,target=/home/bravo/graeae \
       --mount type=bind,source=$HOME/projects/models/,target=/home/bravo/models \
       -it bowling-numba-conda bash
