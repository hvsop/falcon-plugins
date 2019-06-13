#!/usr/bin/env python
import commands,time

endpoint = commands.getstatusoutput("curl -s http://127.0.0.1:1988/plugin/endpoint")[1]

output_list = []

def board_temp():
    try:
        cmd_state, cmd_result = commands.getstatusoutput("ipmitool -I open sdr | grep 'Chipset'")
        if cmd_state == 0:
            board_list =  cmd_result.strip("\n").split("|")
        else:
            return []
        k = board_list[0]
        v = board_list[1].split()[0]
        board_temp_dict = {}
        board_temp_dict["metric"] = "gome_board_temperature"
        board_temp_dict["value"] = v
        board_temp_dict["endpoint"] = endpoint
        board_temp_dict["timestamp"] = int(time.time())
        board_temp_dict["counterType"] = "GAUGE"
        board_temp_dict["step"] = 60
        board_temp_dict["tags"] = "description=main_board_temperature,type=alarm"
        output_list.append(board_temp_dict)
        return output_list
    except:
        return []


def hw_v3_board_temp():
    try:
        cmd_state, cmd_result = commands.getstatusoutput("ipmitool sdr list | grep 'PCH Temp'")
        if cmd_state == 0:
            board_list =  cmd_result.strip("\n").split("|")
        else:
            return []
        v = board_list[1].split()[0]
        board_temp_dict = {}
        board_temp_dict["metric"] = "gome_board_temperature"
        board_temp_dict["value"] = v
        board_temp_dict["endpoint"] = endpoint
        board_temp_dict["timestamp"] = int(time.time())
        board_temp_dict["counterType"] = "GAUGE"
        board_temp_dict["step"] = 60
        board_temp_dict["tags"] = "description=main_board_temperature,type=alarm"
        output_list.append(board_temp_dict)
        return output_list
    except:
        return []
