#!/bin/bash -x
/usr/local/bin/aws s3 cp /home/katmai/AI/atlas/redis-data/appendonly.aof s3://atlas-adventuring-ai
/usr/local/bin/aws s3 cp /home/katmai/AI/atlas/redis-data/dump.rdb s3://atlas-adventuring-ai
/usr/local/bin/aws s3 cp /home/katmai/AI/atlas/atlas.yaml s3://atlas-adventuring-ai
