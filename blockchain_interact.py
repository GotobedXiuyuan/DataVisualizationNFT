from web3 import Web3
import sys
import json

# you need to replace 'infura_project_id' with your actual Infura Project ID
infura_url = "https://mainnet.infura.io/v3/infura_project_id" 
web3 = Web3(Web3.HTTPProvider(infura_url))

# replace 'private_key' with your Ethereum account private key
private_key = "0x2f75ee973c8a5da24942929bcb98133b0538753ee265feb9f95086ead309983d"

# replace 'contract_address' with the address of your deployed smart contract
contract_address = "0x5BeBC0B388aAA2075c3189420bdBFCD84c9cA463"

# replace 'abi_json_file' with the path to your contract's ABI JSON file
abi_json_file = 'abi.json'

def load_abi(abi_file):
    with open(abi_file) as f:
        abi = json.load(f)
    return abi

def register_visualization(image_hash):
    abi = load_abi(abi_json_file)
    contract = web3.eth.contract(address=contract_address, abi=abi)
    
    nonce = web3.eth.getTransactionCount(web3.eth.defaultAccount)

    txn = contract.functions.registerVisualization(image_hash).buildTransaction({
        'chainId': 1,
        'gas': 70000,
        'gasPrice': web3.toWei('1', 'gwei'),
        'nonce': nonce,
    })

    signed_txn = web3.eth.account.signTransaction(txn, private_key=private_key)

    tx_hash = web3.eth.sendRawTransaction(signed_txn.rawTransaction)
    
    return tx_hash.hex()

if __name__ == "__main__":
    image_hash = sys.argv[1]
    print(register_visualization(image_hash))
