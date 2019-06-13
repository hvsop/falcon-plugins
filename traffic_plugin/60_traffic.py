#!/usr/bin/env python
import json,commands
import time,datetime
import sys,os

t=str(int(time.time()))

if os.path.exists('/tmp/dates'):
  f=open('/tmp/dates','r')
  old_t=f.read()
else:
  old_t="0"

f=open('/tmp/dates','w')
f.write(t)
f.close()

timer=int(t)-int(old_t)

i = 0
o = 0
info = os.popen("cat /proc/net/dev|grep -vE 'Inter\-| face|lo\:|bond|vnet|br[0-9]|br\_|br\-|tap\-|kube\-|veth|dummy|tun|docker'")
trafficinfo=info.read()
info.close()

inlist=[]
num = 1
while len(trafficinfo) != 0:
        inlist.append(int(trafficinfo.split()[num]))
        num = num + 17
        if num >= len(trafficinfo.split()):
                break
else:pass

outlist=[]
num = 9
while len(trafficinfo) != 0:
        outlist.append(int(trafficinfo.split()[num]))
        num = num + 17
        if num >= len(trafficinfo.split()):
                break
else:pass

if os.path.exists('/tmp/traffic.in'):
  f=open('/tmp/traffic.in','r')
#  print (type(f.read()))
  type(f.read())
  if len(f.read()) == 0:
    old_in=0
  else:
    old_in=int(f.read())
else:
  old_in=0
i=sum(inlist)
f=open('/tmp/traffic.in','w')
f.write(str(i))
f.close()

if os.path.exists('/tmp/traffic.out'):
  f=open('/tmp/traffic.out','r')
#  print (type(f.read()))
  type(f.read())
  if len(f.read()) == 0:
    old_out=0
  else:
    old_out=int(f.read())
else:
  old_out=0
o=sum(outlist)
f=open('/tmp/traffic.out','w')
f.write(str(o))
f.close()

speedin=0
speedout=0

speedin=(i-old_in)/timer*8
speedout=(o-old_out)/timer*8

endpoint = commands.getstatusoutput("curl -s http://127.0.0.1:1988/plugin/endpoint")[1]
output_list=[]

def output_dict(mt,speed):
    disk_dict = {}
    disk_dict["metric"] = mt
    disk_dict["value"] = speed 
    disk_dict["endpoint"] = endpoint
    disk_dict["timestamp"] = int(time.time())
    disk_dict["counterType"] = "GAUGE"
    disk_dict["step"] = 60
    disk_dict["tags"] = ""
    output_list.append(disk_dict)
    return output_list

output_dict("net.traffic.in.bits",speedin)
output_dict("net.traffic.out.bits",speedout)
print json.dumps(output_list)

