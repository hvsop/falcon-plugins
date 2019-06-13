#!/usr/bin/env python
import commands,time

endpoint = commands.getstatusoutput("curl -s http://127.0.0.1:1988/plugin/endpoint")[1]

output_list = []

def fans_status():
    try:
        cmd_state, cmd_result = commands.getstatusoutput("hpasmcli -s 'show fans' | grep -E '^#'")
        if cmd_state == 0:
            fans_list =  cmd_result.strip("\n").split("\n")
        else:
            return []
        for item in fans_list:
            k = item.split()[0].strip()
            v =  item.split()[2].strip()
            if v == "Yes":
                v = 0
            else:
                v = 1
            fans_dict = {}
            fans_dict["metric"] = "gome_fans_status"
            fans_dict["value"] = v
            fans_dict["endpoint"] = endpoint
            fans_dict["timestamp"] = int(time.time())
            fans_dict["counterType"] = "GAUGE"
            fans_dict["step"] = 60
            fans_dict["tags"] = "fans=%s,type=alarm"%k
            output_list.append(fans_dict)
        return output_list
    except:
        return []


def hw_v3_fans_status():
    try:
        cmd_state, cmd_result = commands.getstatusoutput("ipmitool sdr list | grep -E 'FAN[0-9]+ F Status'")
        if cmd_state == 0:
            fans_list =  cmd_result.strip("\n").split("\n")
        else:
            return []
        for item in fans_list:
            k = item.split()[0].strip()
            v =  item.split("|")[2].strip()
            if v == "ok":
                v = 0
            else:
                v = 1
            fans_dict = {}
            fans_dict["metric"] = "gome_fans_status"
            fans_dict["value"] = v
            fans_dict["endpoint"] = endpoint
            fans_dict["timestamp"] = int(time.time())
            fans_dict["counterType"] = "GAUGE"
            fans_dict["step"] = 60
            fans_dict["tags"] = "fans=%s,type=alarm"%k
            output_list.append(fans_dict)
        return output_list
    except:
        return []
