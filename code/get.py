from flask import Flask, json
import requests
from prisma import Prisma

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


def update_or_add_fact_to_db(fact_id, fact):
	prisma.fact.upsert(
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

@app.route('/api/today')
def today():
	(fact_id, fact) = retrieve_fact("today")
 
	update_or_add_fact_to_db(fact_id, fact)	
 
	return json.jsonify(
			fact_id=fact_id,
			fact=fact)

@app.route('/api/random')
def random():
	(fact_id, fact) = retrieve_fact("random")
	
	update_or_add_fact_to_db(fact_id, fact)

	return json.jsonify(
		fact_id=fact_id,
		fact=fact)

@app.route('/api')
def api_helth():
	return "OK", 200


if __name__ == '__main__':
	prisma = Prisma()
	prisma.connect()
	app.run(debug=True, port=8000)