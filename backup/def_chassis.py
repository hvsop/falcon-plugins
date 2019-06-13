#!/usr/bin/env python
import os
import socket
import time
import json
hostname = socket.gethostname()

temp_list = []

def fans_status():
    cmd_res = os.popen("hpasmcli -s 'show fans' | grep -E '^#'").read()
    fans_list =  cmd_res.strip("\n").split("\n")
    for item in fans_list:
        k = item.split()[0].strip()
        v =  item.split()[2].strip()
        if v == "Yes":
            v = 0
        else:
            v = 1
        fans_dict = {}
        fans_dict["metric"] = "gome_fans_status"
        fans_dict["value"] = v
        fans_dict["endpoint"] = hostname
        fans_dict["timestamp"] = int(time.time())
        fans_dict["counterType"] = "GAUGE"
        fans_dict["step"] = 60
        fans_dict["tags"] = "fans=%s,type=alarm"%k
        temp_list.append(fans_dict)
    print json.dumps(temp_list)
if __name__ == '__main__':
    fans_status()
