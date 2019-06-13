#!/usr/bin/env python
import os
import time
import socket
import json

hostname = socket.gethostname()

temp_list = []

def disk_status():
    phy_driver = os.popen("hpssacli ctrl all show config | grep physicaldrive").read()
    disk_list = phy_driver.strip("\n").split("\n")
    for item in disk_list:
        k1 = item.split()[0].strip()
        k2 = item.split()[1].strip()
        k = k1 + "_" +  k2
        v =  item.split()[9].strip(")")
        if v == "OK":
            v = 0
        else:
            v = 1
        disk_dict = {}
        disk_dict["metric"] = "gome_disk_status"
        disk_dict["value"] = v
        disk_dict["endpoint"] = hostname
        disk_dict["timestamp"] = int(time.time())
        disk_dict["counterType"] = "GAUGE"
        disk_dict["step"] = 60
        disk_dict["tags"] = "Disk=%s,type=alarm"%k
        temp_list.append(disk_dict)
    print json.dumps(temp_list)
if __name__ == '__main__':
    disk_status()
