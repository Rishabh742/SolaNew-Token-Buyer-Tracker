
Step 6: Send Alerts (Telegram / Discord)

      Once we find a potential whale, send instant alerts.

     1. Telegram Alert

	from telegram import Bot

	TELEGRAM_BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

	TELEGRAM_CHAT_ID = "YOUR_CHAT_ID"

	def send_telegram_alert(wallet, balance):
    
		bot = Bot(token=TELEGRAM_BOT_TOKEN)
    
		message = f"🚀 New Buyer Alert!\nWallet: {wallet}\nExtra SOL Left: {balance}"
    
		bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)

	for buyer in eligible_buyers:
    
		send_telegram_alert(buyer[0], buyer[1])


      2. Discord Alert

	 import discord

	 import asyncio

	 DISCORD_WEBHOOK_URL = "YOUR_DISCORD_WEBHOOK_URL"

	 async def send_discord_alert(wallet, balance):
    
		webhook = discord.SyncWebhook.from_url(DISCORD_WEBHOOK_URL)

   		message = f"🚀 **New Buyer Alert!**\n\n🔹 **Wallet:** {wallet}\n🔹 **Extra SOL Left:** {balance}"

   		webhook.send(message)

	 for buyer in eligible_buyers:
   
	 asyncio.run(send_discord_alert(buyer[0], buyer[1]))