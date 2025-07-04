# dadabot
The one and only Dadabot

## Create a discord bot
Follow [this tutorial](https://realpython.com/how-to-make-a-discord-bot-python/#how-to-make-a-discord-bot-in-the-developer-portal) to create a discord bot and copy its token in a file named `token.txt` placed at the root of the project.

## Deployment using Docker:
This is the easiest way to start the bot. Dependencies are installed automatically. Make sure that you have [docker](https://www.docker.com/) installed on your system. Then, run the following commands from the root of the project:
```
docker build . -t dadabot:latest
docker run dadabot:latest
```

## Manual deployment
When debugging, it can be useful to run the project directly on your machine. Here is how to do it:

1. Make sure you have linux installed

2. Run this command to install the required linux packages
```
sudo apt update && sudo apt install -y python3-pip ghostscript poppler-utils ffmpeg
```

3. Run this command to install the required python packages
```
pip install -r requirements.txt
```

4. Launch the bot by running this command
```
python3 bot.py
```