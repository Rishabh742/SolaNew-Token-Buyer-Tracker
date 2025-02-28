

 Step 3: Getting up the Solana Blockchain Data

        To track new token purchases, we need:

          (1) A Solana RPC API (Use public RPCs like QuickNode, Alchemy, or Solana RPC)

          (2) A way to fetch recent transactions.

       Example of API to Fetch Transactions:

            import requests

          SOLANA_RPC_URL = "https://api.mainnet-beta.solana.com"

          def get_recent_transactions():
          
          payload = {
        
              "jsonrpc": "2.0",

              "id": 1,

              "method": "getSignaturesForAddress",

              "params": ["TOKEN_ADDRESS_HERE", {"limit": 10}]
          }
    
       response = requests.post(SOLANA_RPC_URL, json=payload)
    
       if response.status_code == 200:
            
            return response.json()["result"]
       else:
        
            return []
    
       transactions = get_recent_transactions()

       print(transactions)

       (3) Replace "TOKEN_ADDRESS_HERE" with the actual token contract address.

       (4) This fetches the latest transactions related to a token.