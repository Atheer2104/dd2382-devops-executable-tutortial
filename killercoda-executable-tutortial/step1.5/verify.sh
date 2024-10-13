docker ps --filter 'name=postgres' --format '{{.ID}}' | grep ""
docker ps --filter 'name=redis' --format '{{.ID}}' | grep ""

# add curl command here
curl http://localhost:8000/api
curl http://localhost:8000/api/today
curl http://localhost:8000/api/random