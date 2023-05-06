#!/bin/bash -x
#~/.docker/cli-plugins/docker-compose stop
yes | ~/.docker/cli-plugins/docker-compose run -T --rm --build auto-gpt --gpt3only --continuous --ai-settings atlas.yaml
#~/.docker/cli-plugins/docker-compose run -T --rm --build auto-gpt --gpt3only --ai-settings atlas.yaml
