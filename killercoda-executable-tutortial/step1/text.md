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
