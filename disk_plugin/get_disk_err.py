#!/usr/bin/env python
import commands
import time

endpoint = commands.getstatusoutput("curl -s http://127.0.0.1:1988/plugin/endpoint")[1]

slot_num = "/opt/MegaRAID/MegaCli/MegaCli64 -PDList -aAll | grep 'Slot Number'"
media_err = "/opt/MegaRAID/MegaCli/MegaCli64 -PDList -aAll | grep 'Media Error Count'"
other_err = "/opt/MegaRAID/MegaCli/MegaCli64 -PDList -aAll | grep 'Other Error Count'"
Predictive_fail = "/opt/MegaRAID/MegaCli/MegaCli64 -PDList -aAll | grep 'Predictive Failure Count'"

cmd_state1,slot = commands.getstatusoutput(slot_num)
cmd_state2,media = commands.getstatusoutput(media_err)
cmd_state3,other = commands.getstatusoutput(other_err)
cmd_state4,Predictive = commands.getstatusoutput(Predictive_fail)

def media_error():
    try:
        if cmd_state1 == 0 and cmd_state2 == 0 :
            output_list = []
            slot_list = slot.split("\n")
            media_list = media.split("\n")
            slot_number = len(slot_list)
            for i in range(slot_number):
                t1 = slot_list[i].split(":")[0].strip()
                t2 = slot_list[i].split(":")[1].strip()
                k = t1 + '_' + t2 
                v = media_list[i].split(":")[1].strip()
                me_err_dict = {}
                me_err_dict["metric"] = "gome_media_error"
                me_err_dict["value"] = v
                me_err_dict["endpoint"] = endpoint
                me_err_dict["timestamp"] = int(time.time())
                me_err_dict["counterType"] = "GAUGE"
                me_err_dict["step"] = 600
                me_err_dict["tags"] = "Disk=%s,type=alarm"%k
                output_list.append(me_err_dict)
            return output_list
        else:
            return []
    except:
        return []

def other_error():
    try:
        if cmd_state1 == 0 and cmd_state3 == 0 :
            output_list = []
            slot_list = slot.split("\n")
            other_list = other.split("\n")
            slot_number = len(slot_list)
            for i in range(slot_number):
                t1 = slot_list[i].split(":")[0].strip()
                t2 = slot_list[i].split(":")[1].strip()
                k = t1 + '_' + t2 
                v = other_list[i].split(":")[1].strip()
                other_err_dict = {}
                other_err_dict["metric"] = "gome_other_error"
                other_err_dict["value"] = v
                other_err_dict["endpoint"] = endpoint
                other_err_dict["timestamp"] = int(time.time())
                other_err_dict["counterType"] = "GAUGE"
                other_err_dict["step"] = 600
                other_err_dict["tags"] = "Disk=%s,type=alarm"%k
                output_list.append(other_err_dict)
            return output_list
        else:
            return []
    except:
        return []    

def Predictive_error():
    try:
        if cmd_state1 == 0 and cmd_state4 == 0 :
            output_list = []
            slot_list = slot.split("\n")
            Predictive_list = Predictive.split("\n")
            slot_number = len(slot_list)
            for i in range(slot_number):
                t1 = slot_list[i].split(":")[0].strip()
                t2 = slot_list[i].split(":")[1].strip()
                k = t1 + '_' + t2 
                v = Predictive_list[i].split(":")[1].strip()
                Predictive_err_dict = {}
                Predictive_err_dict["metric"] = "gome_Predictive_fail"
                Predictive_err_dict["value"] = v
                Predictive_err_dict["endpoint"] = endpoint
                Predictive_err_dict["timestamp"] = int(time.time())
                Predictive_err_dict["counterType"] = "GAUGE"
                Predictive_err_dict["step"] = 600
                Predictive_err_dict["tags"] = "Disk=%s,type=alarm"%k
                output_list.append(Predictive_err_dict)
            return output_list
        else:
            return []
    except:
        return []
