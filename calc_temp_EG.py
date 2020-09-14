def calcTcorr():
	PUTPAR("MI","30")
	PUTPAR("MAXI","110")
	PUTPAR("CY","100")
	PP()
	list = GETPEAKSARRAY()
	slist=""
	for peak in list:
		slist += str(round(peak.getPositions()[0],4)) + "\t";
	peak=slist.split()
	pp1=float(peak[0])
	pp2=float(peak[1])
	delta=pp1-pp2
	tcor=-99.00 * delta + 463.00
	return (delta,tcor)
curdat=CURDATA()
res1=[]
res2=[]
for i in range(1,11):
	RE_PATH(curdat[3]+"/"+curdat[0]+"/"+str(i)+"/pdata/1")
	(d,t)=calcTcorr()
	res1.append(d)
	res2.append(t)
	res = [[res1[i], res2[i]] for i in range(len(res1))]

with open('/Users/Tiago/Desktop/EG.txt', 'w') as f: #Output path to ddelta values and calculated T
	for item in res:
		f.write("%s\n" % item)

#tecalc = -99.00 * delta + 463.00; EG pure