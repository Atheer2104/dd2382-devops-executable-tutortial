from testcontainers.postgres import PostgresContainer
from testcontainers.redis import RedisContainer
from get import random, setup_redis, setup_postgres_connection, app, today
import pytest
import subprocess
import json
import pickle

@pytest.fixture(scope='session')
def red():
	# Creates the specified redis container   
	redis = RedisContainer('redis:7.4-rc2-bookworm')
	
 	# Start to pull the container
	redis.start()
 	
  	# Fetches the dynamicly allocated port that testcontainers assigns to the redis container
	exposed_port = redis.get_exposed_port(6379)
	
 	# Set up the Redis connection using the exposed port
	# The setup_redis function is assumed to create and return a Redis client
	red = setup_redis(exposed_port)
	return red
	
# Setup prisma fixture for the entire test session
@pytest.fixture(scope='session')
def prisma():
	# create the specific postgresql container with some configs
	postgres = PostgresContainer("postgres:bullseye", driver=None, username="postgres", password="password" ,dbname="users")
	
 	# starting the container 
	postgres.start()

	# Fetches the dynamicly allocated port that testcontainers assigns to the postgresql container
	exposed_port = postgres.get_exposed_port(5432)

	# set up the postgresql connection to the db, here Prisma a database ORM is used for easier usage
	# this function returns a prisma client connection 
	prisma = setup_postgres_connection(exposed_port)	
	
	# runs the prisma migration in order to setup the DB according to schema
	subprocess.run(["prisma", "migrate", "dev"])
		
	return prisma

def test_data_access_random_endpoint(prisma):
	with app.app_context():
		# calling /api/random endpiont
		r = random()
		
		# parsing recieved data from endpoint
		data_from_endpoint = json.loads(r.data)
		fact_id = data_from_endpoint["fact_id"]
		
  		# querying postgresql db for amount of rows where there is match in fact id
		result = prisma.fact.count(
			where={
				'Fact_id': fact_id
			}
		)
		
		# check that we exactly one row in our postgresql db
		assert result == 1


def test_data_access_today_endpoint(prisma, red):
	with app.app_context():
		# calling /api/today endpoint
		r = today()

		# parsing recieved data from endpoint
		data_from_endpoint = json.loads(r.data)
		fact_id = data_from_endpoint["fact_id"]
		fact = data_from_endpoint["fact"]

		# querying postgresql db for amount of rows where there is match in fact id
		result = prisma.fact.count(
			where={
				'Fact_id': fact_id
			}
		)

		# check that we exactly one row in our postgresql db
		assert result == 1

		# check key exists in redis
		assert red.exists("today") == 1

		# retrieving cached fact object
		cached_fact_id, cached_fact = pickle.loads(red.get("today"))

		# check cached version of fact is the same as the the one recived by endpoint 
		assert cached_fact_id == fact_id
		assert cached_fact == fact

		# check that there is expire time set
		assert red.pttl('today') is not None
  

