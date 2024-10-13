## Testing using Testcontainers (Practical)

In this Step, you will show you how:

1. How the Testcontainers installed in Python
2. How to get the PostgreSQL and Redis Testcontainers modules installed in Python
3. How to run the tests!

Let's get even more started!

## Testcontainers installation

1. **Installing testcontainers:** <br/>
We need to install the testcontainers library with following commnad
	- `pip install testcontainers`{{exec}}

2. **Installing the postgress and redis testcontainers:** <br/>
We also need to make sure the the specific Testcontainers modules which we are using are installed, because they are not installed by default. These can be installed by following commands
	- `pip install testcontainers[postgres]`{{exec}}
	- `pip install testcontainers[redis] `{{exec}}

3. **Run the tests:** <br/>
Use pytest to start the execution of the testcases, then pray everything is green 
	- `pytest code/test_cases.py`{{exec}}
