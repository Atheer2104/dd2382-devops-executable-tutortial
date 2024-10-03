from testcontainers.core.container import DockerContainer
from testcontainers.core.waiting_utils import wait_for
from testcontainers.postgres import PostgresContainer
from testcontainers.redis import RedisContainer
import requests
from get import random, setup_redis, setup_postgres_connection, app
import os 
import pytest
import subprocess
import time
import json

@pytest.fixture()
def red():
	redis = RedisContainer('redis:7.4-rc2-bookworm')
	redis.start()
 
	red = setup_redis()
	return red
	

@pytest.fixture()
def prisma():
	postgres = PostgresContainer("postgres:bullseye", driver=None, username="postgres", password="password" ,dbname="users")
	postgres.start()

	exposed_port = postgres.get_exposed_port(5432)

	prisma = setup_postgres_connection(exposed_port)	

	subprocess.run(["prisma", "migrate", "dev"])
		
	return prisma

def test_data_access_random_endpoint(prisma):
	with app.app_context():
		r = random()
  
		assert r.status_code == 200
   
		data_from_endpoint = json.loads(r.data)
		fact_id = data_from_endpoint["fact_id"]

		result = prisma.fact.count(
			where={
				'Fact_id': fact_id
			}
		)
  
		assert result == 1


def test_data_access_today_endpoint():
	with app.app_context():
		r = random()
