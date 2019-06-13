#!/usr/bin/env python
import commands,re,time

endpoint = commands.getstatusoutput("curl -s http://127.0.0.1:1988/plugin/endpoint")[1]

output_list = []

def disk_status():
    try:
        cmd_state, cmd_result = commands.getstatusoutput("ssacli ctrl all show config | grep physicaldrive")
        if cmd_state == 0:
            disk_list = cmd_result.strip("\n").split("\n")
        else:
            return []

        for item in disk_list:
            k1 = item.split()[0].strip()
            k2 = item.split()[1].strip()
            k = k1 + "_" +  k2
            v =  item.split()[10].strip(")")
            if v == "OK":
                v = 0
            else:
                v = 1
            disk_dict = {}
            disk_dict["metric"] = "gome_disk_status"
            disk_dict["value"] = v
            disk_dict["endpoint"] = endpoint
            disk_dict["timestamp"] = int(time.time())
            disk_dict["counterType"] = "GAUGE"
            disk_dict["step"] = 60
            disk_dict["tags"] = "Disk=%s,type=alarm"%k
            output_list.append(disk_dict)
        return output_list
    except:
        return []

def hw_v3_disk_status():
    try:
        cmd1_state,slot_number = commands.getstatusoutput("/opt/MegaRAID/MegaCli/MegaCli64 -PDList -aAll | grep 'Slot Number'")
        cmd2_state,disk_status = commands.getstatusoutput("/opt/MegaRAID/MegaCli/MegaCli64 -PDList -aAll | grep 'Firmware state'")
        if cmd1_state == 0 and cmd2_state == 0:
            slot = re.sub(':\s+','_',slot_number)
            status = re.sub('Firmware state:','',disk_status)
            tmp_var = re.sub(',.*','',status)
            slot_list = slot.split("\n")
            status_list = tmp_var.split("\n")
            list_number = len(slot_list)
            l = []
            for i in range(list_number):
                temp = slot_list[i]
                l.append(temp)
        
            for item in range(list_number):
                k = l[item]
                v = status_list[item]
                if v == " Online":
                    v = 0
                else:
                    v = 1
                disk_dict = {}
                disk_dict["metric"] = "gome_disk_status"
                disk_dict["value"] = v
                disk_dict["endpoint"] = endpoint
                disk_dict["timestamp"] = int(time.time())
                disk_dict["counterType"] = "GAUGE"
                disk_dict["step"] = 60
                disk_dict["tags"] = "Disk=%s,type=alarm"%k
                output_list.append(disk_dict)
            return output_list
        else:
            return []
    except:
        return []
