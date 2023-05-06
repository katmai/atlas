#!/bin/bash -x
#/home/katmai/.docker/cli-plugins/docker-compose stop
#yes | /home/katmai/.docker/cli-plugins/docker-compose run -T --rm --build auto-gpt --gpt3only --continuous --ai-settings atlas.yaml
/home/katmai/.docker/cli-plugins/docker-compose run -T --rm --build auto-gpt 
