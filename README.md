# PlexInformer Project

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Configuration](#configuration)
- [Installation](#installation)
  - [Local Installation](#local-installation)
  - [Docker Installation](#docker-installation)
- [Creating a Discord Bot](#creating-a-discord-bot)
- [Commands](#commands)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

PlexInformer is a Discord bot designed to fetch and display statistics from a Tautulli server, such as the total number of movies and TV shows. It includes commands for on-demand stats and total user count.

## Features
- Fetch and display the total number of movies and TV shows.
- Command to fetch and display the total number of users.
- Scheduled daily stats posting.
- User authentication and authorization.

## Technologies Used
- **Backend:** Python, Discord.py
- **API:** Tautulli API
- **Deployment:** Docker or locally

## Configuration

The configuration settings are located in the `.env` file. Key settings include:
- **TAUTULLI_URL:** Your Tautulli server URL.
- **TAUTULLI_API_KEY:** Your Tautulli API key.
- **DISCORD_BOT_TOKEN:** Your Discord bot token.
- **DISCORD_BOT_PREFIX:** The command prefix for the bot.

## Installation

### Local Installation
To set up the project locally, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/consultomer/PlexInformer.git
   cd PlexInformer
2. **Create and activate a virtual environment::**
   ```bash
   python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
3. **Install the dependencies::**
   ```bash
   pip install -r requirements.txt
4. **Run the application:**
   ```bash
   python3 main.py
### Docker Installation 
1. **Clone the repository:**
   ```bash
   git clone https://github.com/consultomer/PlexInformer.git
   cd PlexInformer
2. **Build Docker Image:**
   ```bash
   docker build -t plexinformer:0.0.1 .
   docker run -dit --name plexinformer --restart unless-stopped plexinformer:0.0.1
3. **Start the Docker container:**
   ```bash   
   docker start plexinformer
## Creating a Discord Bot
To create a Discord bot, follow these steps:

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications).
2. Click on "New Application" and give your application a name.
3. Go to the "Bot" tab and click "Add Bot."
4. Copy the bot token; you'll need it for your `.env` file.
5. In the "Bot" settings, enable the following intents:
   - **Presence Intent:** Required for your bot to receive Presence Update events.
   - **Server Members Intent:** Required for your bot to receive events listed under GUILD_MEMBERS.
   - **Message Content Intent:** Required for your bot to receive message content in most messages.

   **Note:** Once your bot reaches 100 or more servers, you will need verification and approval for these intents.

## Commands
After running the application, you can invite the bot to your server and use the following commands:

- **`!stats`**: Fetch and display the total number of movies and TV shows.
- **`!totalusers`**: Fetch and display the total number of users.

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes. Ensure that your code adheres to the project's coding standards and passes all tests.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For any questions or support, please contact:

- **Omer Abdulrehman**
- **Email:** [consultomer@gmail.com](mailto:consultomer@gmail.com)
- **LinkedIn:** [Omer Abdulrehman](https://www.linkedin.com/in/omerarehman/)