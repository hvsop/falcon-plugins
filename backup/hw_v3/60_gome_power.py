#!/usr/bin/env python
import json
import commands
import get_power_status as status
import get_power_watts as watts

product = commands.getstatusoutput("dmidecode -t system | grep 'Product Name'")[1].split(":")[1].strip()

power_list = []

if product == "ProLiant DL380 Gen9":
    power_list.extend(status.power_status())
    power_list.extend(watts.power_watts())

elif product == "RH2288 V3":
    power_list.extend(status.hw_v3_power_status())
    power_list.extend(watts.hw_v3_power_watts())

print json.dumps(power_list)
