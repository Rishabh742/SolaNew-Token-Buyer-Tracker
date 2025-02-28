
Step 8: Add Database Integration (PostgreSQL/SQLite)

      To avoid duplicate alerts, we need to store buyer data in a database. We will use PostgreSQL (for production) and SQLite (for local testing).

      Option 2: SQLite Setup (For local testing)

           SQLite doesn’t need a server—it’s just a file.

		import sqlite3

		def setup_database():
    
			conn = sqlite3.connect("solana_buyers.db")
    
			cursor = conn.cursor()
    
    		cursor.execute("""
    
		CREATE TABLE IF NOT EXISTS buyers (
        
		id INTEGER PRIMARY KEY AUTOINCREMENT,
        
		wallet_address TEXT UNIQUE NOT NULL,
        	
		balance REAL NOT NULL,
        
		first_seen TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    	      )
    	""")
    
   	 conn.commit()
    
	 conn.close()

	setup_database()