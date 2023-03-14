import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

    # Set the time to 10AM
    target_time = datetime.time(hour=10, minute=0, second=0)

    while True:
        current_time = datetime.datetime.now().time()
        # Check if it's 10AM
        if current_time.hour == target_time.hour and current_time.minute == target_time.minute:
            # Get the channel where the message will be sent
            channel = client.get_channel(channel_id_here)
            # Send the message
            await channel.send('Hello Landonia!!')

        # Wait for 1 minute before checking the time again
        await asyncio.sleep(60)

# Login the bot using your bot token
client.run('your_bot_token_here')
