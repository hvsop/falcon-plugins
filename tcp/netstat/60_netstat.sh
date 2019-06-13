#!/bin/bash

#nowtime=`date +%s`
#endpoint="10.140.60.168"
#source ./env.sh
cd `dirname $0`
endpoint=`cat /app/falcon/agent/config/cfg.json  | grep hostname | awk '{print $2}' | tr '"' ' ' | tr ',' ' ' | awk '{print $1}'`
nowtime=`date +%s`
tcpactive=`netstat -s | grep active | head -n 1 | awk '{print $1}'`
tcppassive=`netstat -s | grep passive | head -n 1 | awk '{print $1}'`

echo "[{\"metric\": \"netstat.tcp.active\", \"endpoint\": \"$endpoint\", \"timestamp\": $nowtime, \"step\": 60, \"value\": $tcpactive, \"counterType\": \"COUNTER\"},{\"metric\": \"netstat.tcp.passive\", \"endpoint\": \"$endpoint\", \"timestamp\": $nowtime, \"step\": 60, \"value\": $tcppassive, \"counterType\": \"COUNTER\"}]"
