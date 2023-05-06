#!/bin/bash -x
mkdir autogpt/auto_gpt_workspace/created-images
mv autogpt/auto_gpt_workspace/*.jpg autogpt/auto_gpt_workspace/created-images/
mv autogpt/auto_gpt_workspace/created-images autogpt/
rm -rf autogpt/auto_gpt_workspace/*
mv autogpt/created-images autogpt/auto_gpt_workspace/
