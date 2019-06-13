#!/bin/sh
host_name=$(hostname)
ts=$(date +%s)
fans_status=$(hpasmcli -s "show fans" | grep -E '^#' | awk '{print $1,$3}')

#get fans_status info
var_fans_status=$(
echo -e "$fans_status" | while read fan status
do
    if [ "$status" == "Yes" ];then
        status=0
    else
        status=1
    fi
    echo -e  "[{\"metric\": \"gome_fans_status\", \"endpoint\": \"${host_name}\",\"tags\":\"fan_name=$fan,type=alarm\", \"timestamp\": $ts,\"step\": 60,\"value\": $status,\"counterType\": \"GAUGE\"}]""\c"
done
)

#format output
echo $var_fans_status | sed 's/\]\[/,/g'
