from pwn import *
import re
import time

pattern = '\d+'


def tinh(a,b):
    trong=0
    tren=a+b+1
    if a > b:
        a,b=b,a
    for i in range(1,a):
        x=int((a-i)*b/a)
        if a*x==(a-i)*b:
            tren+=1
            x=x-1
        trong+=x
    return tren,trong

r= remote("14.225.254.58", 55555)
context.log_level = 'debug'
recv=''
r.recvline()
r.recvline()


while 1:    
    recv = r.recvline().decode()
    if ('MSEC' in str(recv) ):
        print(recv)
        break
    if 'a' in str(recv) and 'b' in str(recv)and '=' in str(recv) :
        recv=re.findall(pattern, str(recv)) 
        a=int(recv[1])
        b=int(recv[3])
        tren,trong = tinh(a,b)
        recv=r.recvuntil(b"= ")
        r.sendline(str(tren).encode())
        recv=r.recvuntil(b"= ")
        r.sendline(str(trong).encode())
    


        