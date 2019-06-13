#!/usr/bin/env python
import json,commands
import get_raid_battery as battery
import get_raid_controller as status
product = commands.getstatusoutput("dmidecode -t system | grep 'Product Name'")[1].split(":")[1].strip()

raid_list  = []

if product == "ProLiant DL380 Gen9":
    raid_list.extend(status.raid_controller())
    raid_list.extend(battery.raid_battery())

elif product == "RH2288 V3":
    raid_list.extend(status.hw_v3_raid_controller())
    raid_list.extend(battery.hw_v3_raid_battery())

print json.dumps(raid_list)
