echo 'Removing old docker container...'
docker rm $(docker stop $(docker ps -a -q --filter ancestor=api_coalescing --format="{{.ID}}"))
echo 'Done.'
echo 'Building docker image...'
python src/tests.py
if [ $? -eq 0 ]
then
  echo 'Done.'
else
  echo "...Tests Failed" && exit;
fi
echo 'Building docker image...'
docker build -t api_coalescing .
echo 'Done.'
docker scan
echo 'Running docker image...'
docker run -i -p 5001:5001 -d api_coalescing
echo 'Done.'