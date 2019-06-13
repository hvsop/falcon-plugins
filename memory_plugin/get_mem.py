#!/usr/bin/env python
import commands,time,re

endpoint = commands.getstatusoutput("curl -s http://127.0.0.1:1988/plugin/endpoint")[1]

def dimm_status():
    try:
        dimm_list = []
        cmd_state1,cmd_result1 = commands.getstatusoutput("hpasmcli -s 'show dimm' | grep Status")
        cmd_state2,cmd_result2 = commands.getstatusoutput("hpasmcli -s 'show dimm' | grep Processor")
        cmd_state3,cmd_result3 = commands.getstatusoutput("hpasmcli -s 'show dimm' | grep Module")

        if cmd_state1 == 0 and  cmd_state2 == 0 and cmd_state3 == 0:
            status = re.sub('Status:.\s+','',cmd_result1)
            process = re.sub('#:.\s+','',cmd_result2)
            dimm_socket = re.sub('#:.\s+','',cmd_result3)
            status_list = status.split("\n")
            process_list = process.split("\n")
            socket_list = dimm_socket.split("\n")
            list_number = len(process_list)
            l = []
            for i in range(list_number):
                temp = process_list[i] + "_" + socket_list[i]
                l.append(temp)
            
            for item in range(list_number):
                k = l[item]
                v = status_list[item]
                if v == "Ok" or v == "DIMM is present, but not in use":
                    v = 0
                else:
                    v = 1
                dimm_dict = {}
                dimm_dict["metric"] = "gome_mem_status"
                dimm_dict["value"] = v
                dimm_dict["endpoint"] = endpoint
                dimm_dict["timestamp"] = int(time.time())
                dimm_dict["counterType"] = "GAUGE"
                dimm_dict["step"] = 600
                dimm_dict["tags"] = "dimm=%s,type=alarm"%k
                dimm_list.append(dimm_dict)
            return dimm_list
        else:
            return [] 
    except:
        return []

def dl580g7_dimm_status():
    try:
        dimm_list = []
        cmd_state1,cmd_result1 = commands.getstatusoutput("hpasmcli -s 'show dimm' | grep Status")
        cmd_state2,cmd_result2 = commands.getstatusoutput("hpasmcli -s 'show dimm' | grep Cartridge")
        cmd_state3,cmd_result3 = commands.getstatusoutput("hpasmcli -s 'show dimm' | grep Module")

        if cmd_state1 == 0 and  cmd_state2 == 0 and cmd_state3 == 0:
            status = re.sub('Status:.\s+','',cmd_result1)
            process = re.sub('#:.\s+','',cmd_result2)
            dimm_socket = re.sub('#:.\s+','',cmd_result3)
            status_list = status.split("\n")
            process_list = process.split("\n")
            socket_list = dimm_socket.split("\n")
            list_number = len(process_list)
            l = []
            for i in range(list_number):
                temp = process_list[i] + "_" + socket_list[i]
                l.append(temp)
            
            for item in range(list_number):
                k = l[item]
                v = status_list[item]
                if v == "Ok" or v == "DIMM is present, but not in use":
                    v = 0
                else:
                    v = 1
                dimm_dict = {}
                dimm_dict["metric"] = "gome_mem_status"
                dimm_dict["value"] = v
                dimm_dict["endpoint"] = endpoint
                dimm_dict["timestamp"] = int(time.time())
                dimm_dict["counterType"] = "GAUGE"
                dimm_dict["step"] = 600
                dimm_dict["tags"] = "dimm=%s,type=alarm"%k
                dimm_list.append(dimm_dict)
            return dimm_list
        else:
            return [] 
    except:
        return []



def hw_v3_dimm_status():
    try:
        output_list = []
        cmd_state, cmd_result = commands.getstatusoutput("ipmitool sdr list | grep ^DIMM")
        if cmd_state == 0:
            dimm_status_list =  cmd_result.strip("\n").split("\n")
        else:
            return []
        for item in dimm_status_list:
            k = item.split("|")[0].strip()
            v =  item.split("|")[2].strip()
            if v == "ok":
                v = 0
            else:
                v = 1
            dimm_status_dict = {}
            dimm_status_dict["metric"] = "gome_mem_status"
            dimm_status_dict["value"] = v
            dimm_status_dict["endpoint"] = endpoint
            dimm_status_dict["timestamp"] = int(time.time())
            dimm_status_dict["counterType"] = "GAUGE"
            dimm_status_dict["step"] = 600
            dimm_status_dict["tags"] = "dimm=%s,type=alarm"%k
            output_list.append(dimm_status_dict)
        return output_list
    except:
        return []

def sugon_v3_dimm_status():
    try:
        output_list = []
        cmd_state, cmd_result = commands.getstatusoutput("ipmitool sdr list | grep Memory_Watts")
        if cmd_state == 0:
            dimm_status_list =  cmd_result.strip("\n").split("\n")
        else:
            return []
        for item in dimm_status_list:
            k = item.split("|")[0].strip()
            v =  item.split("|")[2].strip()
            if v == "ok":
                v = 0
            else:
                v = 1
            dimm_status_dict = {}
            dimm_status_dict["metric"] = "gome_mem_status"
            dimm_status_dict["value"] = v
            dimm_status_dict["endpoint"] = endpoint
            dimm_status_dict["timestamp"] = int(time.time())
            dimm_status_dict["counterType"] = "GAUGE"
            dimm_status_dict["step"] = 600
            dimm_status_dict["tags"] = "dimm=%s,type=alarm"%k
            output_list.append(dimm_status_dict)
        return output_list
    except:
        return []
