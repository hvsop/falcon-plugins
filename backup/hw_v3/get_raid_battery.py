#!/usr/bin/env python
import commands,time

endpoint = commands.getstatusoutput("curl -s http://127.0.0.1:1988/plugin/endpoint")[1]   

def raid_battery():
    try:
        cmd_state, cmd_result = commands.getstatusoutput("ssacli ctrl all show status | grep Battery")
        if cmd_state == 0:
            battery = cmd_result.split(":")[0].split("/")[0].strip()
            if  cmd_result.split(":")[1].strip() == "OK":
                status = 0
            else:
                status = 1
            battery_list = []
            battery_dict = {}
            battery_dict["metric"] = "gome_raid_Battery"
            battery_dict["value"] = status
            battery_dict["endpoint"] = endpoint
            battery_dict["timestamp"] = int(time.time())
            battery_dict["counterType"] = "GAUGE"
            battery_dict["step"] = 60
            battery_dict["tags"] = "description=Battery,type=alarm"
            battery_list.append(battery_dict)
            return battery_list
        else:
            return []
    except:
        return []


def hw_v3_raid_battery():
    try:
        cmd_state, cmd_result = commands.getstatusoutput("/opt/MegaRAID/MegaCli/MegaCli64  -AdpBbuCmd -aAll | grep 'Battery State'")
        if cmd_state == 0:
            if  cmd_result.split(":")[1].strip() == "Optimal":
                status = 0
            else:
                status = 1
            battery_list = []
            battery_dict = {}
            battery_dict["metric"] = "gome_raid_Battery"
            battery_dict["value"] = status
            battery_dict["endpoint"] = endpoint
            battery_dict["timestamp"] = int(time.time())
            battery_dict["counterType"] = "GAUGE"
            battery_dict["step"] = 60
            battery_dict["tags"] = "description=Battery,type=alarm"
            battery_list.append(battery_dict)
            return battery_list
        else:
            return []
    except:
        return []
