import os
import copy
print("\033c\033[47;30m\ngive me the .pack1 pack file ? \n")
a=input().strip()
f1=open(a,"rb")
f=f1.read()
f1.close()
ff=f.split(b"\x01\x00\x05\x04\x03\x02")
if len(ff)< 2:
    printf("this is not a pack file to 1 file")
    exit(1)
files=copy.copy(ff[0].decode())
fff=files.split("\n")
names=fff[0]
try:
    os.mkdir(names,777)
except:
    pass
os.system("chmod 777 "+names)
counter=0
for d in fff:
    if counter!=0 and d.strip()!="":
        
        f1=open(names+"/"+d,"bw")
        f1.write(ff[counter-1])
        f1.close()
    counter=counter+1

counter=0