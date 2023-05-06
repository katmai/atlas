# atlas

## Building
- i wanted to be able to run the master build in docker.
- every app needs a home, so the only thing i will keep changing in the Significant-Gravitas/Auto-GPT master code, is the homedir. Then we build the image aptly called 'sg/auto-gpt:master'

```
sed -i 's/WORKDIR \/app/WORKDIR \/home\/atlas/g' Dockerfile
docker build -t sg/auto-gpt:master .
```

- then in our atlas folder, we build the new image, which is based off 'sg/auto-gpt:master' but this time with our custom things added in Dockerfile and the changes for volume mounts and a few other options in docker-compose.yml

```
docker build -t katmai/atlas:001 .
```

## Memory
- s3://atlas-adventuring-ai/appendonly.aof
- s3://atlas-adventuring-ai/dump.rdb

## Personality
- atlas.yaml

## Creations

