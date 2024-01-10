# Train-Delay-Bot

TrainDelayBot is a Discord bot designed to provide real-time train delay information based on user commands. The bot utilizes data from the Polish State Railways (PKP Intercity) website through web scraping using Selenium and a web driver. It is built using the Discord library for Python and the Responses library for handling message interactions.

## Features
- **Real-time Train Delay Information:** Get instant updates on train delays by using the bot's commands.

- **Default Route:** The bot responds to the !delay command by defaulting to the route between Wronki and Poznań Główny, providing delay information for this route.

- **Custom Routes:** Users can use the !delay FROM TO command to specify departure and arrival stations and receive train delay information for the specified route.

- **Help Command:** Use the !help command to receive a list of available commands and their functionalities.

## Implementation Details
- **Web Scraping with Selenium:** TrainDelayBot employs the Selenium library and a web driver to extract real-time train delay information from the PKP Intercity website.

- **Discord Integration:** The bot utilizes the Discord library for Python to handle message interactions and respond to user commands.

## Usage
Example usage

![image](https://user-images.githubusercontent.com/92379328/234039247-010f88ef-863d-4d66-a84a-7414e0b967d2.png)


