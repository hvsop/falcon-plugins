#!/usr/bin/env python
import commands,time

endpoint = commands.getstatusoutput("curl -s http://127.0.0.1:1988/plugin/endpoint")[1]

def raid_controller():
    try:
        cmd_state,cmd_result = commands.getstatusoutput("ssacli ctrl all show status | grep Controller")
        if cmd_state == 0:
            contr_list = cmd_result.split()
            if contr_list[2].strip()  == "OK" :
                state = 0
            else:
                state = 1
            controller_list = []
            controller_dict = {}
            controller_dict["metric"] = "gome_raid_Controller"
            controller_dict["value"] = state
            controller_dict["endpoint"] = endpoint
            controller_dict["timestamp"] = int(time.time())
            controller_dict["counterType"] = "GAUGE"
            controller_dict["step"] = 600
            controller_dict["tags"] = "description=Controller,type=alarm"
            controller_list.append(controller_dict)
            return controller_list
        else:
            return []
    except:
        return []

def hw_v3_raid_controller():
    try:
        cmd_state,cmd_result = commands.getstatusoutput("ipmitool sdr list | grep 'RAID Status'")
        if cmd_state == 0:
            contr_list = cmd_result.split("|")
            if contr_list[2].strip()  == "ok" :
                state = 0
            else:
                state = 1
            controller_list = []
            controller_dict = {}
            controller_dict["metric"] = "gome_raid_status"
            controller_dict["value"] = state
            controller_dict["endpoint"] = endpoint
            controller_dict["timestamp"] = int(time.time())
            controller_dict["counterType"] = "GAUGE"
            controller_dict["step"] = 600
            controller_dict["tags"] = "description=raid_status,type=alarm"
            controller_list.append(controller_dict)
            return controller_list
        else:
            return []
    except:
        return []

def inspur_raid_controller():
    try:
        cmd_state,cmd_result = commands.getstatusoutput("ipmitool sdr list | grep 'RAID'")
        if cmd_state == 0:
            contr_list = cmd_result.split("|")
            if contr_list[2].strip()  == "ok" :
                state = 0
            else:
                state = 1
            controller_list = []
            controller_dict = {}
            controller_dict["metric"] = "gome_raid_status"
            controller_dict["value"] = state
            controller_dict["endpoint"] = endpoint
            controller_dict["timestamp"] = int(time.time())
            controller_dict["counterType"] = "GAUGE"
            controller_dict["step"] = 600
            controller_dict["tags"] = "description=raid_status,type=alarm"
            controller_list.append(controller_dict)
            return controller_list
        else:
            return []
    except:
        return []
