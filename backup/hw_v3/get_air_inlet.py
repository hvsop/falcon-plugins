#!/usr/bin/env python
import commands,time

endpoint = commands.getstatusoutput("curl -s http://127.0.0.1:1988/plugin/endpoint")[1]

output_list = []

def air_inlet():
    try:
        cmd_state, cmd_result = commands.getstatusoutput("ipmitool -I open sdr | grep 'Front Ambient'")
        if cmd_state == 0:
            air_inlet_list =  cmd_result.strip("\n").split("|")
        else:
            return []
        k = air_inlet_list[0]
        v = air_inlet_list[1].split()[0]
        air_inlet_dict = {}
        air_inlet_dict["metric"] = "gome_air_inlet_temperature"
        air_inlet_dict["value"] = v
        air_inlet_dict["endpoint"] = endpoint
        air_inlet_dict["timestamp"] = int(time.time())
        air_inlet_dict["counterType"] = "GAUGE"
        air_inlet_dict["step"] = 60
        air_inlet_dict["tags"] = "description=air-inlet-temperature,type=alarm"
        output_list.append(air_inlet_dict)
        return output_list
    except:
        return []


def hw_v3_air_inlet():
    try:
        cmd_state, cmd_result = commands.getstatusoutput("ipmitool sdr list | grep Inlet")
        if cmd_state == 0:
            air_inlet_list =  cmd_result.strip("\n").split("|")
        else:
            return []
        k = air_inlet_list[0].split()[0]
        v = air_inlet_list[1].split()[0]
        air_inlet_dict = {}
        air_inlet_dict["metric"] = "gome_air_inlet_temperature"
        air_inlet_dict["value"] = v
        air_inlet_dict["endpoint"] = endpoint
        air_inlet_dict["timestamp"] = int(time.time())
        air_inlet_dict["counterType"] = "GAUGE"
        air_inlet_dict["step"] = 60
        air_inlet_dict["tags"] = "description=air-inlet-temperature,type=alarm"
        output_list.append(air_inlet_dict)
        return output_list
    except:
        return []
