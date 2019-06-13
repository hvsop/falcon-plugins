#!/usr/bin/env python
import os
import socket
import time
import json

hostname = socket.gethostname()

temp_list = [] 

def dimm_status():
    status = os.popen("hpasmcli -s 'show dimm' | grep Status | awk '{print $2}'").read().strip("\n")
    process = os.popen("hpasmcli -s 'show dimm' | grep Processor | awk '{print $1,$3}'").read().strip("\n")
    dimm_socket = os.popen("hpasmcli -s 'show dimm' | grep Module | awk '{print $1,$3}'").read().strip("\n")
    status_list = status.split("\n")
    process_list = process.split("\n")
    socket_list = dimm_socket.split("\n")
    list_number = len(process_list)
   
    l = []
    for i in range(list_number):
        temp = process_list[i] + "_" + socket_list[i]
        l.append(temp)
    
    for item in range(list_number):
        k = l[item]
        v = status_list[item]
        if v == "Ok":
            v = 0
        else:
            v = 1
        dimm_dict = {}
        dimm_dict["metric"] = "gome_mem_status"
        dimm_dict["value"] = v
        dimm_dict["endpoint"] = hostname
        dimm_dict["timestamp"] = int(time.time())
        dimm_dict["counterType"] = "GAUGE"
        dimm_dict["step"] = 60
        dimm_dict["tags"] = "dimm=%s,type=alarm"%k
        temp_list.append(dimm_dict)
    print json.dumps(temp_list)
if __name__ == '__main__':
    dimm_status()
