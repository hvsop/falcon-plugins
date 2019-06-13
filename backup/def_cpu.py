#!/usr/bin/env python
import os
import socket
import time
import json
hostname = socket.gethostname()
temp_list = []

def cpu_status():
    cmd_res = os.popen("ipmitool -I open sdr | grep CPU").read()
    cpu_status_list =  cmd_res.strip("\n").split("\n")
    for item in cpu_status_list:
        k = item.split("|")[0].strip()
        v =  item.split("|")[2].strip()
        if v == "ok":
            v = 0
        else:
            v = 1
        cpu_status_dict = {}
        cpu_status_dict["metric"] = "gome_cpu_status"
        cpu_status_dict["value"] = v
        cpu_status_dict["endpoint"] = hostname
        cpu_status_dict["timestamp"] = int(time.time())
        cpu_status_dict["counterType"] = "GAUGE"
        cpu_status_dict["step"] = 60
        cpu_status_dict["tags"] = "cpu=%s,type=alarm"%k
        temp_list.append(cpu_status_dict)
    #print json.dumps(temp_list)

def cpu_temp():
    cmd_res = os.popen("ipmitool -I open sdr | grep CPU").read()
    cpu_temp_list =  cmd_res.strip("\n").split("\n")
    for item in cpu_temp_list:
        k = item.split("|")[0].strip()
        v =  item.split("|")[1].split()[0]
        cpu_temp_dict = {}
        cpu_temp_dict["metric"] = "gome_cpu_temp"
        cpu_temp_dict["value"] = v
        cpu_temp_dict["endpoint"] = hostname
        cpu_temp_dict["timestamp"] = int(time.time())
        cpu_temp_dict["counterType"] = "GAUGE"
        cpu_temp_dict["step"] = 60
        cpu_temp_dict["tags"] = "cpu=%s,type=alarm"%k
        temp_list.append(cpu_temp_dict)
    print json.dumps(temp_list)
if __name__ == '__main__':
    cpu_status()
    cpu_temp()
