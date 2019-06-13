#!/usr/bin/env python
import json,commands
import get_disk as status
import get_disk_err as error

product = commands.getstatusoutput("dmidecode -t system | grep 'Product Name'")[1].split(":")[1].strip()

disk_list  = []

if product == "ProLiant DL380 Gen9":
    disk_list.extend(status.disk_status())

elif product == "RH2288 V3":
    disk_list.extend(status.hw_v3_disk_status())
    disk_list.extend(error.media_error())
    disk_list.extend(error.other_error())
    disk_list.extend(error.Predictive_error())

print json.dumps(disk_list)
