#!/bin/sh
host_name=`hostname`
ts=`date +%s`
Raid_Controller=`hpssacli ctrl all show status | grep Controller | awk '{print $1,$3}'`
echo $Raid_Controller | while read controller status
do
    if [ "$status" == "OK" ];then
        status=0
    else
        status=1
    fi
    echo  "[{\"metric\": \"gome_raid_$controller\", \"endpoint\": \"${host_name}\",\"tags\":\"type=alarm\", \"timestamp\": $ts,\"step\": 60,\"value\": $status,\"counterType\": \"GAUGE\"}]"
done 
