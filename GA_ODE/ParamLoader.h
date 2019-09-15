#ifndef PARAM_LOAD_H
#define PARAM_LOAD_H

#include "ConfigParser.h"
#include "Converter.h"

#define Prm (*ParamLoader::Instance())

class ParamLoader
{
private:
	ParamLoader()
	{
		ConfigParser cfg("config.txt"); // Load the file
		// Assign the parameters, note the keywords must match that in the config file
		h = Converter::string_to_T<double>(cfg.configs.find("h")->second);
		mu = Converter::string_to_T<double>(cfg.configs.find("mu")->second);
		my_gamma = Converter::string_to_T<double>(cfg.configs.find("gamma")->second);
		beta = Converter::string_to_T<double>(cfg.configs.find("beta")->second);
		tstart = Converter::string_to_T<double>(cfg.configs.find("tstart")->second);
		tend = Converter::string_to_T<double>(cfg.configs.find("tend")->second);
		EPSILON = Converter::string_to_T<double>(cfg.configs.find("EPSILON")->second);
		CROSSOVER_RATE = Converter::string_to_T<double>(cfg.configs.find("CROSSOVER_RATE")->second);
		MUTATION_RATE = Converter::string_to_T<double>(cfg.configs.find("MUTATION_RATE")->second);
		POP_SIZE = Converter::string_to_T<int>(cfg.configs.find("POP_SIZE")->second);
		OUTPUT = Converter::string_to_T<int>(cfg.configs.find("OUTPUT")->second);
		MAXGEN = Converter::string_to_T<int>(cfg.configs.find("MAXGEN")->second);
	}
public:
	static ParamLoader* Instance();
	~ParamLoader(void);
	double h, mu, my_gamma, beta, tstart, tend,EPSILON,CROSSOVER_RATE,MUTATION_RATE;
	int POP_SIZE, OUTPUT, MAXGEN;
};

#endif