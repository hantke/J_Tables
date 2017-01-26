##########################################################################################################
print "######################################################"
print "Starting the code!! Good Luck!!"
################################################ Package ##################################################
#Main Libs
import numpy as np 
from numpy.linalg import norm
from RandomAngle import RandomAngle as RandAng
print "Package Load"
##########################################################################################################

def Simple_Angle(J1,J2):
    Cos_Angl = np.dot(J1,J2)/norm(J1)/norm(J2)
    return np.arccos(Cos_Angl)

J     = np.array([1,0,0])     #Example angular momentum
Angle = np.pi/6. #30^o change of angle

J_new = RandAng(J[0],J[1],J[2],Angle,2.*np.pi*np.random.random())
# RandAng( Jx, Jy, Jz, Angle in radians, random seed- between 0-2*pi)

print 'Change of Angle (degrees): ','%.3f' % (np.arccos(Angle)*180./np.pi)

print 'New AM vector: ','%.3f' % J_new[0],'%.3f' % J_new[1],'%.3f' % J_new[2]
print Angle,Simple_Angle(J,J_new) # sanity check, input angle and real change of angle between J and J_new
##########################################################################################################

