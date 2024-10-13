#!/bin/bash

set -x

set -e

set -o pipefail

# cloning code repository

cd filesystem/home/ubuntu/
git clone https://github.com/Atheer2104/dd2382-devops-executable-tutortial.git
cd dd2382-devops-executable-tutortial/backend-api/

# echo "installing prisma"

pip install prisma 

# echo "running prisma generate"

prisma generate 

echo done > /tmp/finished 


 #sudo apt update && sudo add-apt-repository --yes ppa:deadsnakes/ppa && sudo apt update && sudo apt-get install -y python3.12 && curl https://bootstrap.pypa.io/get-pip.py | sudo python3.12  && python3.12 -m pip install virtualenv && python3.12 -m virtualenv env && source env/bin/activate && sudo apt-get install -y postgresql-client && export DATABASE_URL=postgres://postgres:password@localhost:5432/users && touch /tmp/finished

