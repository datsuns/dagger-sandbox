#!/usr/bin/bash

IMG=$1

id=`docker load -i ${IMG} | awk '/Loaded image ID:/ {print $4}'`
echo ${id}
docker tag "${id}" myimage:latest && docker image ls myimage
