#!/usr/bin/env python
import json,commands
import get_mem as dimm
product = commands.getstatusoutput("dmidecode -t system | grep 'Product Name'")[1].split(":")[1].strip()
p_list = ["ProLiant DL380 Gen9","ProLiant DL580 G7","ProLiant DL580 Gen8","RH2288 V3","RH2288H V3","I620-G20","NF5280M4","SA5212M4","ProLiant DL380 G7","ProLiant DL380 G5","ProLiant DL380e Gen8","ProLiant DL388p Gen8","ProLiant DL388 Gen9","ProLiant DL580 G5","ProLiant DL580 Gen9","ProLiant DL80 Gen9","I620-C20","NF5270M3"]
def main():
    if product in p_list:
        if product == "ProLiant DL380 Gen9" or product == "ProLiant DL380 G7" or product == "ProLiant DL380e Gen8" or product == "ProLiant DL388p Gen8" or product == "ProLiant DL388 Gen9" or product == "ProLiant DL80 Gen9":
            mem_status = []
            mem_status.extend(dimm.dimm_status())
        elif product == "ProLiant DL580 G7" or product == "ProLiant DL580 Gen8" or product == "ProLiant DL380 G5" or product == "ProLiant DL580 G5" or product == "ProLiant DL580 Gen9":
            mem_status = []
            mem_status.extend(dimm.dl580g7_dimm_status())
        
	elif product == "RH2288H V3" or product == "RH2288 V3" or product == "NF5280M4" or product == "SA5212M4" or product == "NF5270M3":
            mem_status = []
            mem_status.extend(dimm.hw_v3_dimm_status())
        elif product == "I620-G20" or product == "I620-C20":
            mem_status = []
            mem_status.extend(dimm.sugon_v3_dimm_status())
        print json.dumps(mem_status)
    else:
        return None
if __name__ == '__main__':
    main()
