#!/usr/bin/env python
import commands,time

endpoint = commands.getstatusoutput("curl -s http://127.0.0.1:1988/plugin/endpoint")[1]

output_list = []

def cpu_status():
    try:
        cmd_state, cmd_result = commands.getstatusoutput("ipmitool -I open sdr | grep CPU")
        if cmd_state == 0:
            cpu_status_list =  cmd_result.strip("\n").split("\n")
        else:
            return []
        for item in cpu_status_list:
            k = item.split("|")[0].split("-")[1].strip()
            v =  item.split("|")[2].strip()
            if v == "ok":
                v = 0
            else:
                v = 1
            cpu_status_dict = {}
            cpu_status_dict["metric"] = "gome_cpu_status"
            cpu_status_dict["value"] = v
            cpu_status_dict["endpoint"] = endpoint
            cpu_status_dict["timestamp"] = int(time.time())
            cpu_status_dict["counterType"] = "GAUGE"
            cpu_status_dict["step"] = 60
            cpu_status_dict["tags"] = "cpu=%s,type=alarm"%k
            output_list.append(cpu_status_dict)
        return output_list
    except:
        return []


def hw_v3_cpu_status():
    try:
        cmd_state, cmd_result = commands.getstatusoutput("ipmitool sdr list | grep -E 'CPU[0-9]+ Status'")
        if cmd_state == 0:
            cpu_status_list =  cmd_result.strip("\n").split("\n")
        else:
            return []
        for item in cpu_status_list:
            k = item.split("|")[0].split()[0].strip()
            v =  item.split("|")[2].strip()
            if v == "ok":
                v = 0
            else:
                v = 1
            cpu_status_dict = {}
            cpu_status_dict["metric"] = "gome_cpu_status"
            cpu_status_dict["value"] = v
            cpu_status_dict["endpoint"] = endpoint
            cpu_status_dict["timestamp"] = int(time.time())
            cpu_status_dict["counterType"] = "GAUGE"
            cpu_status_dict["step"] = 60
            cpu_status_dict["tags"] = "cpu=%s,type=alarm"%k
            output_list.append(cpu_status_dict)
        return output_list
    except:
        return []
