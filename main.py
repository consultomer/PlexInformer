import requests
import discord
import os
from discord.ext import tasks, commands
from datetime import time


# Configuration
tautulli_url = os.environ.get("TAUTULLI_URL")
tautulli_api = os.environ.get("TAUTULLI_API_KEY")

# Configuration for Jellyfin
jelly_url = os.environ.get("JELLY_URL")
jelly_api = os.environ.get("JELLY_API_KEY")
# Configuration for Discord Bot
token = os.environ.get("DISCORD_BOT_TOKEN")
prefix = os.environ.get("DISCORD_BOT_PREFIX")


intents = discord.Intents.default()
intents.message_content = True  # Ensure this is set to True to receive message content
intents.guilds = True  # Needed for guild/channel management

# Create an instance of a Bot with the specified intents
bot = commands.Bot(command_prefix=prefix, intents=intents)


def get_jelly_users():
    """Fetches the list of Jellyfin users from the Jellyfin API."""
    headers = {
        "X-Emby-Token": f"{jelly_api}",
        "Accept": 'application/json, profile="PascalCase"',
    }
    try:
        response = requests.get(f"{jelly_url}/users", headers=headers)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Jellyfin users: {e}")
        return []


def get_tautulli_stats(endpoint, params=None):
    """
    Function to fetch stats from Tautulli API.

    :param endpoint: The API endpoint to query.
    :param params: Additional parameters for the API request.
    :return: JSON response from the API.
    """
    url = f"{tautulli_url}/api/v2"
    params = params or {}
    params.update({"apikey": tautulli_api, "cmd": endpoint})

    response = requests.get(url, params=params)
    response.raise_for_status()  # Raise an error on bad status
    return response.json()


async def fetch_and_send_stats(channel):
    """Fetch Tautulli stats and send them to the Discord channel."""

    # Fetching library sections
    library_sections = get_tautulli_stats("get_libraries")

    # Fetching total number of movies and TV shows
    total_movies = 0
    total_tv_shows = 0
    for section in library_sections["response"]["data"]:
        if section["section_type"] == "movie":
            data = int(section["count"])
            total_movies += data
        elif section["section_type"] == "show":
            data = int(section["count"])
            total_tv_shows += data

    # Constructing the message
    stats_message = (
        f"Total Number of Movies: {total_movies}\n"
        f"Total Number of TV Shows: {total_tv_shows}"
    )

    # Sending the stats to the channel
    await channel.send(stats_message)


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
    guild = discord.utils.get(bot.guilds)  # Get the first guild the bot is connected to
    if guild:
        channel = discord.utils.get(
            guild.text_channels, name="🎥・library"
        )  # Replace with your channel name
        if channel:
            await fetch_and_send_stats(channel)
            send_daily_stats.start(channel)  # Start the daily task


@bot.command(name="stats")
async def stats_command(ctx):
    """Command to fetch and send Tautulli stats on demand."""
    await fetch_and_send_stats(ctx.channel)


@bot.command(name="totalusers")
async def total_users_command(ctx):
    """Command to fetch and send the total number of users."""
    users_stats = get_tautulli_stats("get_users")
    plex_users = len(users_stats["response"]["data"])
    jelly_users = len(get_jelly_users())
    stats_message = (
        f"Total Number of Plex Users: {plex_users}\n"
        f"Total Number of Jelly Users: {jelly_users}\n"
        f"Total Number of Users: {plex_users + jelly_users}"
    )
    await ctx.send(stats_message)


@tasks.loop(time=time(0, 0, 0))  # Runs daily at midnight
async def send_daily_stats(channel):
    """Task to send Tautulli stats daily at midnight."""
    await fetch_and_send_stats(channel)


@send_daily_stats.before_loop
async def before_send_daily_stats():
    await bot.wait_until_ready()


# Run the bot with the specified token
bot.run(token)
