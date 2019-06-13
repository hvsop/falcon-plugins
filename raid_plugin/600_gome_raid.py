#!/usr/bin/env python
import json,commands
import get_raid_battery as battery
import get_raid_controller as status
product = commands.getstatusoutput("dmidecode -t system | grep 'Product Name'")[1].split(":")[1].strip()
p_list = ["ProLiant DL380 Gen9","ProLiant DL580 G7","ProLiant DL580 Gen8","RH2288 V3","RH2288H V3","I620-G20","PowerEdge R730","NF5280M4","SA5212M4"]
def main():
    if product in p_list:
        if product == "ProLiant DL380 Gen9" or product == "ProLiant DL580 G7" or product == "ProLiant DL580 Gen8":
            raid_list  = []
            raid_list.extend(status.raid_controller())
            raid_list.extend(battery.raid_battery())
	elif product == "RH2288H V3" or product == "RH2288 V3" or product == "I620-G20" or product == "PowerEdge R730" :
            raid_list  = []
            raid_list.extend(status.hw_v3_raid_controller())
            raid_list.extend(battery.hw_v3_raid_battery())
        elif product == "NF5280M4" or product == "SA5212M4":
            raid_list  = []
            raid_list.extend(status.inspur_raid_controller())
            raid_list.extend(battery.hw_v3_raid_battery())
        print json.dumps(raid_list)
    else:
        return None
if __name__ == '__main__':
    main()
