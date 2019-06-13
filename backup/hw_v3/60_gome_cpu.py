#!/usr/bin/env python
import json
import commands
import get_cpu_status as status
import get_cpu_temp as temp

product = commands.getstatusoutput("dmidecode -t system | grep 'Product Name'")[1].split(":")[1].strip()

cpu_list = []

if product == "ProLiant DL380 Gen9":
    cpu_list.extend(status.cpu_status())
    cpu_list.extend(temp.cpu_temp())

elif product == "RH2288 V3":
    cpu_list.extend(status.hw_v3_cpu_status())
    cpu_list.extend(temp.hw_v3_cpu_temp())

print json.dumps(cpu_list)
