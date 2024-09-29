from flask import Flask, json
import requests
from prisma import Prisma
import asyncio

prisma = None
app = Flask(__name__)

#fetches fact:
def retrieve_fact(type):
	r = requests.get(f"https://uselessfacts.jsph.pl/api/v2/facts/{type}")
	if r.status_code != 200:
		return "Page Not Found", 404  
	data_in_json = r.json()
	fact_id = data_in_json["id"]
	fact = data_in_json["text"]
	return (fact_id, fact)
	

@app.route('/api/today')
def today():
	(fact_id, fact) = retrieve_fact("today")
 
	
	return json.jsonify(
			fact_id=fact_id,
			fact=fact)

@app.route('/api/random')
async def random():
	(fact_id, fact) = retrieve_fact("random")
	
	await prisma.fact.upsert(
		where={
			'Fact_id': fact_id
		},
		data={
			'update': {
				'num_views': {
					'increment': 1
				}
			},
			'create': {
				'Fact_id': fact_id,
				'Fact': fact,
				'num_views': 1
			}
		}
	)

	return json.jsonify(
		fact_id=fact_id,
		fact=fact)

@app.route('/api')
def api_helth():
	return "OK", 200

async def create_prisma_client():
	global prisma 
	prisma = Prisma()
	await prisma.connect()


if __name__ == '__main__':
	asyncio.run(create_prisma_client())
	app.run(debug=True, port=8000)