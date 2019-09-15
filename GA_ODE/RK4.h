#ifndef RK4_H
#define RK4_H

#include "ParamLoader.h"
#include "my_function.h"
#include <vector>
#include "Manager.h"

inline std::vector<double> ybarfun(std::vector<double> &k, std::vector<double> &y, int type)
{
	std::vector<double> ybar;
	for (size_t i = 0; i< y.size(); i++)
	{
		if (type == 1)
		{
			ybar.push_back(y[i] + 0.5*Prm.h*k[i]);
		}
		else
		{
			ybar.push_back(y[i] + Prm.h*k[i]);
		}
	}
	return ybar;
}

inline void runge(double x, std::vector<std::vector<double> > & y)
{
	std::vector<double> k1;
	std::vector<double> k2;
	std::vector<double> k3;
	std::vector<double> k4;
	std::vector<double> runge;  
	size_t s1 = y.size();
	k1 = f(x,y[s1-1]);// add in file
	std::vector<double> ybar;
	ybar = ybarfun(k1,y[s1-1],1);
	k2 = f((x+0.5*Prm.h),(ybar));//,mu,beta,my_gamma);
	ybar.clear();
	ybar = ybarfun(k2,y[s1-1],1);
	k3 = f((x+0.5*Prm.h),ybar);//,mu,beta,my_gamma);
	ybar.clear();
	ybar = ybarfun(k3,y[s1-1],0);
	k4 = f((x+Prm.h),ybar);//,beta,my_gamma);
	ybar.clear();
	
	for (size_t i = 0; i<y[0].size(); i++)
	{
		runge.push_back(y[s1-1][i] + (Prm.h/6)*(k1[i]+2*k2[i]+2*k3[i]+k4[i]));
	}
	y.push_back(runge);
	k1.clear();
	k2.clear();
	k3.clear();
	k4.clear();
	runge.clear();
	//delete [] k1, k2, k3, k4;
}

inline void runge(double x, std::vector<std::vector<double> > & y, SGenome& Sg)
{
	std::vector<double> k1;
	std::vector<double> k2;
	std::vector<double> k3;
	std::vector<double> k4;
	std::vector<double> runge;  
	size_t s1 = y.size();
	k1 = f(x,y[s1-1],Sg);// add in file
	std::vector<double> ybar;
	ybar = ybarfun(k1,y[s1-1],1);
	k2 = f((x+0.5*Prm.h),(ybar),Sg);//,mu,beta,my_gamma);
	ybar.clear();
	ybar = ybarfun(k2,y[s1-1],1);
	k3 = f((x+0.5*Prm.h),ybar,Sg);//,mu,beta,my_gamma);
	ybar.clear();
	ybar = ybarfun(k3,y[s1-1],0);
	k4 = f((x+Prm.h),ybar,Sg);//,beta,my_gamma);
	ybar.clear();
	
	for (size_t i = 0; i<y[0].size(); i++)
	{
		runge.push_back(y[s1-1][i] + (Prm.h/6)*(k1[i]+2*k2[i]+2*k3[i]+k4[i]));
	}
	y.push_back(runge);
	k1.clear();
	k2.clear();
	k3.clear();
	k4.clear();
	runge.clear();
}
#endif