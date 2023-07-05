from web3 import Web3
from web3.middleware import geth_poa_middleware
import sys
import json
import time

local_blockchain_url = "http://127.0.0.1:8545"
web3 = Web3(Web3.HTTPProvider(local_blockchain_url))
web3.middleware_onion.inject(geth_poa_middleware, layer=0)

contract_address = Web3.to_checksum_address("0xe466b03c36b7a39eae227c994788c92722992947")
abi_json_file = '/Users/wuxiuyuan/build/contracts/VisualizationRegistry.json'

def load_abi(abi_file):
    with open(abi_file) as f:
        abi = json.load(f)
    return abi['abi']

def register_visualization(account_address, visualization_name, image_hash):
    abi = load_abi(abi_json_file)
    contract = web3.eth.contract(address=contract_address, abi=abi)
    
    # Check if the hash already exists in the contract
    is_registered = contract.functions.registerVisualization(
        account_address,
        visualization_name,
        bytes.fromhex(image_hash)
    )
    if is_registered:
        print("Hash already registered. Skipping registration.")
        return
    
    nonce = web3.eth.get_transaction_count(account_address)

    txn_function = contract.functions.registerVisualization(account_address, visualization_name, bytes.fromhex(image_hash))
    txn = txn_function.buildTransaction({
        'chainId': 1,
        'gas': 100000,
        'gasPrice': 1,
        'nonce': nonce,
    })

    signed_txn = web3.eth.account.sign_transaction(txn, private_key=private_key)

    tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)
    
    print(f'Transaction hash: {tx_hash.hex()}')

    print('Waiting for transaction to be mined...')
    while True:
        txn_receipt = web3.eth.get_transaction_receipt(tx_hash)
        if txn_receipt is not None:
            break
        time.sleep(3)  # wait before retrying

    print(f'Transaction status: {"Successful" if txn_receipt["status"] == 1 else "Failed"}')
if __name__ == "__main__":
    image_hash = sys.argv[1]
    private_key = "0x4985ebabcf2eb9555f2c557b83dc5c57f51c49ad77d6fcf4ba66a54d4f4b38c9"
    account = web3.eth.account.from_key(private_key)
    visualization_name = "my visualization"
    register_visualization(account_address=account.address, visualization_name=visualization_name, image_hash=image_hash)

