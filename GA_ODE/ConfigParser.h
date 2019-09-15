#ifndef CONFIG_H
#define CONFIG_H

#include <map>
#include <iostream>
#include <string>

class ConfigParser
{
	public:
		std::map<std::string, std::string> configs;
		std::string fname;
		ConfigParser(std::string);
		~ConfigParser();
	private:
		void parseLine(std::string &line, size_t num);
		void extractContents(std::string &line) ;
		void extractKey(std::string &key, size_t const &sepPos, const std::string &line);
		void extractValue(std::string &value, size_t const &sepPos, const std::string &line);
		void removeComment(std::string &line);
		bool onlyWhitespace(const std::string &line);
};

#endif