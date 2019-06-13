#!/bin/sh
host_name=`hostname`
ts=`date +%s`
phy_drive=(`hpssacli ctrl all show config | grep physicaldrive | awk '{print $1"_"$2}'`)
phy_number=`hpssacli ctrl all show config | grep physicaldrive | awk '{print $1"_"$2}' | wc -l`
disk_status=(`hpssacli ctrl all show config | grep physicaldrive | awk '{print $10}'| tr -d ")"`)

phy_res=$(
for ((i=0;i<$phy_number;i++))
do
   echo ${phy_drive[$i]} ${disk_status[$i]}
done
)

#get disk_status info
var_disk_status=$(
echo "$phy_res" | while read p_name p_status
do
    if [ "$p_status" == "OK" ];then
        p_status=0
    else
        p_status=1
    fi
    echo -e  "[{\"metric\": \"gome_disk_status\", \"endpoint\": \"${host_name}\",\"tags\":\"phy_driver=$p_name,type=alarm\", \"timestamp\": $ts,\"step\": 60,\"value\": $p_status,\"counterType\": \"GAUGE\"}]""\c"
done
)

#format output
echo $var_disk_status | sed 's/\]\[/,/g'
