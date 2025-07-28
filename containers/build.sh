#!/bin/bash

if [ -z "$1" ]; then
  echo "You must provide the Slack webhook URL as an argument"
  exit 1
fi

webhook="$1"
location=$(dirname "$0")

(cd "$location" && docker build -t backup-coord --build-arg=webhook="$webhook" .)

echo
echo "To deploy container, run: podman run -d --name backup-coord localhost/backup-coord"
