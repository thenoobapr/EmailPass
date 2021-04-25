#main.py
from flask import Flask, jsonify
clients = [
	{
		"ID": 1,
		"Name": "Ravi Kumar",
		"Amount": "$10,000",
		"Mobile": "8766543880"
	},
	{
		"ID": 2,
		"Name": "Suresh Yadav",
		"Amount": "$5000",
		"Mobile": "9877615550"
	}
]
app = Flask(__name__)
@app.route("/")
def index():
	return "Hello world!"
@app.route("/library/v1.0/clients", methods=["GET"])
def get_clients():
	return jsonify({"clients": clients})
@app.route("/library/v1.0/clients/<int:client_id>", methods=["GET"])
def get_client(client_id):
	result = {}
	for client in clients:
		if client["id"] == client_id:
			result = jsonify({"client": client})
	return result
if __name__ == "__main__":
	app.run()
