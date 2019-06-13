#!/usr/bin/env python
import commands,time

endpoint = commands.getstatusoutput("curl -s http://127.0.0.1:1988/plugin/endpoint")[1]

output_list = []

def lom_card():
    try:
        cmd_state, cmd_result = commands.getstatusoutput("ipmitool -I open sdr | grep 'LOM Card'")
        if cmd_state == 0:
            lom_card_list =  cmd_result.strip("\n").split("|")
        else:
            return []
        k = lom_card_list[0]
        v = lom_card_list[1].split()[0]
        lom_card_dict = {}
        lom_card_dict["metric"] = "gome_lom_card_temperature"
        lom_card_dict["value"] = v
        lom_card_dict["endpoint"] = endpoint
        lom_card_dict["timestamp"] = int(time.time())
        lom_card_dict["counterType"] = "GAUGE"
        lom_card_dict["step"] = 600
        lom_card_dict["tags"] = "description=air-outlet-temperature,type=alarm"
        output_list.append(lom_card_dict)
        return output_list
    except:
        return []
def dl580g8_lom_card():
    try:
        cmd_state, cmd_result = commands.getstatusoutput("ipmitool -I open sdr | grep 'Board'")
        if cmd_state == 0:
            lom_card_list =  cmd_result.strip("\n").split("|")
        else:
            return []
        k = lom_card_list[0]
        v = lom_card_list[1].split()[0]
        lom_card_dict = {}
        lom_card_dict["metric"] = "gome_lom_card_temperature"
        lom_card_dict["value"] = v
        lom_card_dict["endpoint"] = endpoint
        lom_card_dict["timestamp"] = int(time.time())
        lom_card_dict["counterType"] = "GAUGE"
        lom_card_dict["step"] = 600
        lom_card_dict["tags"] = "description=air-outlet-temperature,type=alarm"
        output_list.append(lom_card_dict)
        return output_list
    except:
        return []


def hw_v3_lom_card():
    try:
        cmd_state, cmd_result = commands.getstatusoutput("ipmitool sdr list | grep Outlet")
        if cmd_state == 0:
            lom_card_list =  cmd_result.strip("\n").split("|")
        else:
            return []
        k = lom_card_list[0].split()[0]
        v = lom_card_list[1].split()[0]
        lom_card_dict = {}
        lom_card_dict["metric"] = "gome_lom_card_temperature"
        lom_card_dict["value"] = v
        lom_card_dict["endpoint"] = endpoint
        lom_card_dict["timestamp"] = int(time.time())
        lom_card_dict["counterType"] = "GAUGE"
        lom_card_dict["step"] = 600
        lom_card_dict["tags"] = "description=air-outlet-temperature,type=alarm"
        output_list.append(lom_card_dict)
        return output_list
    except:
        return []
def sugon_v3_lom_card():
    try:
        cmd_state, cmd_result = commands.getstatusoutput("grep Outlet| tail -1")
        if cmd_state == 0:
            lom_card_list =  cmd_result.strip("\n").split("|")
        else:
            return []
        k = lom_card_list[0].split()[0]
        v = lom_card_list[1].split()[0]
        lom_card_dict = {}
        lom_card_dict["metric"] = "gome_lom_card_temperature"
        lom_card_dict["value"] = v
        lom_card_dict["endpoint"] = endpoint
        lom_card_dict["timestamp"] = int(time.time())
        lom_card_dict["counterType"] = "GAUGE"
        lom_card_dict["step"] = 600
        lom_card_dict["tags"] = "description=air-outlet-temperature,type=alarm"
        output_list.append(lom_card_dict)
        return output_list
    except:
        return []
