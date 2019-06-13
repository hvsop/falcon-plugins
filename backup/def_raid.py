#!/usr/bin/env python
import os
import json
import socket
import time

hostname = socket.gethostname()

temp_list = []

def raid_controller_status():
    controller_cmd_result = os.popen("hpssacli ctrl all show status | grep Controller | awk '{print $1,$3}'").read()
    if controller_cmd_result.split()[1] == "OK":
        status = 0
    else:
        status = 1
    controller_dict = {}
    controller_dict["metric"] = "gome_raid_Controller"
    controller_dict["value"] = status
    controller_dict["endpoint"] = hostname
    controller_dict["timestamp"] = int(time.time())
    controller_dict["counterType"] = "GAUGE"
    controller_dict["step"] = 60
    controller_dict["tags"] = "type=alarm"
    temp_list.append(controller_dict)

def raid_battery_status():
    battery_cmd_result = os.popen("hpssacli ctrl all show status | grep Battery").read()
    battery =  battery_cmd_result.split(":")[0].split("/")[0].strip()
    if  battery_cmd_result.split(":")[1].strip() == "OK":
        status = 0
    else:
        status = 1
    battery_dict = {}
    battery_dict["metric"] = "gome_raid_Battery"
    battery_dict["value"] = status
    battery_dict["endpoint"] = hostname
    battery_dict["timestamp"] = int(time.time())
    battery_dict["counterType"] = "GAUGE"
    battery_dict["step"] = 60
    battery_dict["tags"] = "type=alarm"
    temp_list.append(battery_dict)
    print json.dumps(temp_list)
if __name__ == '__main__':
    raid_controller_status()
    raid_battery_status()
