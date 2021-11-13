#! /usr/bin/env fish
docker run -p 2225:22 --name bowling-ray \
       --mount type=bind,source=$HOME/projects/Bowling-For-Data-Private,target=/home/bravo/Bowling-For-Data-Private \
       --mount type=bind,source=/media/data,target=/home/bravo/data \
       --mount type=bind,source=$HOME/projects/graeae,target=/home/bravo/graeae \
       --mount type=bind,source=$HOME/projects/models/,target=/home/bravo/models \
       --shm-size=9.18gb \
       -it bowling-ray
