#!/usr/bin/env bash

curl -si "$1" | grep -i 'Content-Length' | awk '{print $2}'
