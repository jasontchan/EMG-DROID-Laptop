#!/usr/bin/env bash
export DISPLAY=${DISPLAY:-:0}
export DOCKER_XAUTH="$HOME/.docker.xauth"

rm -f "$DOCKER_XAUTH"
touch "$DOCKER_XAUTH"
chmod 600 "$DOCKER_XAUTH"

xauth nlist "$DISPLAY" | sed -e 's/^..../ffff/' | xauth -f "$DOCKER_XAUTH" nmerge -
xauth -f "$DOCKER_XAUTH" list

xhost +local:root