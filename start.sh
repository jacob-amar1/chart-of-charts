#!/bin/bash
  apps=$(ls apps/ )
  for item in $apps
  do
    echo $item
    check=$(git diff --name-only HEAD^ HEAD -- $item/ --relative)
    if [ -z "$check" ]; then
        echo "the tracked directory: $item did not canged skipping build"
    else
        echo "the tracked directory: $item has been changed, building docker file"
    fi
  done
