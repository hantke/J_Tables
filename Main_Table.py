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
Table_Angle =  np.load(DIR+'Table_3D_Purged_Ms2_30sn_Normal_z_Angle_Proj_jmod'  +EXT)
Table_Dir   =  np.load(DIR+'Table_3D_Purged_Ms2_30sn_Normal_z_Dir_Proj_jmod'  +EXT)
##########################################################################################################

def Get_Index_MC(A,amin,amax,NBin= 20):
	B = int((A - amin)/(amax-amin)*NBin)
	return min(max(B,0),NBin-1)
def Simple_Angle(J1,J2):
    Cos_Angl = np.dot(J1,J2)/norm(J1)/norm(J2)
    return np.arccos(Cos_Angl)
def Simple_CosAngle(J1,J2):
    Cos_Angl = np.dot(J1,J2)/norm(J1)/norm(J2)
    return Cos_Angl
def Unit_Vec(J):
    return J/norm(J)

#def Get_Closer_Usefull_ID_3D(A,id1,id2,id3):
	#while True:
		#if A[id1][id2][id3] > -99 or id1 < 0 or id2 < 0 or id3 < 0: return id1,id2,id3
		#if id1 <= id2 and id3 <= id2: id2 -= 1
		#if id2 <= id1 and id3 <= id1: id1 -= 1
		#if id1 <= id3 and id2 <= id3: id3 -= 1

J_old = np.array([0.9,-0.1,0]) #Example angular momentum
J     = np.array([1,0,0])     #Example angular momentum

log_dm   = -1.5    # log(dm/M)
dlogMs   = 0.2   # d log M*
log_M    = 12    # log(M/h^-1 Msun)

i_dm     = Get_Index_MC(log_dm, -3.,0.)
i_Mc     = Get_Index_MC(log_M, 11.,14.5)
i_M     = Get_Index_MC(dlogMs, 0,0.5)

#ind1,ind2,ind3 = Get_Closer_Usefull_ID_3D(i_dm,i_Mc,i_M)
ind1,ind2,ind3 = i_dm,i_Mc,i_M

Angle = Table_Angle[i_dm][i_Mc][i_M]
DIR   = Table_Dir[i_dm][i_Mc][i_M]

if Angle == -99 or DIR == -99:
	print 'Careful, not information of at least one of the tables for the combination of dm,dlogMs,M. Consider using Get_Closer_Usefull_ID_3D()'
#	When we create the tables, if we did not have any data for the combination of dm,dlogMs,M we set the tables to be -99
#	Get_Closer_Usefull_ID_3D() looks for a non-extreme neighbor (with a lower value of i_dm,i_MC and i_M)
else:
	print 'Change of Angle (degrees): ','%.3f' % (np.arccos(Angle)*180./np.pi)
	print 'Change of Direction (degrees)','%.3f' % (np.arccos(DIR)*180./np.pi)
Cos_Phi   = np.cos(min(2*DIR,np.pi)+1e-4) #DIR = 90^o == Phi = 180^o => Random oriented change of angle

count = 0
Cos_alpha1 = Simple_CosAngle(J_old,J)
J1_Unit = Unit_Vec(J_old)
J2_Unit = Unit_Vec(J)
##########################################################################################################
while True:
	J3      = RandAng(J[0],J[1],J[2],Angle,2.*np.pi*np.random.random())
	J3_Unit = Unit_Vec(J3)
	###########################################
	Cos_alpha2 = np.dot(J2_Unit,J3_Unit)
	dJ1_P = J2_Unit*Cos_alpha1-J1_Unit
	dJ2_P = J3_Unit-J2_Unit*Cos_alpha2
	DIR2 = Simple_CosAngle(dJ1_P,dJ2_P)
	###########################################
	if DIR2 > Cos_Phi:
		J_new = J3
		break
	if count > 3000:
		print 'WARNING IN COUNT' #The convination of the change of angle and the change of direction is not possible
		break
		count += 1
				

print 'New AM vector: ','%.3f' % J_new[0],'%.3f' % J_new[1],'%.3f' % J_new[2]
#print '%.3f' % Angle,'%.3f' % Simple_Angle(J,J_new)
