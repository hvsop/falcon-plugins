#!/usr/bin/env python
#import json
import commands

cmd_state, cmd_result = commands.getstatusoutput('cat /etc/redhat-release|xargs |grep " 5"')
if cmd_state == 0:
  import simplejson as json
else:
  import json

import get_power_status as status
import get_power_watts as watts

product = commands.getstatusoutput("dmidecode -t system | grep 'Product Name'")[1].split(":")[1].strip()
p_list = ["ProLiant DL380 Gen9","ProLiant DL580 G7","ProLiant DL580 Gen8","ProLiant DL380 G7","ProLiant DL360p Gen8","ProLiant DL380p Gen8","ProLiant DL580 Gen9","ProLiant DL388p Gen8","ProLiant DL380e Gen8","ProLiant DL80 Gen9","ProLiant DL388 Gen9","ProLiant DL388eGen8","ProLiant DL380 G6","RH2288 V3","RH2288H V3","Tecal RH2288H V2-8S","I620-G20","I620-C20","NF5280M4","SA5212M4","PowerEdge R710","PowerEdge R720","PowerEdge R730","PowerEdge R730xd","PowerEdge R620","PowerEdge R630","PowerEdge R910","PowerEdge R410"," PowerEdge R420","PowerEdge M610","PowerEdge M910","R4900 G2","UniServer R4900 G3"]
def main():
    if product in p_list:
        if product == "ProLiant DL380 Gen9" or product == "ProLiant DL580 G7" or product == "ProLiant DL580 Gen8" or product == "ProLiant DL380 G7" or product == "ProLiant DL360p Gen8" or product == "ProLiant DL380p Gen8"or product == "ProLiant DL580 Gen9" or product == "ProLiant DL388p Gen8" or product == "ProLiant DL380e Gen8" or product == "ProLiant DL80 Gen9" or product == "ProLiant DL388 Gen9" or product == "ProLiant DL388eGen8" or product == "ProLiant DL380 G6":
            power_list = []
            power_list.extend(status.power_status())
            power_list.extend(watts.power_watts())
            power_list.extend(watts.power_watts_sum())
	elif product == "RH2288H V3" or product == "RH2288 V3" or product == "Tecal RH2288H V2-8S":
            power_list = []
            power_list.extend(status.hw_v3_power_status())
            power_list.extend(watts.hw_v3_power_watts())
            power_list.extend(watts.power_watts_sum())
        elif product == "I620-G20" or product == "I620-C20" or product == "NF5280M4" or product == "SA5212M4":
            power_list = []
            power_list.extend(status.sugon_v3_power_status())
            power_list.extend(watts.sugon_v3_power_watts())
            power_list.extend(watts.power_watts_sum())
        elif product == "PowerEdge R730" or product == "PowerEdge R730xd" or product == "PowerEdge R910" or product == "PowerEdge R410" or product == " PowerEdge R420" or product == "PowerEdge M610" or product == "PowerEdge M910" or product == "PowerEdge R710" or product == "PowerEdge R720" or product == "PowerEdge R620" or product == " PowerEdge R630":
            power_list = []
            power_list.extend(status.dell_power_status())
            power_list.extend(watts.dell_power_watts())
            power_list.extend(watts.power_watts_sum())
        elif product == "R4900 G2" or product == "UniServer R4900 G3":
            power_list = []
            power_list.extend(status.h3c_power_status())
            power_list.extend(watts.h3c_power_watts())
            power_list.extend(watts.power_watts_sum())
        print json.dumps(power_list)
    else:
        return None
if __name__ == '__main__':
    main()
