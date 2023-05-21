#!/bin/bash -x
## build the docker image
cd ~/AI/Auto-GPT
git checkout master
git reset --hard HEAD
git pull
sed -i 's/WORKDIR \/app/WORKDIR \/home\/atlas/g' Dockerfile
docker build -t sg/auto-gpt:master .

## build the atlas image
cd ~/AI/atlas
docker build -t katmai/atlas:001 .
