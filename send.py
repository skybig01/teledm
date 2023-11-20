import csv
import tracemalloc
import asyncio
from telegram import Bot

# Enable tracemalloc and start tracking memory allocations
tracemalloc.start()

# Telegram Bot API token
bot_token = '6207729556:AAGkD6STkqNMG9fdHe9WsxgJFJRpgENgHpc'

# Message to send to each member
message = 'Hello! This is a message sent to all members.'

async def send_messages():
    bot = Bot(token=bot_token)

    # Read members' data from the CSV file
    with open('members.csv', 'r', encoding='UTF-8') as f:
        reader = csv.reader(f)
        next(reader)  # Skip the header row
        for row in reader:
            user_id = row[1]  # Assuming the user ID is in the second column
            await bot.send_message(chat_id=user_id, text=message)  # Await the coroutine

    # Stop tracking memory allocations
    snapshot = tracemalloc.take_snapshot()
    top_stats = snapshot.statistics('lineno')

    # Print the traceback of object allocation
    for stat in top_stats:
        print(stat)

    print('Message sent to all members successfully.')

# Call the async function using asyncio.run()
asyncio.run(send_messages())
