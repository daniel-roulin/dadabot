FROM python:latest

WORKDIR /app

ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && apt install -y python3-pip ghostscript poppler-utils ffmpeg

COPY requirements.txt ./
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "bot.py" ]