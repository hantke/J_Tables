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
##########################################################################################################
def Simple_Angle(J1,J2):
    Cos_Angl = np.dot(J1,J2)/norm(J1)/norm(J2)
    return np.arccos(Cos_Angl)

def Simple_CosAngle(J1,J2):
    Cos_Angl = np.dot(J1,J2)/norm(J1)/norm(J2)
    return Cos_Angl
def Unit_Vec(J):
    return J/norm(J)

J_old = np.array([0.9,-0.1,0]) #Example angular momentum
J     = np.array([1,0,0])     #Example angular momentum
Angle = np.pi/6. #30^o change of angle
DIR   = 0        #The change of angle is full correlated
Cos_Phi   = np.cos(min(2*DIR,np.pi)+1e-4) #DIR = 90^o == Phi = 180^o => Random oriented change of angle

print 'Change of Angle (degrees): ','%.3f' % (np.arccos(Angle)*180./np.pi)
print 'Change of Direction (degrees)','%.3f' % (np.arccos(DIR)*180./np.pi)

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
