echo "Cloning Code Respository"

cd filesystem/home/ubuntu/
git clone https://github.com/Atheer2104/dd2382-devops-executable-tutortial.git
cd dd2382-devops-executable-tutortial/backend-api/

# install psql
sudo apt-get install -y postgresql-client

export DATABASE_URL=postgres://postgres:password@localhost:5432/users

echo "Done"