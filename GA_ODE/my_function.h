#ifndef MYFUNC_H
#define MYFUNC_H
#include "ParamLoader.h"
#include "Manager.h"
#include <vector>

inline std::vector<double> f(double x, std::vector<double> &y)
{
	double lambda = Prm.beta*y[1]/(y[0]+y[1]+y[2]);
	std::vector<double> f;
	//double *f = new double[3];
	f.push_back(100 -y[0]*(lambda +Prm.mu));
	f.push_back(y[0]*lambda - y[1]*(Prm.my_gamma + Prm.mu));
	f.push_back(y[1]*Prm.my_gamma - y[2]*Prm.mu);
	return f;
}

inline std::vector<double> f(double x, std::vector<double> &y, SGenome &Sg)
{
	double lambda = Sg.beta*y[1]/(y[0]+y[1]+y[2]);
	std::vector<double> f;
	//double *f = new double[3];
	f.push_back(100 -y[0]*(lambda +Sg.mu));
	f.push_back(y[0]*lambda - y[1]*(Sg.my_gamma + Sg.mu));
	f.push_back(y[1]*Sg.my_gamma - y[2]*Sg.mu);
	return f;
}

#endif