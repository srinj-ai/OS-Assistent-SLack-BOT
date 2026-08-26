require("dotenv").config();

const { App } = require("@slack/bolt");

const app = new App({
  token: process.env.SLACK_BOT_TOKEN,
  appToken: process.env.SLACK_APP_TOKEN,
  socketMode: true
});

app.command("/osass-ping", async ({ command, ack, respond }) => {
  const start = Date.now();
  await ack();
  const latency = Date.now() - start;
  await respond({ text: `Pong!\nLatency: ${latency}ms` });
});

app.command("/osass-hello", async ({ command, ack, respond }) => {
  await ack();
  const userName = command.user_name || command.user_id || "there";
  await respond({ text: `hello ${userName}` });
});

app.command("/osass-help", async ({ ack, respond }) => {
  await ack();
  await respond({
    text:
`Available commands:
/osass-ping - Check bot latency
/osass-hello - Get a personalized greeting
/osass-help - Show this help message
/osass-time - Show the current server time
/osass-choose - Choose between options
/osass-joke - Get a short joke`
  });
});

app.command("/osass-time", async ({ ack, respond }) => {
  await ack();
  const now = new Date().toLocaleString();
  await respond({ text: `Current server time: ${now}` });
});

app.command("/osass-choose", async ({ command, ack, respond }) => {
  await ack();
  const options = command.text.split(/\s+/);
  if (options.length < 2) {
    await respond({ text: "Usage: /osass-choose option1 option2" });
    return;
  }
  await respond({ text: `I choose: ${options[0]}` });
});

app.command("/osass-joke", async ({ ack, respond }) => {
  await ack();
  await respond({ text: "Why did the developer go broke? Because they used up all their cache." });
});

(async () => {
  await app.start();
  console.log("bot is running!");
})();