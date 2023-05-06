#!/bin/bash

# Set the container name
container_name="atlas-auto-gpt"

# Get the container ID
container_id=$(docker ps -qf "name=$container_name")

# Open an interactive bash shell to the container
docker exec -it $container_id bash
