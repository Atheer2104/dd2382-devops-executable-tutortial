# cloning code repository
echo "Cloning Code Respository"

cd filesystem/home/ubuntu/
git clone https://github.com/Atheer2104/dd2382-devops-executable-tutortial.git
cd dd2382-devops-executable-tutortial/backend-api/

# install python 3.12
sudo apt update
sudo add-apt-repository --yes ppa:deadsnakes/ppa
sudo apt update

sudo apt-get install -y python3.12 && sudo apt-get install -y postgresql-client && sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.12 1 && curl https://bootstrap.pypa.io/get-pip.py | sudo python3.12 && export DATABASE_URL=postgres://postgres:password@localhost:5432/users && echo "Done"