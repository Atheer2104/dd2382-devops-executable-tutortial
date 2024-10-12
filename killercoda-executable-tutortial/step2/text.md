## Testing using Testcontainers 

In this Step, you will learn more about:

1. How the Testcontainers is setup in python to test the backend API
2. How to get the exposed port of the containers created by Testcontainers
3. How the Testcontainers library works in python

Let's get started!

## How Testing is performed 

We have two tests namely **test_data_access_random_endpoint** and **test_data_access_today_endpoint**. We are using pytest to run these test hence they start with the name test that is how pytest will identifiy which test functions to execute.

The former test function tests the random endpoint by calling the respective endpoint function and getting the fact id which is returned in the JSON response. Then it checks that in the postgreSQL database, there exists such a row with same fact id because we are saving the fact and fact id together with the view count in PostgreSQL.

The latter test function tests the today endpoint by calling the respective endpoint function, it also gets the fact id and checks the same thing as the previous test when it comes to PostgreSQL but this endpoint caches the fact to Redis so it also checks in Redis that fact is available and the value is equal to the fact received from the endpoint. Finally, it also checks that the cached fact in Redis has an expiration date.

## How Testcontainers is Integrated into the tests 
As mentioned Testcontainers allow us to spin up dockercontainers for our services such as Redis and PostgreSQL. These are needed to implement our pytest test cases on the data insertion and check that the stored data is accessible.    

As specified earlier one can start a GenericContainer in Testcontainers and in the python library for Testcontainers, this is known as DockerContainer("X"), here X refers to the name of the docker image, more info about how this looks like is [here](https://testcontainers-python.readthedocs.io/en/latest/core/README.html), since we are using well-known services we are not using GenericContainer instead we are using modules that are provided by Testcontainers, list of the available modules are found [here](https://testcontainers-python.readthedocs.io/en/latest/modules/index.html)

### PostgreSQL
Here's how we set up PostgreSQL using Testcontainers:
```
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
```{{}}

Notice that we setup up this Testcontainer in the pytest fixture to ensure that when we run the testcases the containers are up and running before we try to store and access anything. We also use this fixutre one per session, so that we use the same storage instance for all our testcases however we can use the a different storage instance if that is needed. 

We can also see that we are setting up the prisma connection to the PostgreSQL database however for this to work we need to get the port of that our PostgreSQL container is exposed to. We fetching the exposed port that the Testcontainer library dynamcly allocates for us by using the get_exposed_port function and use it to connect Prisma.

### Redis 
Here is how we setup the Redis container
```
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
    ```{{}}

    This works preaty much in the same way as the setup for PostgreSQL Testcontainer. We use a communuity module for redis and then fetch the allocated exposed port then start the redis Testcontainer. The setup function for setup_redis and setup_postgres_connection can be found in the [View file](backend-api/code/get.py){{open}}