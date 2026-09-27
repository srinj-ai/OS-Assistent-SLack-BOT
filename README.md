# OS-Assistent-SLack-BOT

A Slack bot built with Node.js and [Slack Bolt for JavaScript](https://slack.dev/bolt-js) that provides helpful utility commands and interactive tools within your Slack workspace.

## Preview

![OS Assistant Slack Bot Commands](.assets/image.png)

## Features

- **Ping & Latency Check**: Measures bot response latency instantly.
- **Personalized Greeting**: Greets users directly with their name/username.
- **Server Time**: Displays the current server date and time.
- **Decision Maker**: Randomly/optionally picks choices provided by the user.
- **Jokes**: Delivers quick developer jokes.
- **Help Menu**: Lists all available slash commands and descriptions.

## Prerequisites

- [Node.js](https://nodejs.org/) (v18 or higher recommended)
- A Slack workspace with permissions to install/create Slack Apps.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/srinj-ai/OS-Assistent-SLack-BOT.git
   cd OS-Assistent-SLack-BOT
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

## Configuration

1. Create a `.env` file in the root directory based on `.env.example`:
   ```bash
   cp .env.example .env
   ```

2. Configure your Slack App credentials in `.env`:
   ```env
   SLACK_BOT_TOKEN=xoxb-your-bot-token
   SLACK_APP_TOKEN=xapp-your-app-token
   ```

   - `SLACK_BOT_TOKEN`: Bot User OAuth Token (`xoxb-...`) with necessary scopes (e.g., `commands`).
   - `SLACK_APP_TOKEN`: App-Level Token (`xapp-...`) with `connections:write` scope enabled for Socket Mode.

## Usage

Start the bot server:

```bash
node index.js
```

Or for development:
```bash
npm start
```

## Available Commands

| Command | Description | Example Usage |
| --- | --- | --- |
| `/osass-ping` | Check bot latency and response time | `/osass-ping` |
| `/osass-hello` | Get a personalized greeting | `/osass-hello` |
| `/osass-help` | Display list of available commands and usage info | `/osass-help` |
| `/osass-time` | Display the current server date and time | `/osass-time` |
| `/osass-choose` | Choose between provided options | `/osass-choose option1 option2` |
| `/osass-joke` | Get a developer joke | `/osass-joke` |

## License

This project is open source and available under the [MIT License](LICENSE).
