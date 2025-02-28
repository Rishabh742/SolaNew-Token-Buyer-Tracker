
Step 5: Filter Eligible Buyers

       Now, let's filter buyers who:

          (1) Just bought the token for the first time.

          (2) Have extra Solana in their account.

          def filter_new_buyers(transactions):
    
            new_buyers = []
    
    	    for tx in transactions:
        
		buyer_wallet = tx['owner']  # Assuming 'owner' key contains wallet address
        
		sol_balance = get_account_info(buyer_wallet)

            if sol_balance > 5:  # Adjust threshold based on preference
            
		new_buyers.append((buyer_wallet, sol_balance))

    	    return new_buyers

	eligible_buyers = filter_new_buyers(transactions)

	print(eligible_buyers)