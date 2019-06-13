#!/bin/sh
host_name=$(hostname)
ts=$(date +%s)
cpu_temp=$(ipmitool -I open sdr | grep CPU | awk '{print $1="CPU""_"$2,$4}')

#get cpu_temp info
var_cpu_temp=$(
echo -e "$cpu_temp" | while read cpu temp
do
    echo -e "[{\"metric\": \"gome_cpu_temp\", \"endpoint\": \"${host_name}\",\"tags\":\"cpu=$cpu,type=alarm\", \"timestamp\": $ts,\"step\": 60,\"value\": $temp,\"counterType\": \"GAUGE\"}]""\c"
done
)

#format output
echo $var_cpu_temp | sed 's/\]\[/,/g'
