from testcontainers.postgres import PostgresContainer
from testcontainers.redis import RedisContainer
from get import random, setup_redis, setup_postgres_connection, app, today
import pytest
import subprocess
import json
import pickle

@pytest.fixture(scope='session')
def red():
	redis = RedisContainer('redis:7.4-rc2-bookworm')
	redis.start()
 
	exposed_port = redis.get_exposed_port(6379)
 
	red = setup_redis(exposed_port)
	return red
	

@pytest.fixture(scope='session')
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
   
		data_from_endpoint = json.loads(r.data)
		fact_id = data_from_endpoint["fact_id"]

		result = prisma.fact.count(
			where={
				'Fact_id': fact_id
			}
		)
  
		assert result == 1


def test_data_access_today_endpoint(prisma, red):
	with app.app_context():
		r = today()
		data_from_endpoint = json.loads(r.data)
		fact_id = data_from_endpoint["fact_id"]
		fact = data_from_endpoint["fact"]

		result = prisma.fact.count(
			where={
				'Fact_id': fact_id
			}
		)

		# check key exists in redis
		assert red.exists("today") == 1
		
		# retrieving cached fact object
		cached_fact_id, cached_fact = pickle.loads(red.get("today"))
		
  		# check cached version of fact is the same as the 
		assert cached_fact_id == fact_id
		assert cached_fact == cached_fact
		
  		assert red.pttl('today') is not None
		assert result == 1
  
		


  

