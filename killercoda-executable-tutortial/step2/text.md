## How the Testcontainers is setup in the backend API (Theory)

In this Step, you will learn more about:

1. How the Testcontainers is setup in Python to test the backend API
2. How to get the exposed port of the containers created by Testcontainers
3. How the Testcontainers library works in Python

Let's get more started!

## How Testing is Performed 

We have two tests namely **test_data_access_random_endpoint** and **test_data_access_today_endpoint**. We are using pytest to run these tests hence they start with the name test that is how pytest will identify which test functions to execute.

The former test function tests the random endpoint by calling the respective endpoint function and getting the fact id returned in the JSON response. Then it checks that in the PostgreSQL database, there exists such a row with the same fact id because we are saving the fact and fact id together with the view count in PostgreSQL.

The latter test function tests the today endpoint by calling the respective endpoint function, it also gets the fact id and checks the same thing as the previous test when it comes to PostgreSQL but this endpoint caches the fact to Redis so the test also checks in Redis that fact is available and the value is equal to the fact received from the endpoint. Finally, it also checks that the cached fact in Redis has an expiration date.

## How Testcontainers are Integrated Into The Tests 
As mentioned Testcontainers allow us to spin up containers for our services such as Redis and PostgreSQL. These are needed to implement our pytest test cases on the data insertion and check that the stored data is accessible.    

As specified earlier one can start a GenericContainer in Testcontainers and in the python library for Testcontainers, this is known as DockerContainer("X"), here X refers to the name of the docker image, more info about how this looks like is [here](https://testcontainers-python.readthedocs.io/en/latest/core/README.html). Since we are using well-known services we are not using GenericContainer instead we are using modules that are provided by Testcontainers, A list of the available modules in Python is found [here](https://testcontainers-python.readthedocs.io/en/latest/modules/index.html)

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

Notice that we set up the testcontainer in the pytest fixture to ensure that when we run the test cases the containers are up and running before we try to store and access anything. We also use this fixture once per session, so that we use the same storage instance for all our test cases however we can use different storage instances if that is needed. 

We are creating the PostgreSQL container with the image **postgres:bullseye** and we are then defining some environment configuration for PostgreSQL like the name and password of the database together with the database name, you can also see that we have set the driver to None because we don't want any driver. After starting the container we are fetching the exposed port that the Testcontainer library dynamically allocates for us by using the **get_exposed_port** function and using it to connect Prisma and running the migrations in another subprocess.

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

This works pretty much in the same way as the setup for PostgreSQL testcontainer, but now we are using a Redis container with the image being **redis:7.4-rc2-bookworm** then we are starting the container. Also here we need to get the exposed port so that we can set up a connection to the Redis instance.  

