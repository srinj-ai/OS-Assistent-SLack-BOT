"""Slack OS Assistant bot implemented with Python Slack Bolt."""

import os
import datetime
import time

from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler


load_dotenv()

app = App()


@app.command("/osass-ping")
def handle_ping(ack, respond):
    start = time.time()
    ack()
    latency = round((time.time() - start) * 1000)
    respond(text=f"Pong!\nLatency: {latency}ms")


@app.command("/osass-hello")
def handle_hello(ack, respond, command):
    ack()
    user_name = command.get("user_name") or command.get("user_id", "there")
    respond(text=f"hello {user_name}")


@app.command("/osass-help")
def handle_help(ack, respond):
    ack()
    respond(
        text=(
            "Available commands:\n"
            "/osass-ping - Check bot latency\n"
            "/osass-hello - Get a personalized greeting\n"
            "/osass-time - Show the current server time\n"
            "/osass-choose - Choose between options\n"
            "/osass-joke - Get a short joke"
        )
    )


@app.command("/osass-time")
def handle_time(ack, respond):
    ack()
    current_time = datetime.datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %Z")
    respond(text=f"Current server time: {current_time}")


@app.command("/osass-choose")
def handle_choose(ack, respond, command):
    ack()
    options = command.get("text", "").split()
    if len(options) < 2:
        respond(text="Usage: /osass-choose option1 option2")
        return
    respond(text=f"I choose: {options[0]}")


@app.command("/osass-python")
def handle_python(ack, respond):
    ack()
    respond(text="The OS Assistant bot is running normally.")



@app.command("/osass-joke")
def handle_joke(ack, respond):
    ack()
    respond(text="Why did the developer go broke? Because they used up all their cache.")


if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
