
Step 8: Add Database Integration (PostgreSQL/SQLite)

      To avoid duplicate alerts, we need to store buyer data in a database. We will use PostgreSQL (for production) and SQLite (for local testing).

       Step 8.1: Set Up the Database

	Option 1: PostgreSQL Setup (Recommended for production)

           1. Install PostgreSQL

	     Windows: Install from postgresql.org

	     Linux/Mac: Use Homebrew or apt install postgresql


           2. Create a Database & Table


		CREATE DATABASE solana_tracker;
		\c solana_tracker;

		CREATE TABLE buyers (
    			id SERIAL PRIMARY KEY,
    
			wallet_address TEXT UNIQUE NOT NULL,
    
			balance DECIMAL NOT NULL,
    
			first_seen TIMESTAMP DEFAULT CURRENT_TIMESTAMP
		);