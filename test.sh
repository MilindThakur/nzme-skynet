#!/bin/sh
./docker_compose.sh start
curl -sSL http://localhost:4444/wd/hub/status | jq .value.ready | grep true
py.test -v test
#pkill -f SimpleHTTPServer
./docker_compose.sh stop
