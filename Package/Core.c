#include <Python.h>

double *
_OldRandomAngle(double Jx0,double Jy0,double Jz0,double angle,double modulo,double random, double random2, double random3)
{
	double Jx,Jy,Jz,angulo_t,angulo_phi,Jx2,Jy2,Jz2;
	if (random3 > 0.5) angle = -angle;
	if (random < 0.334){
		Jx = Jx0;
		Jy = Jy0*cos(random2)-  Jz0*sin(random2);
		Jz = Jy0*sin(random2) + Jz0*cos(random2);
		angulo_t = acos(Jz/modulo)+angle ;
		angulo_phi = atan2(Jy,Jx);
		Jz = modulo*cos(angulo_t);
		Jy = modulo*sin(angulo_t)*sin(angulo_phi);
		Jx = modulo*sin(angulo_t)*cos(angulo_phi);
		Jx2 = Jx;
		Jy2 = Jy*cos(-1*random2)-  Jz*sin(-1*random2);
		Jz2 = Jy*sin(-1*random2)+  Jz*cos(-1*random2);
	}
	else if (random < 0.667){
		Jx = Jx0*cos(random2) +Jz0*sin(random2);
		Jy = Jy0;
		Jz = -Jx0*sin(random2) + Jz0*cos(random2);
		angulo_t = acos(Jz/modulo)+angle ;
		angulo_phi = atan2(Jy,Jx);
		Jz = modulo*cos(angulo_t);
		Jy = modulo*sin(angulo_t)*sin(angulo_phi);
		Jx = modulo*sin(angulo_t)*cos(angulo_phi);
		Jx2 = Jx*cos(-1*random2) + Jz*sin(-1*random2);
		Jy2 = Jy;
		Jz2 = -Jx*sin(-1*random2)+  Jz*cos(-1*random2);
	}
	else  if (random <= 1)   {
		Jx = Jx0*cos(random2) -Jy0*sin(random2);
		Jy = Jx0*sin(random2) + Jy0*cos(random2);
		Jz = Jz0;
		angulo_t = acos(Jz/modulo)+angle ;
		angulo_phi = atan2(Jy,Jx);
		Jz = modulo*cos(angulo_t);
		Jy = modulo*sin(angulo_t)*sin(angulo_phi);
		Jx = modulo*sin(angulo_t)*cos(angulo_phi);
		Jx2 = Jx*cos(-1*random2) - Jy*sin(-1*random2);
		Jy2 = Jx*sin(-1*random2) + Jy*cos(-1*random2);
		Jz2 = Jz;
	} 
	else{
		angulo_t = acos(Jz0/modulo)+angle ;
		angulo_phi = atan2(Jy0,Jx0);
		Jz = modulo*cos(angulo_t);
		Jy = modulo*sin(angulo_t)*sin(angulo_phi);
		Jx = modulo*sin(angulo_t)*cos(angulo_phi);
		double CosA = cos(random2);
		double SinA = sin(random2);
		Jx2 = (CosA+Jx0*Jx0*(1-CosA))*Jx       +   (Jx0*Jy0*(1-CosA)-Jz0*SinA)*Jy      + (Jx0*Jz0*(1-CosA)+Jy0*SinA)*Jz;
		Jy2 = (Jx0*Jy0*(1-CosA)+Jz0*SinA)*Jx   +     (CosA+Jy0*Jy0*(1-CosA))*Jy        + (Jy0*Jz0*(1-CosA)-Jx0*SinA)*Jz;
		Jz2 =  (Jx0*Jz0*(1-CosA)-Jy0*SinA)*Jx  +    (Jz0*Jy0*(1-CosA)+Jx0*SinA)*Jy     + (CosA+Jz0*Jz0*(1-CosA))*Jz;
		
	}
	static double r[3];
	r[0] = Jx2;
	r[1] = Jy2;
	r[2] = Jz2;
	return  r;
}

double *
_RandomAngle(double Jx0,double Jy0,double Jz0,double angle,double random)
{
	static double r[3];
	double modulo = sqrt(Jx0*Jx0+Jy0*Jy0+Jz0*Jz0);
	if (modulo < 1e-10){
		r[0] = 0;
		r[1] = 0;
		r[2] = 0;
		return  r;
	}
	double Jx,Jy,Jz,angulo_t,angulo_phi,Jx2,Jy2,Jz2;
	Jz0 = Jz0/modulo;
	Jy0 = Jy0/modulo;
	Jx0 = Jx0/modulo;
	angulo_t = acos(Jz0)+angle ;
	angulo_phi = atan2(Jy0,Jx0);
	Jz = cos(angulo_t);
	Jy = sin(angulo_t)*sin(angulo_phi);
	Jx = sin(angulo_t)*cos(angulo_phi);
	double CosA = cos(random);
	double SinA = sin(random);
	Jx2 = (CosA+Jx0*Jx0*(1-CosA))*Jx       +   (Jx0*Jy0*(1-CosA)-Jz0*SinA)*Jy      + (Jx0*Jz0*(1-CosA)+Jy0*SinA)*Jz;
	Jy2 = (Jx0*Jy0*(1-CosA)+Jz0*SinA)*Jx   +     (CosA+Jy0*Jy0*(1-CosA))*Jy        + (Jy0*Jz0*(1-CosA)-Jx0*SinA)*Jz;
	Jz2 =  (Jx0*Jz0*(1-CosA)-Jy0*SinA)*Jx  +    (Jz0*Jy0*(1-CosA)+Jx0*SinA)*Jy     + (CosA+Jz0*Jz0*(1-CosA))*Jz;

	
	r[0] = Jx2*modulo;
	r[1] = Jy2*modulo;
	r[2] = Jz2*modulo;
	return  r;
}
// static PyObject*
// RandomAngle(PyObject* self, PyObject* args)
// {
//     double Jx0;
//     double Jy0;
//     double Jz0;
//     double angle;
//     double modulo;
//     double random;
//     double random2;
//     double random3;
// 
//     if (!PyArg_ParseTuple(args, "dddddddd", &Jx0,&Jy0,&Jz0,&angle,&modulo,&random, &random2, &random3))
//         return NULL;
// 
//     return Py_BuildValue("ddd", _OldRandomAngle(Jx0,Jy0,Jz0,angle,modulo,random, random2, random3)[0],_OldRandomAngle(Jx0,Jy0,Jz0,angle,modulo,random, random2, random3)[1],_OldRandomAngle(Jx0,Jy0,Jz0,angle,modulo,random, random2, random3)[2]);
// }

static PyObject*
RandomAngle(PyObject* self, PyObject* args)
{
    double Jx0;
    double Jy0;
    double Jz0;
    double angle;
    double random;


    if (!PyArg_ParseTuple(args, "ddddd", &Jx0,&Jy0,&Jz0,&angle,&random))
        return NULL;

    return Py_BuildValue("ddd", _RandomAngle(Jx0,Jy0,Jz0,angle,random)[0],_RandomAngle(Jx0,Jy0,Jz0,angle,random)[1],_RandomAngle(Jx0,Jy0,Jz0,angle,random)[2]);
}
static PyMethodDef Prop[] = {
    {"RandomAngle", RandomAngle, METH_VARARGS, "Random Or. a 3d vector in an angle alpha"},
    {NULL, NULL, 0, NULL}
};

PyMODINIT_FUNC
initRandomAngle(void)
{
    (void) Py_InitModule("RandomAngle", Prop);
}