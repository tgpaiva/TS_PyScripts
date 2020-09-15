# Multiplies all gp in gpnam list by 3 %
# DiffBB (60A) z gradient (1768 Gcm) conversion to regular HR probes 50 (Gcm) gradient (10A) for HR pp sequences

#  variable creation
gradient = [] 

# read gpnam array as a string
grad_HR = GETPAR("GPZ") 

# convert strings to a list of floats
grad_HR = [float(x) for x in grad_HR.split()] 

# transform HR gradients  to diff gradients 53 / 1700 ~ 0.03 
grad_diffbb = [grad_HR[x] * 0.03 for x in range (len(grad_HR))] 

# write gpz values to gpnam array
for z in range (len(grad_diffbb)): 
		PUTPAR("GPZ {}".format(str(z)), str(grad_diffbb[z]))