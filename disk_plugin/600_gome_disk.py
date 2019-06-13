#!/usr/bin/env python
import json,commands
import get_disk as status
import get_disk_err as error

product = commands.getstatusoutput("dmidecode -t system | grep 'Product Name'")[1].split(":")[1].strip()
p_list = ["ProLiant DL380 Gen9","ProLiant DL580 G7","ProLiant DL580 Gen8","RH2288 V3","RH2288H V3","PowerEdge R730","I620-G20","NF5280M4","SA5212M4","PowerEdge M610","PowerEdge R410","PowerEdge R620","PowerEdge R630","PowerEdge R710","PowerEdge R910","ProLiant DL360p Gen8","ProLiant DL380e Gen8","ProLiant DL380 G5","ProLiant DL380 G7","ProLiant DL388p Gen8","ProLiant DL388 Gen9","ProLiant DL580 G5","ProLiant DL580 Gen9","ProLiant DL80 Gen9","I620-C20","NF5270M3","R4900 G2","UniServer R4900 G3"]
def main():
    if product in p_list:
        if product == "ProLiant DL380 Gen9" or product == "ProLiant DL580 G7" or product == "ProLiant DL580 Gen8" or product == "ProLiant DL360p Gen8" or product == "ProLiant DL380e Gen8" or product == "ProLiant DL380 G5" or product == "ProLiant DL380 G7" or product == "ProLiant DL388p Gen8" or product == "ProLiant DL388 Gen9" or product == "ProLiant DL580 G5" or product == "ProLiant DL580 Gen9" or product == "ProLiant DL80 Gen9":
            disk_list  = []
            disk_list.extend(status.disk_status())
        elif product == "R4900 G2" or product == "UniServer R4900 G3":
            disk_list  = []
            disk_list.extend(status.h3c_disk_status())

	elif product == "RH2288H V3" or product == "RH2288 V3" or product == "PowerEdge R730" or product == "I620-G20" or product == "NF5280M4" or product == "SA5212M4" or product == "PowerEdge M610" or product == "PowerEdge R410" or product == "PowerEdge R620" or product == "PowerEdge R630" or product == "PowerEdge R710" or product == "PowerEdge R910" or product == "I620-C20" or product == "NF5270M3":
            disk_list  = []
            disk_list.extend(status.hw_v3_disk_status())
            disk_list.extend(error.media_error())
            disk_list.extend(error.other_error())
            disk_list.extend(error.Predictive_error())
        print json.dumps(disk_list)
    else:
        return None
if __name__ == '__main__':
    main()
