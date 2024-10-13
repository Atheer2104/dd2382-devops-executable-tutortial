echo "Doing setup for you"
while [ ! -f /tmp/finished ]; do sleep 1; done

cd filesystem/home/ubuntu/dd2382-devops-executable-tutortial/backend-api/
source env/bin/activate
echo DONE