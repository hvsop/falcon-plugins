#!/bin/sh
host_name=`hostname`
name=$(ipmitool -I open sdr list | grep 'Power Supply'| awk '{print $1"_"$2"_"$3,$8}')
ts=`date +%s`

#get power_status info
var_power_status=$(
echo -e "$name" | while read power status 
do
    for i in "$status"
    do
        if [ "$i" == "ok" ];then 
            status=0
	else
	    status=1
        fi
        echo -e "[{\"metric\": \"gome_power_status\", \"endpoint\": \"${host_name}\",\"tags\":\"power=$power,type=alarm\", \"timestamp\": $ts,\"step\": 60,\"value\": $status,\"counterType\": \"GAUGE\"}]""\c"
    done
done
)

#format output
echo $var_power_status | sed 's/\]\[/,/g'
