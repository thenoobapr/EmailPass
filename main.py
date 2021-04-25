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
	},
	{
		"ID": 3,
		"Name": "Mallesh goud",
		"Amount": "$14,000",
		"Mobile": "8766543321"
	},
	{
		"ID": 4,
		"Name": "Bipin Choudhary",
		"Amount": "$15,000",
		"Mobile": "9877564442"
	}
]
app = Flask(__name__)
@app.route("/")
def index():
	return "Code Is Working Fine"
@app.route("/library/clients", methods=["GET"])
def get_clients():
	return jsonify({"clients": clients})
@app.route("/library/clients/<int:client_id>", methods=["GET"])
def get_client(client_id):
	result = {}
	for client in clients:
		if client["id"] == client_id:
			result = jsonify({"client": client})
	return result
if __name__ == "__main__":
	app.run()
