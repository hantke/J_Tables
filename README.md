Angular momentum evolution  in Dark Matter haloes
Contreras, Padilla & Lagos 2017
__________________________________________________


The following codes allowed to evolve the 
(specific) angular momentum 'J' ('j') of 
following the procedure presented in 
Contreras et al. 2017.

Any doubt or concern please do not hesitate
in contacting me at stcontre@uc.cl

To run the codes just run:
python <name_of_the_file.py>

###########################################
ChangeOfAngle.py

It changes the vector 'J' in an angle 'Angle' 
in a random direction.

###########################################
ChangeOfDir.py

It changes the vector 'J' in an angle 'Angle'.
For a large sample of vectors, the average
change of direction of the vector will be
'DIR'.

###########################################
Main_Table.py

It changes the vector 'J' in an angle 'Angle'.
For a large sample of vectors, the average
change of direction of the vector will be
'DIR'. The value of 'Angle' and the value 
of 'DIR' are calculated from the change of
mass that affects the halo (dm/M), the change
of Mc(z) in which this change of mass occurs
(dlogMc) and the mass of the halo (M).

###########################################

j_modCT96.py

Gives the modulus of 'j' using as input the
mass of the halo and the scale factor 'a'
(equations 11-14 of Contreras et al. 2017)

###########################################

ChangeOfj_CT96.py

It changes the modulus of 'j' using as input
the mass of the halo, the scale factor 'a', 
de change of mass of the halo and the change in 'a'
following equation 15 of Contreras et al. 2017

###########################################

ChangeOfj_MC_Halo.py

Same as 'Main_Table.py' but calculate the change on
the modulus of 'j' instead of its angle.

