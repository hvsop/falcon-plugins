#!/bin/sh
host_name=`hostname`
ts=`date +%s`
dimm_num=`hpasmcli -s "show dimm" | grep Processor | wc -l`
Processor=(`hpasmcli -s "show dimm" | grep Processor | awk  '{print $1"_"$3}'`)
Module=(`hpasmcli -s "show dimm" | grep Module | awk '{print $1="socket""_"$3}'`)
Status=(`hpasmcli -s "show dimm" | grep Status | awk '{print $2}'`)

dimm_status=$(
for ((i=0;i<$dimm_num;i++))
do
    echo ${Processor[$i]}_${Module[$i]}  ${Status[$i]}
done
)

#get dimm_status info
var_dimm_status=$(
echo "$dimm_status" | while read dimm_name status
do
    if [ "$status" == "Ok" ];then
        status=0
    else
        status=1
    fi
    echo -e "[{\"metric\": \"gome_mem_status\", \"endpoint\": \"${host_name}\",\"tags\":\"mem_socket=$dimm_name,type=alarm\",\"timestamp\": $ts,\"step\": 60,\"value\": $status,\"counterType\": \"GAUGE\"}]""\c"
done
)
#format output
echo $var_dimm_status | sed 's/\]\[/,/g'
