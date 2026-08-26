# OS-Assistent-SLack-BOT

A Slack bot built with Node.js and Slack Bolt that provides helpful utility commands.

## Installation

Install the dependencies:

```bash
npm install
```

## Configuration

Set `SLACK_BOT_TOKEN` and `SLACK_APP_TOKEN` in a `.env` file, then start the bot:

```bash
node index.js
```

## Available Commands

- `/osass-ping` - Check bot latency
- `/osass-hello` - Get a personalized greeting
- `/osass-help` - Show this help message
- `/osass-time` - Show the current server time
- `/osass-choose option1 option2` - Choose between options
- `/osass-joke` - Get a short joke