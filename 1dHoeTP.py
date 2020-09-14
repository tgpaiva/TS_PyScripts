#curdat = CURDATA()
p16 = GETPAR ("P 16")
d16 = GETPAR ("D 16")

mixlist=[0.002, 0.050, 0.0100, 0.200]

vdlist=[]
for i in range(len(mixlist)):
  d=mixlist[i] - float(p16) * 1E-6 - float(d16) - 54 * 1E-6
  vdlist.append(d)


WPATH=("/opt/topspin3.5pl7/exp/stan/nmr/lists/vd/" + "HOESY19F1H_TP")
with open(WPATH,'w') as f:
  for item in vdlist:
	  f.write("%s\n" % item)

#PUTPAR("VDLIST", "HOESY19F1H_TP")