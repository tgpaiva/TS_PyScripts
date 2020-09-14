curdat = CURDATA()
st=(curdat[3]+"/"+curdat[0] +"/" + curdat[1]+"/pdata/" + curdat[2])
i_file=st+"/TopSpinDC.xml"
text_file = open(i_file, "r")
pl=open(i_file).readlines()
m=[]
d=[]
n=[]
gradients=[]
for line in pl:
    d1=line.split('   ') 
    m.append(d1)
i=m.index(['', ' <XValues>\n'])
ii=m.index(['</DynamicsCenterInterfaceSection>\n'])     
for g in range (i+1,ii-1):
    p=(m[g])
    d.append(p)
for h in range (0,len(d)):    
    string=str(d[h][2])
    n.append(string)
for w in range (0,len(d)):
    a=n[w].find("g=")
    aa=n[w].find("q=")
    g1=float(n[w][a+3:aa-2])
    gradients.append(g1)
with open('/Users/Tiago/Desktop/grad.txt', 'w') as f: #gradlist output path
    for item in gradients:
        f.write("%s\n" % item)