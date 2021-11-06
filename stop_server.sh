echo 'Removing old docker container...'
docker rm $(docker stop $(docker ps -a -q --filter ancestor=api_coalescing --format="{{.ID}}"))
echo 'Done.'