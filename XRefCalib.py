# Takes the SR correction in a 1D Proton spectrum and calculates the required correction
# for X spectrum (ie 13C, 15N)
# constant definition
NUC = [1.0000000000,0.1013291180,0.2514495300] # 1H , 15N , 13C 

B = INPUT_DIALOG("Field", "Insert B0 in MHz\n in exemple 400, 500..", ["field = "], ["400"]) 
if B[0] == '400': 
	BF = [400.1500000,40.5468470,100.6177980] # 1H , 15N , 13C 
elif B[0] == '500': 
	BF = [500.3400000,50.6990119,
125.8105931]
elif B[0] == '600': 
	BF = [600.1300000,60.8106450,
150.902809]

nuc = INPUT_DIALOG("Ref Calib", "Insert nucleus\nC or N", ["NUCLEUS = "], ["C"], [""], ["1"]) 
if nuc[0] == 'N':
	nuc = NUC[1]
	bfref = BF[1]
elif  nuc[0] == 'C':
	nuc = NUC[2]
	bfref = BF[2]

curdat = CURDATA()
RefDataExpno = INPUT_DIALOG("Ref Data", "Insert reference dataset number", ["Expno = "], 
["5"])
RE([curdat[0],RefDataExpno[0],"1",curdat[3] + '/'])
bfcorr = GETPAR2("SF") 
float(bfcorr)
bfcorr = nuc * float(bfcorr)
SR = (bfcorr - bfref) * 1E6
RefDataExpno = INPUT_DIALOG("Dataset to Calib", "Insert dataset requiring calibration", ["Expno = "], 
["4"])
RE([curdat[0],RefDataExpno[0],"1",curdat[3] + '/'])
PUTPAR ("SR",str(SR))
EFP()
APKS()