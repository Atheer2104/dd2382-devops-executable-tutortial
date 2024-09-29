from flask import Flask, json
import requests

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
def random():
	(fact_id, fact) = retrieve_fact("random")

	return json.jsonify(
		fact_id=fact_id,
		fact=fact)

@app.route('/api')
def api_helth():
	return "OK", 200

@app.route('/')
def index():
	return "Hello", 200

if __name__ == '__main__':
	app.run(debug=True, port=8000)