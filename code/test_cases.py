from testcontainers.core.container import DockerContainer
from testcontainers.core.waiting_utils import wait_for
from testcontainers.postgres import PostgresContainer
import requests
from get import random, setup_redis_and_postgres_connection, app
import os 
import pytest
import subprocess
import time
import json

# @pytest.fixture(scope='session', autouse=True)
# def setup_post():
	

def test_random_endpoint():
	postgres = PostgresContainer("postgres:bullseye", driver=None, username="postgres", password="password" ,dbname="users")
	postgres.start()

	time.sleep(3)
	
	conn = postgres.get_connection_url()
	print(f'FIRST:-------{conn}')
	exposed_port = postgres.get_exposed_port(5432)
	
	os.environ["DATABASE_URL"] = f"postgres://postgres:password@localhost:{exposed_port}/users"
 
	subprocess.run(["prisma", "migrate", "dev"])
	 
	setup_redis_and_postgres_connection()
  
	with app.app_context():
		r = random()
  
		assert r.status_code == 200
		# print(r.data)
   
		data_from_endpoint = json.loads(r.data)
		fact_id = data_from_endpoint["fact_id"]
		fact = data_from_endpoint["fact"]
		
		print(fact_id)
		print(fact)
 

