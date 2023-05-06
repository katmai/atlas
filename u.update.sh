#!/bin/bash -x
git checkout master
git pull
git checkout atlas
git merge master
