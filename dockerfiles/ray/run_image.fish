#! /usr/bin/env fish

# the first port maps the ssh port, 22 is what I chose for all the ray containers so I don't have to deal with SSH
# warnings since the different containers use the same user name
# the 6379 port is for redis
# if you use this container as the head of a ray node the other nodes need to be able to access its redis server

docker run -p 2225:22 -p 6379:6379 --name bowling-ray \
       --shm-size=9.18gb \
       --mount type=bind,source=$HOME/projects/Bowling-For-Data-Private,target=/home/bravo/Bowling-For-Data-Private \
       --mount type=bind,source=$HOME/projects/Bowling-For-Data,target=/home/bravo/Bowling-For-Data \
       --mount type=bind,source=/media/data,target=/home/bravo/data \
       --mount type=bind,source=$HOME/projects/graeae,target=/home/bravo/graeae \
       --mount type=bind,source=$HOME/projects/models/,target=/home/bravo/models \
       -it bowling-ray
