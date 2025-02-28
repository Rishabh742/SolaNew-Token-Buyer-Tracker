
 Step 4: Identify the New Buyers

        Now, let's check if the buyer is new:

          (1) Extract the buyer’s wallet address.

          (2) Verify if it has only recently received Solana (indicating a new wallet).

          (3) Check if it has extra Solana left.

          def get_account_info(wallet_address):
           
              payload = {
                
                "jsonrpc": "2.0",

                "id": 1,

                "method": "getBalance",

                "params": [wallet_address]
    	      }
    
        response = requests.post(SOLANA_RPC_URL, json=payload)
    
        if response.status_code == 200:
        
		balance = response.json()["result"]["value"]

        		return balance / 1e9  # Convert from lamports to SOL
    	return 0

	wallet_address = "NEW_BUYER_WALLET_ADDRESS"
	balance = get_account_info(wallet_address)
	print(f"Wallet {wallet_address} has {balance} SOL")