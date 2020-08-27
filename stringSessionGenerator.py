import asyncio
from pyrogram import Client

print("============================================================")
print("String Session Generator for SpamProtectionAgent userbot")
print("------------------------------------------------------------")
print()
print("This Python script will help you generate an session string that needed")
print("for running this userbot. You'll need your Telegram API app ID and hash")
print("in order for the session string to be generated.")
print()
print("If you don't have app ID and hash, you can get one from")
print("https://my.telegram.org/apps. By using this script, you agree to")
print("the API terms at https://core.telegram.org/api/terms.")
print()
print("============================================================")

APP_ID = int(input("Please enter your Telegram API app ID: "))
API_HASH = input("Please enter your Telegram API app hash: ")


async def main(api_id, api_hash):
    """generate StringSession for the current MemorySession"""
    async with Client(":memory:", api_id=api_id, api_hash=api_hash) as app:
        print(app.export_session_string())

if __name__ == "__main__":
	loop = asyncio.get_event_loop()
	loop.run_until_complete(main(APP_ID, API_HASH))