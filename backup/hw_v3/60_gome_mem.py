#!/usr/bin/env python
import json,commands
import get_mem as dimm

product = commands.getstatusoutput("dmidecode -t system | grep 'Product Name'")[1].split(":")[1].strip()

mem_status = []

if product == "ProLiant DL380 Gen9":
    mem_status.extend(dimm.dimm_status())

elif product == "RH2288 V3":
    mem_status.extend(dimm.hw_v3_dimm_status())

print json.dumps(mem_status)
