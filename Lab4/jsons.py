import json
with open('sample-data.json') as file:
    data=json.load(file)
print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU")
print("-------------------------------------------------- --------------------  ------  ------")
s=data['imdata']
for i in s:
    l=i["l1PhysIf"]
    a=l["attributes"]
    dn=a['dn']
    speed=a['speed']
    mtu=a['mtu']
    c=""
    if(dn != "topology/pod-1/node-201/sys/phys-[eth1/33]"):
        if(dn != "topology/pod-1/node-201/sys/phys-[eth1/34]"):
            if(dn != "topology/pod-1/node-201/sys/phys-[eth1/35]"):
                continue
    if(len(dn) == 42):
        c+=dn+" "*30+speed+"   "+mtu
    else:
        c+=dn+" "*31+speed+"   "+mtu
    print(c)