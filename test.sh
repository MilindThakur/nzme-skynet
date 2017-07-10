#!/bin/sh
./docker_compose.sh start
cd test/testserver
python -m SimpleHTTPServer &>/dev/null &
cd ../../
sleep 2
pytest test
pkill -f SimpleHTTPServer
./docker_compose.sh stop
