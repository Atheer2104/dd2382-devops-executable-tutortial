Backend API Explanation

In this Step, you will learn more about:

1. The structure and components of our backend API
2. How to application is usually run using Docker scripts 
3. How to use TestContainers for testing

Let's get started!

## Main Components

1. **Flask Application (`get.py`):**
   - Sets up the Flask application
   - Defines API routes and their handlers
   - Manages interactions with external API and databases
   - Fetches todays random or some random fact 
   
2. **External API Integration:**
   - Fetches facts from `https://uselessfacts.jsph.pl/api/v2/facts/`

3. **Redis Caching:**
   - Caches the "fact of the day" to reduce external API calls
   - Implements expiration to ensure a new fact each day

4. **Database Integration (Prisma):**
   - Stores facts and their view counts
   - Uses upsert operations to update or add facts

## Setup Application

1. **Starting docker Scripts (`get.py`):**
    - `scripts/init_postgresql.sh`{{exec}} : Starts the PostgreSQL database container.
    - `scripts/init_redis.sh`{{exec}} : Starts the Redis containers. 

2. **Installing dependencies**
    -  `pip install -r requirements.txt`{{exec}} : The dependencies such as flask and Prisma needs to be installed. In this project 
    we chose Prisma as an ORM to handle the the communication with the database and simplify the operations.

3. **Setting up data model from Prisma schema** 
    -   `prisma migrate dev`{{exec}} : One of the features that prisma offers is that it allows us to configure the data model in the schema file and then this will be migrated to the data base and implemente the data model. 

4. **Starting Flask**
    -   `python code/get.py`{{exec}} : Start the flask web application


5. **Testing** 
    - `curl http://localhost:8000/today/`{{exec}} : 