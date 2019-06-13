#!/bin/sh
host_name=$(hostname)
ts=$(date +%s)
cpu_status=$(ipmitool -I open sdr | grep CPU | awk '{print $1="CPU""_"$2,$8}')

#get cpu_status info
var_cpu_status=$(  
echo "$cpu_status" | while read cpu status
do
    if [ "$status" == "ok" ];then
        status=0
    else
        status=1
    fi
    echo  -e "[{\"metric\": \"gome_cpu_status\", \"endpoint\": \"${host_name}\",\"tags\":\"cpu=$cpu,type=alarm\", \"timestamp\": $ts,\"step\": 60,\"value\": $status,\"counterType\": \"GAUGE\"}]""\c"
done
)   

#format output
echo $var_cpu_status | sed  's/\]\[/,/g'   
