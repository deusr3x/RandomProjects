#ifndef CONVERTER_H
#define CONVERTER_H

#include <string>
#include <iostream>
#include <sstream>

class Converter
{
	public:
		template <typename T>
		static std::string T_to_string(T const &val) 
		{
			std::ostringstream ostr;
			ostr << val;

			return ostr.str();
		}

		
		template <typename T>
		static T string_to_T(std::string const &val) 
		{
			std::istringstream istr(val);
			T returnVal;
			if (!(istr >> returnVal))
				std::cout<<"not a valid type"<<std::endl;//exitWithError("CFG: Not a valid " + (std::string)typeid(T).name() + " received!\n");
			//istr >> returnVal;
			return returnVal;
		}
		/*template <>
		static std::string string_to_T(std::string const &val)
		{
			return val;
		}*/
		//template <>
		//static std::string string_to_T(std::string const &val);
};

#endif