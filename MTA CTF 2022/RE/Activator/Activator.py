userName='VN_MSEC_CRACKER'
lenUserNameMod= int(len(userName)/3)
v6=[]
v7=[0,0xda,0xc2,0x11,0x1]
strAntidebug='AntiDebugValueViewer'
for i in range(lenUserNameMod):
    v4=0
    for j in range(3):
        v4=v4+ord(userName[3*i+j])
    v6=v6+[v4]
serial=""
for i in range(lenUserNameMod):
    check=False
    for number in range(0,256):
        if (number ^ ord(strAntidebug[i])&0xff) == v7[i]:
            serial = serial+str(hex(number))[2:]
            check=True
    if not check:
        print("index",i,"not find")
    else:
        serial=serial+'-'
serial=serial[0:-1]
print(serial)