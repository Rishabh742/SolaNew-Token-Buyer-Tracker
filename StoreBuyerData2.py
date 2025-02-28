
Step 8.2: Store Buyer Data

        Now, let's save new buyers in the database.

        For SQLite

		def save_buyer(wallet, balance):
    
			conn = sqlite3.connect("solana_buyers.db")
    
			cursor = conn.cursor()

    		cursor.execute("""
    
		INSERT OR IGNORE INTO buyers (wallet_address, balance) VALUES (?, ?)
    
			""", (wallet, balance))

   		 conn.commit()
    
		 conn.close()

	  for buyer in eligible_buyers:
    
	  	save_buyer(buyer[0], buyer[1])