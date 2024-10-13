## Testing using Testcontainers (Practical)

In this Step, you will show you how:

1. How the Testcontainers installed in Python
2. How to get the PostgreSQL and Redis Testcontainers modules installed in Python
3. How to run the tests!

Let's get even more started!

## Testcontainers installation

1. **Installing Testcontainers Library:** <br/>
We need to install the Testcontainers library in Python with the following command
	- `pip install testcontainers`{{exec}}

2. **Installing the PostgreSQL and Redis Testcontainers modules:** <br/>
We also need to make sure the specific Testcontainers modules which we are using are installed, because they are not installed by default. These can be installed by following the commands
	- `pip install testcontainers[postgres]`{{exec}}
	- `pip install testcontainers[redis] `{{exec}}

3. **Run the tests:** <br/>
Use pytest to start the execution of the test cases, it will take a few seconds but we should see that our two tests pass.
	- `pytest code/test_cases.py`{{exec}}
