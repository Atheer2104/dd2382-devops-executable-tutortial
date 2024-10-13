echo "Doing setup for you"
while [ ! -f /tmp/finished ]; do sleep 1; done

cd filesystem/home/ubuntu/dd2382-devops-executable-tutortial/backend-api/
export DATABASE_URL=postgres://postgres:password@localhost:5432/users
source env/bin/activate
echo DONE