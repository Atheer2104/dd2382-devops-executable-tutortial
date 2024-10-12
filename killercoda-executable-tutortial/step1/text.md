## Backend API Explanation

In this Step, you will learn more about:

1. The structure and components of the backend API to be tested against
2. How the backend API works 
3. How to run application

Let's get started!

## Main Components

The main components of the backend API are the following 

1. **Flask Application:** <br/>
The file at **code/get.py** contains all the functionallity which the backend API provides and it does the following 

	- Defines API routes and their handlers
We have three endpoints **/api** a healthpoint for the API and the remaning two endopoints are **/api/random** and **/api/today**, these are our service endpoint which we provide 

   - Sets up the Flask application   
   - Manages interactions with external API and databases
   
2. **External API Integration:** <br/>
Our backend API it provides *useless facts* and these come in two versions either a random fact which is retrieved at **/api/random**. The other version is "Fact of The Day" which is retrieved at **/api/today**. These facts are retrieved from another external API, more details found [here](https://uselessfacts.jsph.pl)

3. **Redis Caching:**
   - "Fact of The Day" is Cached using Redis to reduce external API calls
   - The cached fact will expire at midnight to ensure consistency
4. **PostgreSQL Database:**
	- Stores facts together with a view count
	- Uses upsert operations to update or add facts

## Setup Backend API

Now we will setup & start the backend API using following steps

1. **Starting docker Scripts:** <br/>
These scripts are used to start a postresql and a redis container that are used by the backend API
    - `scripts/init_postgresql.sh`{{exec}}
    - `scripts/init_redis.sh`{{exec}}


2. **Installing dependencies** <br/>
The dependencies such as flask and Prisma needs to be installed. In this project we chose Prisma as an ORM to handle the the communication with the database and simplify the operations.
    -  `pip install -r requirements.txt`{{exec}}

3. **Setting up data model from Prisma schema** <br/>
Prisma it supports migrations which allows using a single command setup the entire postgresql database when it comes to creating the tables and columns.
    -   `prisma migrate dev`{{exec}}

4. **Starting Backend API**<br/>
Now we will start the backend API which is a flask application 
    -   `python code/get.py`{{exec}}

5. **Endpoint Testing** <br/>
Now we can test our endpoints by sending the following http request to the backend API, open a new terminal and run run the following commands 
    - `curl http://localhost:8000/api`{{exec}}
	- `curl http://localhost:8000/api/today`{{exec}}
	- `curl http://localhost:8000/api/random`{{exec}}