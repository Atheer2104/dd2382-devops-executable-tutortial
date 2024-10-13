## Setup Backend API (Practical)

In this Step, you will learn more about:

1. How to setup the backend API
2. How to run the backend API

Let's get started!

Now we will setup & start the backend API, we have setup an empty virtual environment for you already and activated it so we continue on with the following steps 

1. **Installing dependencies** <br/>
The dependencies such as Flask and Prisma needs to be installed. In this project we chose Prisma as an ORM to handle the the communication with the database to simplify the operations.
	-  `pip install -r requirements.txt`{{exec}}

2. **Starting docker Scripts:** <br/>
These scripts are used to start a PostgreSQL and a Redis container that are used by the backend API
	- `scripts/init_postgresql.sh`{{exec}}
	- `scripts/init_redis.sh`{{exec}}

3. **Setting up data model from Prisma schema** <br/>
Prisma it supports migrations which allows using a single command to setup the entire PostgreSQL database when it comes to creating the tables and columns.
	-   `prisma migrate dev`{{exec}}

4. **Starting Backend API**<br/>
Now we will start the backend API which is a Flask application 
	-   `python code/get.py`{{exec}}

5. **Endpoint Testing** <br/>
Now we can test our endpoints by sending the following http request to the backend API, **open a new terminal and run run the following commands**, You should be able to see reponse from the API

	- `curl http://localhost:8000/api`{{exec}}
	- `curl http://localhost:8000/api/today`{{exec}}
	- `curl http://localhost:8000/api/random`{{exec}}