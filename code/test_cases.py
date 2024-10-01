from testcontainers.core.container import DockerContainer
from testcontainers.core.waiting_utils import wait_for
from testcontainers.postgres import PostgresContainer
import requests
from get import main
import os 
import pytest
import subprocess
import time

# @pytest.fixture(scope='session', autouse=True)
# def setup_post():
	

def test_random_endpoint():
	postgres = PostgresContainer("postgres:bullseye", driver=None, username="postgres", password="password" ,dbname="users")
	postgres.start()

	time.sleep(3)
	
	conn = postgres.get_connection_url()
	print(f'FIRST:-------{conn}')
	exposed_port = postgres.get_exposed_port(5432)

	print(exposed_port)
	
	# main(postgres_port=exposed_port)
	
	# time.sleep(3)
	
	# subprocess.run(["prisma", "migrate", "dev"])
	
	# r = requests.get("http://127.0.0.1:8000/api/today")
	
	# # response should be OK
	# assert r.status_code == 200
	
	# data_from_endpoint = r.json()
	# fact_id = data_from_endpoint["fact_id"]
	# fact = data_from_endpoint["fact"]
	
	# print(fact_id)
	# print(fact)
 

