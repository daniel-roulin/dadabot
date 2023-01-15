FROM python:3.7

WORKDIR /app

ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && apt install -y python3-pip ghostscript poppler-utils ffmpeg

COPY requirements.txt ./
ENV SODIUM_INSTALL=systemt
RUN pip install -r requirements.txt

COPY . .

CMD [ "python3", "bot.py" ]