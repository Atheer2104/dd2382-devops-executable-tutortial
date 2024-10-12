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



### PostgresSql

### Redis 

