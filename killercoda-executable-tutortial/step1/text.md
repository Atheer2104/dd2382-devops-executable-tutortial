## Backend API Explanation

In this Step, you will learn more about:

1. The structure and components of the backend API to be tested against
2. How the backend API works 
3. How to run the backend API

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
   - "Fact of The Day" is Cached using Redis to reduce external API calls, since it's the same fact
   - The cached fact will expire at midnight to ensure consistency
4. **PostgreSQL Database:**
	- Stores facts together with a view count
	- Uses upsert operations to update or add facts

## Setup Backend API

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