# Semi-auto pick picking routine
# Prompts user for certain processing parameters


#pc = sys.argv[1]
#mi = sys.argv[2]
#maxi = sys.argv[3]
curdat = CURDATA()
RSR("1","999",show = "n")
RE([curdat[0], curdat[1], "999", curdat[3]], "y")
APKS()
pc = INPUT_DIALOG("PC", "Insert peak separation ppm") 
mi = INPUT_DIALOG("MI", "Insert min relative intensity of peaks") 
maxi = INPUT_DIALOG("Maxi", "Insert max relative intensity of peaks")
PUTPAR("PC",str(pc[0]))
PUTPAR("MI",str(mi[0]))
PUTPAR("MAXI",str(maxi[0]))
#PUTPAR("PC",str(pc))
#PUTPAR("MI",str(mi))
#PUTPAR("MAXI",str(maxi))
PP()