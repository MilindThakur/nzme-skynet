#!/bin/sh
./docker_compose.sh start
cd test/testserver
python -m SimpleHTTPServer &>/dev/null &
cd ../../
# Wait for the emulators to start
#echo "Sleeping for 1m for emulators to start..."
#sleep 1m
py.test -v test
pkill -f SimpleHTTPServer
./docker_compose.sh stop
