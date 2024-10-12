## Testing using Testcontainers 

In this Step, you will learn more about:

1. How the Testcontainers is setup in python to test the backend API
2. How the get the exposed port of the containers created by Testcontainers
3. How the Testcontainers library works in python

Let's get started!

## How Testing is performed 

We have two tests namely **test_data_access_random_endpoint** and **test_data_access_today_endpoint**. We are using pytest to run these test hence they start with the name test that is how pytest will identifiy which test functions to execute.

The latter test function tests the random endpoint by calling the endpoint and getting the fact id which is returned in the Json response.Then it checks that in the postgreSQL database there exists such a row because we are saving the fact together with their view count in PostgresSQL.

The former test function tests the today endpoint by clal



## How Testcontainers is Integrated into the tests 

As mentioned Testcontainers allow us to spin up dockercontainers for our services such as redis and PostgreSQL. These are needed to implement our pytest testcases on the the data insertion and checking that the stored data is accessable.    

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

### Redis 

