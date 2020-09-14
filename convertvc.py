curdat = CURDATA()

d20=GETPAR("D 20")
p2=GETPAR("P 2")
mult = 2 * float(d20) + float(p2)/1e6

AQPATH=(curdat[3]+"/"+curdat[0] + "/"+curdat[1]+ "/" + "vclist")
vclist=open(AQPATH).readlines()
vclist = list(map(int,vclist))

vdlist=[]
for i in range (len(vclist)):
    iterator=mult * vclist[i]
    vdlist.append(iterator)
   
WPATH=(curdat[3]+"/"+curdat[0] + "/"+curdat[1]+ "/" + "vdlist")
with open(WPATH, 'w') as f: #gradlist output path
   for item in vdlist:
       f.write("%s\n" % item)