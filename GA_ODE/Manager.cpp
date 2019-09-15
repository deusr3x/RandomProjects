#include "Manager.h"
#include "ParamLoader.h"
#include "RK4.h"
#include <fstream>
#include <sstream>

Manager::~Manager(void)
{
}


void Manager::UpdateFitness()
{
	m_iFittestGenome		= 0;
	//m_dBestFitnessScore		= 10000;
	/*m_dBestFitnessScore1		= 10000;
	m_dBestFitnessScore2		= 10000;
	m_dBestFitnessScore3		= 10000;*/
	m_dTotalFitnessScore	= 0;
	for (size_t j = 0; j<m_vecGenomes.size();j++)
	{
		double tstep = (Prm.tend-Prm.tstart)/Prm.h;
		std::vector<std::vector<double> > y;

		std::vector<double> temp;
		temp.push_back(m_vecGenomes[j].popstart);
		temp.push_back(300);
		temp.push_back(0);
		y.push_back(temp);

		for (int i = 0; i < (int)tstep; i++)
		{
			double x = Prm.tstart + Prm.h*i;
			runge(x,y,m_vecGenomes[j]);
		}
		//double data[] = {9817, 9538, 9120, 8521, 7707, 6686, 5521, 4330, 3241, 2340};
		//std::vector<double> mydata(data, data+sizeof(data) / sizeof(double));
		//m_vecGenomes[j].dFitness = checker(mydata, y);
		std::vector<double> output;
		checker2(y, output);
		m_vecGenomes[j].dFitness1 = output[0];
		m_vecGenomes[j].dFitness2 = output[1];
		m_vecGenomes[j].dFitness3 = output[2];
		//m_dTotalFitnessScore += m_vecGenomes[j].dFitness;
		//if (m_vecGenomes[j].dFitness < m_dBestFitnessScore)
		//if ((m_vecGenomes[j].dFitness1 < m_dBestFitnessScore1) && (m_vecGenomes[j].dFitness2 < m_dBestFitnessScore2) && (m_vecGenomes[j].dFitness3 < m_dBestFitnessScore3))
		if (m_vecGenomes[j].dFitness1+m_vecGenomes[j].dFitness2+m_vecGenomes[j].dFitness3 < m_dBestFitnessScore1+m_dBestFitnessScore2+m_dBestFitnessScore3)
		{
			//m_dBestFitnessScore = m_vecGenomes[j].dFitness;
			std::cout << m_dBestFitnessScore1 << " vs " << m_vecGenomes[j].dFitness1 << " | " <<
				m_dBestFitnessScore2 << " vs " << m_vecGenomes[j].dFitness2 << " | " <<
				m_dBestFitnessScore3 << " vs " << m_vecGenomes[j].dFitness3<< std::endl;
			m_dBestFitnessScore1 = m_vecGenomes[j].dFitness1;
			m_dBestFitnessScore2 = m_vecGenomes[j].dFitness2;
			m_dBestFitnessScore3 = m_vecGenomes[j].dFitness3;
			fittest = y;
			m_iFittestGenome = j;
			BestGene = m_vecGenomes[j];
			if ( (output[0]<=Prm.EPSILON) && (output[1] <= Prm.EPSILON) && (output[2] <= 0.055))//Prm.EPSILON))//(m_vecGenomes[j].dFitness <= 3*Prm.EPSILON)
			{
				//is so, stop the run
				//std::cout<<j<<std::endl;
				//std::cout<<m_vecGenomes[j].dFitness<<std::endl;
				//GetFittestFitness(j);
				m_bBusy = false;
			}
		}
	}
}

void Manager::Epoch()
{
	UpdateFitness();

	int NewBabies = 0;
	std::vector<SGenome> vecBabyGenomes;
	while (NewBabies < m_iPopSize)
	{
		//select 2 parents
		SGenome mum = RouletteWheelSelection();
		SGenome dad = m_vecGenomes[myRandInt(0,m_iPopSize+1)];//RouletteWheelSelection();

		//operator - crossover
		SGenome baby1, baby2;
		Crossover(mum, dad, baby1, baby2);

		//operator - mutate
		Mutate(baby1);
		Mutate(baby2);

		//add to new population
		vecBabyGenomes.push_back(baby1);
		vecBabyGenomes.push_back(baby2);

		NewBabies += 2;
	}
	if(Started())
		m_vecGenomes = vecBabyGenomes;
	++m_iGeneration;
}

SGenome& Manager::RouletteWheelSelection()
{
	/*double fSlice = uniRand()*m_dTotalFitnessScore;

	double cfTotal = 0.0;

	int SelectedGenome = 0;

	for (int i=0; i<m_iPopSize; ++i)
	{
		
		cfTotal += m_vecGenomes[i].dFitness;
		
		if (cfTotal > fSlice) 
		{
			SelectedGenome = i;
			break;
		}
	}
	
	return m_vecGenomes[SelectedGenome];*/
	return BestGene;//m_vecGenomes[m_iFittestGenome];
}
void Manager::Crossover(SGenome &mum, SGenome &dad, SGenome &baby1,SGenome &baby2)
{
	if ( (uniRand() > m_dCrossoverRate) || (mum == dad)) 
	{
		baby1 = mum;
		baby2 = dad;

		return;
	}
	int pnum = myRandInt(1,5);
	switch(pnum)
	{
	case 1:
		{
			baby1 = dad;
			baby1.beta = mum.beta;
			baby2 = mum;
			baby2.beta = dad.beta;
			break;
		}
	case 2:
		{
			baby1 = dad;
			baby1.mu = mum.mu;
			baby2 = mum;
			baby2.mu = dad.mu;
			break;
		}
	case 3:
		{
			baby1 = dad;
			baby1.my_gamma = mum.my_gamma;
			baby2 = mum;
			baby2.my_gamma = dad.my_gamma;
			break;
		}
	case 4:
		{
			baby1 = dad;
			baby1.popstart = mum.popstart;
			baby2 = mum;
			baby2.popstart = dad.popstart;
			break;
		}
	default:
		{
			baby1 = mum;
			baby2 = dad;
			break;
		}
	}
}

void Manager::Mutate(SGenome &in)
{
	if (uniRand() < m_dMutationRate)
	{
		int pnum = myRandInt(1,5);
		switch(pnum)
		{
		case 1:
			{
				in.beta = in.beta*uniRand(0.85,1.15);//uniRand(MIN_BETA,MAX_BETA);
				if (in.beta == 0.0)
					in.beta = uniRand(MIN_BETA,MAX_BETA);
				//else
				//	in.beta = uniRand(MIN_BETA,in.beta);
				break;
			}
		case 2:
			{
				in.mu = in.mu*uniRand(0.85,1.15);//uniRand(MIN_MU,MAX_MU);
				if (in.mu < 0.0+Prm.EPSILON)
					in.mu = uniRand(MIN_MU,MAX_MU);
				/*else
					in.mu = uniRand(MIN_MU,in.mu);*/
				break;
			}

		case 3:
			{
				in.my_gamma = in.my_gamma*uniRand(0.85,1.15);//uniRand(MIN_GAMMA,MAX_GAMMA);
				if (in.my_gamma < 0.0+Prm.EPSILON)
					in.my_gamma = uniRand(MIN_GAMMA,MAX_GAMMA);
				/*else
					in.my_gamma = uniRand(MIN_GAMMA,in.my_gamma);*/
				break;
			}
		case 4:
			{
				in.popstart = (int)in.popstart*uniRand(0.85,1.15);
				if (in.popstart < 0.0+Prm.EPSILON)
					in.popstart = uniRand(MIN_POPSTART,MAX_POPSTART);
				break;
			}
		default:
			{

			}
		}
	}
}

void Manager::CreateStartPopulation()
{
	m_vecGenomes.clear();
	
	for (int i=0; i<m_iPopSize; i++)
	{
		m_vecGenomes.push_back(SGenome(1));
	}

	m_iGeneration		 = 0;
	m_iFittestGenome	 = 0;
	//m_dBestFitnessScore		= 10000;
	m_dBestFitnessScore1		= 10000;
	m_dBestFitnessScore2		= 10000;
	m_dBestFitnessScore3		= 10000;
	m_dTotalFitnessScore = 0;
}

void Manager::Run()
{
	CreateStartPopulation();
	m_bBusy = true;
}

void Manager::SaveRun(int gen)
{
	std::ofstream outfile;
	std::string filename = "fitgen";
	filename.append(IntToStr(gen));
	outfile.open(("Fitruns/" +filename+".bin").c_str(),std::ios::out | std::ios::binary);
	for (size_t i = 0; i<fittest.size(); i++)
	{
		for(size_t j = 0; j<fittest[i].size();j++)
		{
			outfile.write(reinterpret_cast<const char*> (&fittest[i][j]), sizeof(double));
		}
	}
}
