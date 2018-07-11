#!/bin/bash

PID_FILE=/tmp/badwordbot.pid
[ -f $PID_FILE ] && kill -9 $(cat $PID_FILE) && rm $PID_FILE
echo "Starting BadWordBot"
pipenv run python3.6 ./bot.py > /var/log/badwordbot.log 2>&1 & echo $! >>$PID_FILE
