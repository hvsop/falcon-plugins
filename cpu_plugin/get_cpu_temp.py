#!/usr/bin/env python
import commands,time

endpoint = commands.getstatusoutput("curl -s http://127.0.0.1:1988/plugin/endpoint")[1]

output_list = []

def cpu_temp():
    try:
        cmd_state, cmd_result = commands.getstatusoutput("ipmitool -I open sdr | grep CPU")
        if cmd_state == 0:
            cpu_temp_list =  cmd_result.strip("\n").split("\n")
        else:
            return []

        for item in cpu_temp_list:
            k = item.split("|")[0].split("-")[1].strip()
            v =  item.split("|")[1].split()[0]
            cpu_temp_dict = {}
            cpu_temp_dict["metric"] = "gome_cpu_temperature"
            cpu_temp_dict["value"] = v
            cpu_temp_dict["endpoint"] = endpoint
            cpu_temp_dict["timestamp"] = int(time.time())
            cpu_temp_dict["counterType"] = "GAUGE"
            cpu_temp_dict["step"] = 600
            cpu_temp_dict["tags"] = "cpu=%s,type=alarm"%k
            output_list.append(cpu_temp_dict)
        return output_list
    except:
        return []


def hw_v3_cpu_temp():
    try:
        cmd_state, cmd_result = commands.getstatusoutput("ipmitool sdr list | grep -E 'CPU[0-9]+ Core'")
        if cmd_state == 0:
            cpu_temp_list =  cmd_result.strip("\n").split("\n")
        else:
            return []

        for item in cpu_temp_list:
            k = item.split("|")[0].split()[0]
            v =  item.split("|")[1].split()[0]
            cpu_temp_dict = {}
            cpu_temp_dict["metric"] = "gome_cpu_temperature"
            cpu_temp_dict["value"] = v
            cpu_temp_dict["endpoint"] = endpoint
            cpu_temp_dict["timestamp"] = int(time.time())
            cpu_temp_dict["counterType"] = "GAUGE"
            cpu_temp_dict["step"] = 600
            cpu_temp_dict["tags"] = "cpu=%s,type=alarm"%k
            output_list.append(cpu_temp_dict)
        return output_list
    except:
        return []

def sugon_v3_cpu_temp():
    try:
        cmd_state, cmd_result = commands.getstatusoutput("ipmitool sdr list | grep -E 'CPU[0-9]+_Temp'")
        if cmd_state == 0:
            cpu_temp_list =  cmd_result.strip("\n").split("\n")
        else:
            return []

        for item in cpu_temp_list:
            k = item.split("|")[0].split()[0]
            v =  item.split("|")[1].split()[0]
            cpu_temp_dict = {}
            cpu_temp_dict["metric"] = "gome_cpu_temperature"
            cpu_temp_dict["value"] = v
            cpu_temp_dict["endpoint"] = endpoint
            cpu_temp_dict["timestamp"] = int(time.time())
            cpu_temp_dict["counterType"] = "GAUGE"
            cpu_temp_dict["step"] = 600
            cpu_temp_dict["tags"] = "cpu=%s,type=alarm"%k
            output_list.append(cpu_temp_dict)
        return output_list
    except:
        return []


def h3c_cpu_temp():
    try:
        cmd_state, cmd_result = commands.getstatusoutput("ipmitool sdr list full|grep -E 'CPU [0-9]+'|grep -vE '\-[0-9]+'")
        if cmd_state == 0:
            cpu_temp_list =  cmd_result.strip("\n").split("\n")
        else:
            return []

        for item in cpu_temp_list:
            k = item.split("|")[0].split()[0]
            v =  item.split("|")[1].split()[0]
            cpu_temp_dict = {}
            cpu_temp_dict["metric"] = "gome_cpu_temperature"
            cpu_temp_dict["value"] = v
            cpu_temp_dict["endpoint"] = endpoint
            cpu_temp_dict["timestamp"] = int(time.time())
            cpu_temp_dict["counterType"] = "GAUGE"
            cpu_temp_dict["step"] = 600
            cpu_temp_dict["tags"] = "cpu=%s,type=alarm"%k
            output_list.append(cpu_temp_dict)
        return output_list
    except:
        return []

def dell_cpu_temp():
    try:
#        cmd_state, cmd_result = commands.getstatusoutput("ipmitool sdr list full| grep 'Inlet Temp'")
        cmd_state, cmd_result = commands.getstatusoutput("ipmitool sdr list full| grep -E 'Inlet Temp|Exhaust Temp'")
        if cmd_state == 0:
            cpu_temp_list =  cmd_result.strip("\n").split("\n")
        else:
            return []

        for item in cpu_temp_list:
            k = item.split("|")[0].split()[0]
            v =  item.split("|")[1].split()[0]
            cpu_temp_dict = {}
            cpu_temp_dict["metric"] = "gome_cpu_temperature"
            cpu_temp_dict["value"] = v
            cpu_temp_dict["endpoint"] = endpoint
            cpu_temp_dict["timestamp"] = int(time.time())
            cpu_temp_dict["counterType"] = "GAUGE"
            cpu_temp_dict["step"] = 600
            cpu_temp_dict["tags"] = "cpu=%s,type=alarm"%k
            output_list.append(cpu_temp_dict)
        return output_list
    except:
        return []
