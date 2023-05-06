#!/bin/bash

if [ $# -ne 1 ]; then
  echo "Usage: $0 <process name>"
  exit 1
fi

pid=$(pgrep -f $1)

if [ -z "$pid" ]; then
  echo "Process not found: $1"
  exit 1
fi

echo $pid
