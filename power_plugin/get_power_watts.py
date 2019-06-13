#!/usr/bin/env python
import commands,time

endpoint = commands.getstatusoutput("curl -s http://127.0.0.1:1988/plugin/endpoint")[1]

output_list = []
_output_list = []
watts_values = []

def power_watts_sum():
        power_watts_dict = {}
#        print sum(watts_values)
        power_watts_dict["metric"] = "gome_powerwatts"
        power_watts_dict["value"] = sum(watts_values)
        power_watts_dict["endpoint"] = endpoint
        power_watts_dict["timestamp"] = int(time.time())
        power_watts_dict["counterType"] = "GAUGE"
        power_watts_dict["step"] = 600
        power_watts_dict["tags"] = ""
        _output_list.append(power_watts_dict)
        return _output_list

def power_watts():
    try:
        cmd_state, cmd_result = commands.getstatusoutput("ipmitool  -I open sdr  | grep 'Power Supply'")
        if cmd_state == 0:
            power_watts_list =  cmd_result.strip("\n").split("\n")
        else:
            return []

        for item in power_watts_list:
            k = item.split("|")[0].strip()
            v =  item.split("|")[1].strip().split()[0]
            power_watts_dict = {}
            power_watts_dict["metric"] = "gome_power_watts"
            power_watts_dict["value"] = v
            power_watts_dict["endpoint"] = endpoint
            power_watts_dict["timestamp"] = int(time.time())
            power_watts_dict["counterType"] = "GAUGE"
            power_watts_dict["step"] = 600
            power_watts_dict["tags"] = "Power=%s,type=alarm"%k
            output_list.append(power_watts_dict)
            watts_values.append(int(v))
        return output_list
    except:
        return []

def hw_v3_power_watts():
    try:
        cmd_state, cmd_result = commands.getstatusoutput('ipmitool  -I open sdr  | grep -Ei "Power[0-9]+"')
        if cmd_state == 0:
            power_watts_list =  cmd_result.strip("\n").split("\n")
        else:
            return []

        for item in power_watts_list:
            k = item.split("|")[0].strip()
            v =  item.split("|")[1].strip().split()[0]
            power_watts_dict = {}
            power_watts_dict["metric"] = "gome_power_watts"
            power_watts_dict["value"] = v
            power_watts_dict["endpoint"] = endpoint
            power_watts_dict["timestamp"] = int(time.time())
            power_watts_dict["counterType"] = "GAUGE"
            power_watts_dict["step"] = 600
            power_watts_dict["tags"] = "Power=%s,type=alarm"%k
            output_list.append(power_watts_dict)
            watts_values.append(int(v))
        return output_list
    except:
        return []
def sugon_v3_power_watts():
    try:
        cmd_state, cmd_result = commands.getstatusoutput('ipmitool  -I open sdr  | grep -Ei "Total_Power"')
        if cmd_state == 0:
            power_watts_list =  cmd_result.strip("\n").split("\n")
        else:
            return []

        for item in power_watts_list:
            k = item.split("|")[0].strip()
            v =  item.split("|")[1].strip().split()[0]
            power_watts_dict = {}
            power_watts_dict["metric"] = "gome_power_watts"
            power_watts_dict["value"] = v
            power_watts_dict["endpoint"] = endpoint
            power_watts_dict["timestamp"] = int(time.time())
            power_watts_dict["counterType"] = "GAUGE"
            power_watts_dict["step"] = 600
            power_watts_dict["tags"] = "Power=%s,type=alarm"%k
            output_list.append(power_watts_dict)
            watts_values.append(int(v))
        return output_list
    except:
        return []

def h3c_power_watts():
    try:
        cmd_state, cmd_result = commands.getstatusoutput('ipmitool  -I open sdr  | grep -Ei "Total_Power"')
        if cmd_state == 0:
            power_watts_list =  cmd_result.strip("\n").split("\n")
        else:
            cmd_state, cmd_result = commands.getstatusoutput('ipmitool  -I open sdr | grep -Ei "PSU[0-9]_PIN"')
            if cmd_state == 0:
                power_watts_list =  cmd_result.strip("\n").split("\n")
            else:
                return []

        for item in power_watts_list:
            k = item.split("|")[0].strip()
            v =  item.split("|")[1].strip().split()[0]
            power_watts_dict = {}
            power_watts_dict["metric"] = "gome_power_watts"
            power_watts_dict["value"] = v
            power_watts_dict["endpoint"] = endpoint
            power_watts_dict["timestamp"] = int(time.time())
            power_watts_dict["counterType"] = "GAUGE"
            power_watts_dict["step"] = 600
            power_watts_dict["tags"] = "Power=%s,type=alarm"%k
            output_list.append(power_watts_dict)
            watts_values.append(int(v))
        return output_list
    except:
        return []

def dell_power_watts():
    try:
        cmd_state, cmd_result = commands.getstatusoutput('ipmitool sdr list full| grep -E "^System Level|^Pwr"')
        if cmd_state == 0:
            power_watts_list =  cmd_result.strip("\n").split("\n")
        else:
            return []

        for item in power_watts_list:
            k = item.split("|")[0].strip()
            v =  item.split("|")[1].strip().split()[0]
            power_watts_dict = {}
            power_watts_dict["metric"] = "gome_power_watts"
            power_watts_dict["value"] = v
            power_watts_dict["endpoint"] = endpoint
            power_watts_dict["timestamp"] = int(time.time())
            power_watts_dict["counterType"] = "GAUGE"
            power_watts_dict["step"] = 600
            power_watts_dict["tags"] = "Power=%s,type=alarm"%k
            output_list.append(power_watts_dict)
            watts_values.append(int(v))
        return output_list
    except:
        return []
