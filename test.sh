#!/bin/sh
cd test/testserver
python -m SimpleHTTPServer &>/dev/null &
cd ../../
./docker_compose.sh start
py.test -v test
pkill -f SimpleHTTPServer
./docker_compose.sh stop
