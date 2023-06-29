# DataVisualizationNFT
1. Develop and Deploy the Smart Contract
First, you'll need to write the smart contract in Solidity. You've already developed the VisualizationRegistry.sol smart contract for this purpose.
Next, deploy this contract to the blockchain using Truffle. In your terminal, you can do this with the command truffle migrate. Remember to have your local blockchain (like Ganache) running before attempting to deploy.
2. Locate Contract Address and Private Key
After successfully deploying the contract, the contract address will be printed in the terminal.
Also, in the build/contracts directory of your Truffle project, you'll find a JSON file named VisualizationRegistry.json. Inside this file, under the "networks" field, you'll find the contract address.
To find the private key, check the accounts provided by your local blockchain (Ganache). Ganache shows the private keys of the available accounts in its GUI or terminal output.
3. Prepare the Python Scripts
Now you have to write two Python scripts, hash_generator.py and register_visualization.py.
The hash_generator.py script will take an input file and generate a SHA-256 hash for it.
The blockchain_interact.py script will interact with your deployed smart contract and call the registerVisualization function. It will use the hash generated by hash_generator.py as an argument.
Remember to replace the placeholders in these scripts (private_key and contract_address) with the actual private key of your account and the address of the deployed contract.
4. Generate the Hash
Execute the hash_generator.py script by providing the visualization file as an argument. This will generate the SHA-256 hash for your visualization file. Remember to write down the hash or keep the terminal open as you will need it for the next step.
5. Register the Visualization
Next, execute the blockchian_interact.py script. It will interact with the blockchain, specifically with your deployed contract, and call the registerVisualization function with the previously generated hash.
If everything is successful, your visualization is now registered on the blockchain, and the hash is associated with your Ethereum account.