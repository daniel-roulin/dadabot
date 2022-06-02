# dadabot
The one and only Dadabot

### Installation
`docker run --restart always dadarou/dadabot:latest`

### Steps to update
- `docker build . -t dadabot:latest`
- `ssh username@server`
- `docker pull dadarou/dadabot:latest`
- `docker run --restart always dadabot:latest`