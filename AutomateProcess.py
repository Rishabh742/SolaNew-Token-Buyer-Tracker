
Step 7: Automate the Process

      To continuously track new buyers, run the script every few minutes using a scheduler.

        Using a Simple Infinite Loop

           import time

	   while True:
    
	     transactions = get_recent_transactions()
    
	     eligible_buyers = filter_new_buyers(transactions)
    
    	   for buyer in eligible_buyers:
        	send_telegram_alert(buyer[0], buyer[1])
        
		asyncio.run(send_discord_alert(buyer[0], buyer[1]))
    
    	   print("Checked transactions. Waiting for next run...")
    
	   time.sleep(300) 