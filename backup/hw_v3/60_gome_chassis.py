#!/usr/bin/env python
import json
import commands
import get_air_inlet as inlet
import get_board_temp as board
import get_fans as fans
import get_lom_card as outlet

product = commands.getstatusoutput("dmidecode -t system | grep 'Product Name'")[1].split(":")[1].strip()

chassis_list  = []

if product == "ProLiant DL380 Gen9":
    chassis_list.extend(fans.fans_status())
    chassis_list.extend(inlet.air_inlet())
    chassis_list.extend(outlet.lom_card())
    chassis_list.extend(board.board_temp())

elif product == "RH2288 V3":
    chassis_list.extend(fans.hw_v3_fans_status())
    chassis_list.extend(inlet.hw_v3_air_inlet())
    chassis_list.extend(outlet.hw_v3_lom_card())
    chassis_list.extend(board.hw_v3_board_temp())
print json.dumps(chassis_list)
