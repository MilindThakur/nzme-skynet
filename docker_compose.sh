#!/usr/bin/env bash
# set -e: exit asap if a command exits with a non-zero status
# set -x: print each command right before it is executed
set -xe

SCRIPT_ACTION=$1

COMPOSE_FILE="docker-compose.yaml"

# In OSX install gtimeout through `brew install coreutils`
function mtimeout() {
    if [ "$(uname -s)" = 'Darwin' ]; then
        gtimeout "$@"
    else
        timeout "$@"
    fi
}

echoerr() { printf "%s\n" "$*" >&2; }

# print error and exit
die () {
  echoerr "ERROR: $1"
  # if $2 is defined AND NOT EMPTY, use $2; otherwise, set to "160"
  errnum=${2-160}
  exit $errnum
}

WaitZaleniumStarted()
{
    DONE_MSG="Zalenium is now ready!"
    while ! docker logs zalenium | grep "${DONE_MSG}" >/dev/null; do
        echo -n '.'
        sleep 0.2
    done
}
export -f WaitZaleniumStarted

WaitAppiumStarted()
{
    DONE_MSG=":4723"
    while ! docker logs zalenium | grep "${DONE_MSG}" >/dev/null; do
        echo -n '.'
        sleep 1
    done
}
export -f WaitAppiumStarted

wait_for_emulator()
{
    local bootanim=""
    until [[ "$bootanim" =~ "1" ]]; do
       bootanim=`docker exec Nexus_5 adb -e shell getprop dev.bootcomplete 2>&1`
       echo "Waiting for emulator to start...$bootanim"
       sleep 1
    done
}

StartUp()
{
    # Avoid "An HTTP request took too long to complete." error
    export COMPOSE_HTTP_TIMEOUT=360

    # elgalu/selenium is mandatory requirement
    DOCKER_SELENIUM_IMAGE_COUNT=$(docker images | grep "elgalu/selenium" | wc -l)
    if [ ${DOCKER_SELENIUM_IMAGE_COUNT} -eq 0 ]; then
        echo "Seems that docker-selenium's image has not been downloaded yet, lets get it."
        docker pull elgalu/selenium
    fi

    # Ensure we have a clean environment
    docker-compose -f ${COMPOSE_FILE} -p zalenium down
#    rm -rf /tmp/videos
#    mkdir -p /tmp/videos

    # Start in daemon mode
    docker-compose -f ${COMPOSE_FILE} -p zalenium up --force-recreate -d

    # Attach to the logs but as a background process so we can see the logs on time
    docker-compose -f ${COMPOSE_FILE} -p zalenium logs --follow &

    # Wait for Zalenium
    if ! mtimeout --foreground "2m" bash -c WaitZaleniumStarted; then
        echo "Zalenium failed to start after 2 minutes, failing..."
        exit 8
    fi

#   Enable when testing on Android docker image in the docker-compose-yaml
#   Requires machine to have hardware acceleration
#    # Wait for Appium Emulator
#    if ! mtimeout --foreground "2m" bash -c WaitAppiumStarted; then
#        echo "Appium Node failed to join grid after 2 minutes, failing..."
#        exit 8
#    fi
#
#    echo "Wait for android emulator to be ready"
#    sleep 20s
#
#    wait_for_emulator

    echo "Zalenium started! Ready to run some tests!"
}

ShutDown()
{
    # Leave a clean environment
    docker-compose -f ${COMPOSE_FILE} -p zalenium down
}

case ${SCRIPT_ACTION} in
    start)
        StartUp
    ;;
    stop)
        ShutDown
    ;;
esac