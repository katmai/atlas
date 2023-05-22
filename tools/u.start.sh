#!/bin/bash -x
#~/.docker/cli-plugins/docker-compose stop
~/.docker/cli-plugins/docker-compose run -T --rm --build auto-gpt --gpt3only --ai-settings atlas.yaml --prompt-settings atlas.settings.yaml
#~/.docker/cli-plugins/docker-compose run -T --rm --build auto-gpt --gpt3only --continuous --ai-settings atlas.yaml --prompt-settings atlas.settings.yaml
#yes | ~/.docker/cli-plugins/docker-compose run -T --rm --build auto-gpt --gpt3only --continuous --ai-settings atlas.yaml --prompt-settings atlas.settings.yaml

#~/.docker/cli-plugins/docker-compose run -T --rm --build auto-gpt --gpt3only --ai-settings atlas.yaml
