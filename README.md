# atlas

## Building
- i wanted to be able to run the master build in docker but i also wanted the ability to add custom things of my own choosing in there, so this is a layer on top of AutoGPT.
- to get started, either clone or fork the main repo 'https://github.com/Significant-Gravitas/Auto-GPT' and change to that folder.
- every app needs a home, so the only thing i will keep changing in the Significant-Gravitas/Auto-GPT master code, is the homedir. Mine is `/home/atlas`.
- Then we build the image aptly called 'sg/auto-gpt:master'.

```
cd Auto-GPT
sed -i 's/WORKDIR \/app/WORKDIR \/home\/atlas/g' Dockerfile
docker build -t sg/auto-gpt:master .
```

- then in our atlas folder, we build the new image, which is based off 'sg/auto-gpt:master' but this time with our custom things added in Dockerfile and the changes for volume mounts and a few other options in docker-compose.yml

```
docker build -t katmai/atlas:001 .

```
## Customizing - these are things that should be altered for your own preference
- tools/u.start.sh - my command for starting up. 
- Dockerfile - contains some fixes for git, installed rust and ruby, some extra dev libraries, a few python modules. just stuff i have seen us getting stuck at over time. if i can make the road a little bit easier, maybe i should.
- docker-compose.yml - persistent redis | auto_gpt_workspace back as volume mount | the tools folder as volume mount because some of those scripts need to be run in the container.

## Tools
[](./tools/u.)
[bash](./tools/u.bash.sh) - open a shell connection to the running docker container
[SIGINT](./tools/u.sigint.py) - while in the container - running `python u.sigint.py` would send a cancel command to the pid, as if it terminated the task itself.


## Memory
- s3://atlas-adventuring-ai/appendonly.aof
- s3://atlas-adventuring-ai/dump.rdb

## Personality
- atlas.yaml

## Creations

