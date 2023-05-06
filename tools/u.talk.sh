#!/bin/bash

if [ $# -ne 2 ]; then
  echo "Usage: $0 <message> <pid>"
  exit 1
fi

MESSAGE="$1"
PID="$2"

echo "$MESSAGE" > /proc/$PID/fd/0
