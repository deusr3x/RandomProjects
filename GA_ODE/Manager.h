#ifndef MANAGER_H
#define MANAGER_H
#include <vector>
#include <iostream>
#include "myRandomFcns.h"
#include "defines.h"
#include "ParamLoader.h"

struct SGenome
{
	//double dFitness;
	double dFitness1,dFitness2,dFitness3;

	double mu, beta, my_gamma, popstart;

	//SGenome():dFitness(0){}
	SGenome():dFitness1(0),dFitness2(0),dFitness3(0) {}

	//SGenome(const int num_bits):dFitness(0)
	SGenome(const int num_bits):dFitness1(0),dFitness2(0),dFitness3(0)
	{
		mu = uniRand(MIN_MU, MAX_MU);//RandDouble
		beta = uniRand(MIN_BETA,MAX_BETA);//RandD
		my_gamma = uniRand(MIN_GAMMA, MAX_GAMMA);//Prm.my_gamma;//RandD
		popstart = myRandInt(MIN_POPSTART,MAX_POPSTART);
	}
	bool operator==(const SGenome& rhs) const
	{
		if ((beta == rhs.beta) && (mu == rhs.mu) && (my_gamma == rhs.my_gamma))
		{
			return true;
		}
		else
		{
			return false;
		}
	}
};

class Manager
{
private:
	std::vector<SGenome> m_vecGenomes;
	SGenome BestGene;
	std::vector<std::vector<double> > fittest;
	int m_iPopSize;
	double m_dCrossoverRate;
	double m_dMutationRate;
	int m_iFittestGenome;
	//double m_dBestFitnessScore;
	double m_dBestFitnessScore1,m_dBestFitnessScore2,m_dBestFitnessScore3;
	double m_dTotalFitnessScore;
	int m_iGeneration, m_iGeneLength;
	bool m_bBusy;
	SGenome& RouletteWheelSelection();
	void Crossover(SGenome &mum, SGenome &dad, SGenome &baby1,SGenome &baby2);
	void Mutate(SGenome &in);
	void CreateStartPopulation();
public:
	Manager(double cross_rat,
         double mut_rat,
         int    pop_size,
         int    num_bits,
         int    gene_len):m_dCrossoverRate(cross_rat),
                          m_dMutationRate(mut_rat),
                          m_iPopSize(pop_size),
                          m_dTotalFitnessScore(0.0),
                          m_iGeneration(0),
                          m_iGeneLength(gene_len),
                          m_bBusy(false)
	{
		CreateStartPopulation();
	};
	~Manager(void);

	void Epoch();
	void Mutate();
	void UpdateFitness();
	int	Generation(){return m_iGeneration;}
	int	GetFittest(){return m_iFittestGenome;}
	void GetFittestFitness(int in)
	{
		//std::cout<<m_vecGenomes[in].dFitness<<std::endl;
		/*std::cout<<m_vecGenomes[in].dFitness1<<"\t"<<m_vecGenomes[in].dFitness2<<"\t"<<m_vecGenomes[in].dFitness3<<std::endl;
		std::cout<<"beta: "<<m_vecGenomes[in].beta<<std::endl;
		std::cout<<"mu: "<<m_vecGenomes[in].mu<<std::endl;
		std::cout<<"gamma: "<<m_vecGenomes[in].my_gamma<<std::endl;
		std::cout<<"startpop: "<<m_vecGenomes[in].popstart<<std::endl;*/
		std::cout<<BestGene.dFitness1<<"\t"<<BestGene.dFitness2<<"\t"<<BestGene.dFitness3<<std::endl;
		std::cout<<"beta: "<<BestGene.beta<<std::endl;
		std::cout<<"mu: "<<BestGene.mu<<std::endl;
		std::cout<<"gamma: "<<BestGene.my_gamma<<std::endl;
		std::cout<<"startpop: "<<BestGene.popstart<<std::endl;
	}
	bool Started(){return m_bBusy;}
	void Stop(){m_bBusy = false;}
	void Run();
	void SaveRun(int gen);

};

#endif