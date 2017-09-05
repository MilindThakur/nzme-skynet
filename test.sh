#!/bin/sh
./docker_compose.sh start
cd test/testserver
python -m SimpleHTTPServer &>/dev/null &
cd ../../
# Wait for the emulators to start
sleep 20
py.test -v test
pkill -f SimpleHTTPServer
./docker_compose.sh stop
