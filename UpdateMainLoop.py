
Step 8.3: Prevent Duplicate Alerts

	Before sending alerts, check if the wallet is already stored.

	Update Main Loop

	for buyer in eligible_buyers:
    
		wallet, balance = buyer
    
	if is_new_buyer(wallet):  # Only send alerts for new buyers
        
		send_telegram_alert(wallet, balance)
        
		asyncio.run(send_discord_alert(wallet, balance))
        
		save_buyer(wallet, balance)