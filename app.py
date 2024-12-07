from flask import Flask, request, jsonify
from web3 import Web3
from flask_cors import CORS
from flask import json

app = Flask(__name__)
CORS(app)

ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))
web3.eth.default_account = web3.eth.accounts[0]

with open("food_donation_platform/build/contracts/ChristmasAid.json") as f:
    contract_data = json.load(f)

abi = contract_data["abi"]
address = contract_data["networks"]["5777"]["address"]

contract = web3.eth.contract(address=address, abi=abi)

@app.route("/donate", methods=["POST"])
def donate():
    data = request.json
    try:
        tx_hash = contract.functions.donate().transact({
            "from": data["address"],
            "value": web3.to_wei(data["amount"], "ether")
        })
        web3.eth.wait_for_transaction_receipt(tx_hash)
        return jsonify({"message": "Donation successful!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/recipients", methods=["POST"])
def add_recipient():
    data = request.json
    tx_hash = contract.functions.addRecipient(data["address"]).transact()
    web3.eth.wait_for_transaction_receipt(tx_hash)
    return jsonify({"message": "Recipient added!"})

@app.route("/distribute", methods=["POST"])
def distribute():
    tx_hash = contract.functions.distributeFunds().transact()
    web3.eth.wait_for_transaction_receipt(tx_hash)
    return jsonify({"message": "Funds distributed!"})

if __name__ == "__main__":
    app.run(debug=True)
