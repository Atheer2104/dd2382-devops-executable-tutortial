docker ps --filter 'name=postgres' --format '{{.ID}}' | grep ""
docker ps --filter 'name=redis' --format '{{.ID}}' | grep ""

# add curl command here

