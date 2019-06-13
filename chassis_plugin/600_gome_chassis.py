#!/usr/bin/env python
import json
import commands
import get_air_inlet as inlet
import get_board_temp as board
import get_fans as fans
import get_lom_card as outlet

product = commands.getstatusoutput("dmidecode -t system | grep 'Product Name'")[1].split(":")[1].strip()
p_list = ["ProLiant DL380 Gen9","ProLiant DL580 Gen8","RH2288 V3","RH2288H V3","I620-G20","NF5280M4","SA5212M4"]
def main():
    if product in p_list:
        if product == "ProLiant DL380 Gen9":
            chassis_list  = []
            chassis_list.extend(fans.fans_status())
            chassis_list.extend(inlet.air_inlet())
            chassis_list.extend(outlet.lom_card())
            chassis_list.extend(board.board_temp())
        elif product == "ProLiant DL580 Gen8":
            chassis_list  = []
            chassis_list.extend(fans.fans_status())
            chassis_list.extend(inlet.air_inlet())
            chassis_list.extend(outlet.dl580g8_lom_card())
            chassis_list.extend(board.board_temp())
    
	elif product == "RH2288H V3" or product == "RH2288 V3":
            chassis_list  = []
            chassis_list.extend(fans.hw_v3_fans_status())
            chassis_list.extend(inlet.hw_v3_air_inlet())
            chassis_list.extend(outlet.hw_v3_lom_card())
            chassis_list.extend(board.hw_v3_board_temp())
        elif product == "I620-G20":
            chassis_list  = []
            chassis_list.extend(fans.sugon_v3_fans_status())
            chassis_list.extend(inlet.sugon_v3_air_inlet())
            chassis_list.extend(outlet.sugon_v3_lom_card())
            chassis_list.extend(board.sugon_v3_board_temp())
        elif product == "NF5280M4" or product == "SA5212M4":
            chassis_list  = []
            chassis_list.extend(fans.inspur_v3_fans_status())
            chassis_list.extend(inlet.hw_v3_air_inlet())
            chassis_list.extend(outlet.hw_v3_lom_card())
            chassis_list.extend(board.sugon_v3_board_temp())

        print json.dumps(chassis_list)
    else:
        return None
if __name__ == '__main__':
    main()
