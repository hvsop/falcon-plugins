#!/usr/bin/env python
import commands,time

endpoint = commands.getstatusoutput("curl -s http://127.0.0.1:1988/plugin/endpoint")[1] 

output_list = []

def power_status():
    try:
        cmd_state, cmd_result = commands.getstatusoutput("ipmitool  -I open sdr  | grep 'Power Supply'")
        if cmd_state == 0:
            power_list =  cmd_result.strip("\n").split("\n")
        else:
            return []

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
            power_dict["endpoint"] = endpoint
            power_dict["timestamp"] = int(time.time())
            power_dict["counterType"] = "GAUGE"
            power_dict["step"] = 60
            power_dict["tags"] = "Power=%s,type=alarm"%k
            output_list.append(power_dict)
        return output_list
    except:
        return []


def hw_v3_power_status():
    try:
        cmd_state, cmd_result = commands.getstatusoutput('ipmitool  -I open sdr  | grep -Ei "Power[0-9]+"')
        if cmd_state == 0:
            power_list =  cmd_result.strip("\n").split("\n")
        else:
            return []

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
            power_dict["endpoint"] = endpoint
            power_dict["timestamp"] = int(time.time())
            power_dict["counterType"] = "GAUGE"
            power_dict["step"] = 60
            power_dict["tags"] = "Power=%s,type=alarm"%k
            output_list.append(power_dict)
        return output_list
    except:
        return []
