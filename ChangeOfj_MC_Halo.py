##########################################################################################################
print "######################################################"
print "Starting the code!! Good Luck!!"
################################################ Package ##################################################
#Main Libs
import numpy as np 
from numpy.linalg import norm
from RandomAngle import RandomAngle as RandAng
print "Package Load"
############################################### Read ###################################################
DIR = 'Tables/'
EXT = '.npy'
Table_Mod =  np.load(DIR+'Table_3D_Purged_Ms2_30sn_Normal_z_dj_Proj_jmod'  +EXT)
##########################################################################################################
def Get_Index_MC(A,amin,amax,NBin= 20):
	B = int((A - amin)/(amax-amin)*NBin)
	return min(max(B,0),NBin-1)
##########################################################################################################


log_dm   = -1.5    # log(dm/M)
dlogMs   = 0.2   # d log Mc
log_M    = 12    # log(M/h^-1 Msun)

i_dm     = Get_Index_MC(log_dm, -3.,0.)
i_Mc     = Get_Index_MC(log_M, 11.,14.5)
i_M     = Get_Index_MC(dlogMs, 0,0.5)

j1 = 2


dj = Table_Mod[i_dm][i_Mc][i_M]
j2 = j1 * 10**dj

print 'log(dm/M) = ','%.2f' % log_dm,'dlog(Mc) = ','%.2f' % dlogMs,'j1 / (Mpc/h km/s) = ','%.2f' % j1
print 'j2 / (Mpc/h km/s) = ','%.2f' % j2
