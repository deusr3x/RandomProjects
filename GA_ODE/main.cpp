#include <iostream>
#include <fstream>
#include <ctime>
//#include "ParamLoader.h"
#include "Manager.h"
#include "defines.h"
#include "RK4.h"

Manager* manager;
int main()
{
	clock_t ck0 = clock();
	srand((unsigned int)time(NULL));
	manager = new Manager(Prm.CROSSOVER_RATE,Prm.MUTATION_RATE,Prm.POP_SIZE,1,GENE_LENGTH);
	manager->Run();
	for (int i = 0; i<Prm.MAXGEN;i++)
	{
		if (manager->Started())
			manager->Epoch();
		else
			break;
		//std::cout<<manager->Generation()<<std::endl;
		if (Prm.OUTPUT==1)
			manager->SaveRun(i);
		//if (i%1000==1)
		//	manager->GetFittestFitness(manager->GetFittest());
	}


	std::cout<<manager->GetFittest() <<std::endl;
	manager->GetFittestFitness(manager->GetFittest());
	manager->SaveRun(Prm.MAXGEN);
	clock_t ck1 = clock();
	std::cout << "CPU time = " << double(ck1-ck0)/CLOCKS_PER_SEC << " seconds.\n";
	std::cout<<"Press ENTER to close";
	std::cin.ignore(80,'\n');
	return 0;
}
