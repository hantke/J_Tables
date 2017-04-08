###########################################################################################################
################################################ Package ##################################################
#Main Libs
import numpy as np 
from numpy.linalg import norm
################################################ Parameters ##################################################
p0 = 0.681
p1 = 0.089
q0 = -8.013
q1 = -0.775
a0 = 0.71 

#TEST
M1 = 1e12
a1 = 0.8
j1 = 2 #Initial angular momentum

M2 = 1.05e12
a2 = 0.82

################################################ Functions ##################################################
def NoLin_Eq_simpler(a,k,i,A0):#k,i
    return np.where( a > A0, i, k*(a-A0)+i)
def CT_theorical_j(M,a):
	logM = np.log10(M+1e-10)
	p = NoLin_Eq_simpler(a,p1,p0,a0)
	q = NoLin_Eq_simpler(a,q1,q0,a0)
	return 10**(p*logM+q)
############################################### Read ###################################################
j2 = j1 * (CT_theorical_j(M2,a2))/(CT_theorical_j(M1,a1))
print 'log(dm/M) = ','%.2f' % np.log10((M2-M1)/M2),'da = ','%.2f' % (a2-a1),'j1 / (Mpc/h km/s) = ','%.2f' % j1
print 'j2 / (Mpc/h km/s) = ','%.2f' % j2


