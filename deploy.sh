printf "Building image...\n"
docker build . -t dadabot:latest

printf "\nSwitching context...\n"
docker context use dadaserver

printf "\nStopping and removing old container...\n"
docker rm $(docker stop $(docker ps -a -q --filter ancestor=dadarou/dadabot:latest --format="{{.ID}}"))

printf "\nPulling latest image...\n"
docker pull dadarou/dadabot:latest

printf "\nRunning container...\n"
docker run -d --restart always dadarou/dadabot:latest

printf "\nRunning containers:\n"
docker ps -a

printf "\nResetting context...\n"
docker context use default

printf "\nDone!\n"