#ifndef MYRAND_H
#define MYRAND_H

#include <cstdlib>
#include <string>
#include <sstream>
#include <vector>

inline double uniRand(){return rand()/double(RAND_MAX);}

inline double uniRand(double a, double b){return (b-a)*uniRand() + a;}

inline int myRandInt(int a, int b){return int((b-a)*uniRand() + a);}

inline std::string IntToStr(int n)
{
	std::ostringstream os;
	os<<n;
	return os.str();
}

inline double checker(const std::vector<double> &data, const std::vector<std::vector<double> > &input)
{
	double totD1=0, totD2=0, totD3=0;
	double data2[] = {476, 747, 1152, 1735, 2524, 3514, 4636, 5774, 6799, 7627};
	std::vector<double> mydata2(data2, data2+sizeof(data2) / sizeof(double));
	double data3[] = {4, 10, 19, 32, 54, 83, 123, 173, 234, 303};
	std::vector<double> mydata3(data3, data3+sizeof(data3) / sizeof(double));

	for(size_t i=0; i< data.size(); i++)
	{
		totD1 += (data[i]-input[i+1][0])*(data[i]-input[i+1][0]) / input[i+1][0];
		totD2 += (data2[i]-input[i+1][1])*(data2[i]-input[i+1][1]) / input[i+1][1];
		totD3 += (data3[i]-input[i+1][2])*(data3[i]-input[i+1][2]) / input[i+1][2];
		//std::cout<<data[i]<<" - "<<input[i+1][0]<<" = "<<data[i]-input[i+1][0]<<std::endl;
	}
	double totD = totD1+totD2+totD3;
	return totD;
}

inline void checker2(const std::vector< std::vector<double> > &input, std::vector<double> &output)
{
	double totD1=0, totD2=0, totD3=0;
	double mydata[] = {8000, 7500, 7500, 6500, 5000, 3500, 4000,2000, 1500, 1000};//{9817, 9538, 9120, 8521, 7707, 6686, 5521, 4330, 3241, 2340};
	std::vector<double> data(mydata, mydata+sizeof(mydata) / sizeof(double));
	double data2[] = {2000, 1000, 1400, 2000, 4000, 4400, 5500, 4800, 6934, 7235};//{476, 747, 1152, 1735, 2524, 3514, 4636, 5774, 6799, 7627};
	std::vector<double> mydata2(data2, data2+sizeof(data2) / sizeof(double));
	double data3[] = {4, 10, 21, 38, 63, 99, 145, 200, 260, 321};//{4, 10, 19, 32, 54, 83, 123, 173, 234, 303};
	std::vector<double> mydata3(data3, data3+sizeof(data3) / sizeof(double));

	for(size_t i=0; i< data.size(); i++)
	{
		totD1 += (data[i]-input[i+1][0])*(data[i]-input[i+1][0]) / input[i+1][0];
		totD2 += (data2[i]-input[i+1][1])*(data2[i]-input[i+1][1]) / input[i+1][1];
		totD3 += (data3[i]-input[i+1][2])*(data3[i]-input[i+1][2]) / input[i+1][2];
		//std::cout<<data[i]<<" - "<<input[i+1][0]<<" = "<<data[i]-input[i+1][0]<<std::endl;
	}
	output.push_back(totD1);
	output.push_back(totD2);
	output.push_back(totD3);
	
}

#endif