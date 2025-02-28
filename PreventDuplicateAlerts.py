
Step 8.3: Prevent Duplicate Alerts

	Before sending alerts, check if the wallet is already stored.

	Modify the Alert Function

	def is_new_buyer(wallet):
    
		conn = sqlite3.connect("solana_buyers.db")
    
		cursor = conn.cursor()

    	cursor.execute("SELECT * FROM buyers WHERE wallet_address = ?", (wallet,))
    
	result = cursor.fetchone()

    	conn.close()
    
	return result is None