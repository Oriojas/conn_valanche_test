import os
import json
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()

with open("artifacts/Saludo_metadata.json") as f:
    info_json = json.load(f)

ABI = info_json["output"]["abi"]

CONTRACT = "0x4B5Eb373E929f6A5475C2bd1cf91bd756FA4eE4F"
WALLET = os.environ["WALLET"]
PRIV_KEY = os.environ["PRIV_KEY"]

avalanche_rpc_url = "https://avalanche-fuji.blockpi.network/v1/rpc/public"

w3 = Web3(Web3.HTTPProvider(avalanche_rpc_url))

if w3.is_connected():
    print("-" * 50)
    print("Connected to Avalanche RPC endpoint")
    print("-" * 50)
    print(w3.eth.block_number)
    print("-" * 50)
    balance = w3.eth.get_balance(WALLET)
    print("-" * 50)
    print(f"Wallet balance: {w3.from_wei(balance, 'ether')} AVAX")
    print("-" * 50)

else:
    print("-" * 50)
    print("Failed to connect to Avalanche RPC endpoint")
    print("-" * 50)

contract_address = CONTRACT
contract_abi = ABI

contract = w3.eth.contract(address=contract_address,
                           abi=contract_abi)

result = contract.functions.leerSaludo().call()

print(result)

function_data = contract.functions.guardarSaludo({"Saludo 9 desde Python"}).build_transaction({
    "from": WALLET,
    "gas": 2000000,
    "maxFeePerGas": w3.to_wei('35', 'gwei'),
    "maxPriorityFeePerGas": w3.to_wei('2', 'gwei'),
    "nonce": w3.eth.get_transaction_count(WALLET),
    "chainId": 43113,
})

signed_transaction = w3.eth.account.sign_transaction(function_data, PRIV_KEY)
transaction_hash = w3.eth.send_raw_transaction(signed_transaction.raw_transaction)

print("-" * 50)
print(f"Transaction hash: {transaction_hash.hex()}")
print("-" * 50)

result2 = contract.functions.leerSaludo().call()

print("-" * 50)
print(f"Nuevo Saludo: {result}")
print("-" * 50)