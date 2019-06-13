#!/usr/bin/env python
import os
import time
import socket
import json
hostname = socket.gethostname()

temp_list = []

def power_status():
    cmd_res = os.popen("ipmitool  -I open sdr  | grep 'Power Supply'").read()
    power_list =  cmd_res.strip("\n").split("\n")
    for item in power_list:
        k = item.split("|")[0].strip()
        v =  item.split("|")[2].strip()
        if v == "ok":
            v = 0
        else:
            v = 1
        power_dict = {}
        power_dict["metric"] = "gome_power_status"
        power_dict["value"] = v
        power_dict["endpoint"] = hostname
        power_dict["timestamp"] = int(time.time())
        power_dict["counterType"] = "GAUGE"
        power_dict["step"] = 60
        power_dict["tags"] = "Power=%s,type=alarm"%k
        temp_list.append(power_dict)
    #print json.dumps(temp_list)

def power_watts():
    cmd_res = os.popen("ipmitool  -I open sdr  | grep 'Power Supply'").read()
    power_watts_list =  cmd_res.strip("\n").split("\n")
    #temp_list = []
    for item in power_watts_list:
        k = item.split("|")[0].strip()
        v =  item.split("|")[1].strip().split()[0]
        power_watts_dict = {}
        power_watts_dict["metric"] = "gome_power_watts"
        power_watts_dict["value"] = v
        power_watts_dict["endpoint"] = hostname
        power_watts_dict["timestamp"] = int(time.time())
        power_watts_dict["counterType"] = "GAUGE"
        power_watts_dict["step"] = 60
        power_watts_dict["tags"] = "Power=%s,type=alarm"%k
        temp_list.append(power_watts_dict)
    print json.dumps(temp_list)
if __name__ == '__main__':
    power_status()
    power_watts()
