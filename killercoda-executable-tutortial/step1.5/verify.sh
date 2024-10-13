#!/bin/bash

docker ps --filter 'name=postgres' --format '{{.ID}}' | grep ""
docker ps --filter 'name=redis' --format '{{.ID}}' | grep ""

# add curl command here
curl http://localhost:8000/api
curl http://localhost:8000/api/today
curl http://localhost:8000/api/random

if lsof -i:8000 > /dev/null; then
  kill $(lsof -t -i:8000)
fi