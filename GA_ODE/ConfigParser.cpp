#include "ConfigParser.h"
#include <fstream>
#include <cstdlib>

ConfigParser::ConfigParser(std::string fname)
{
	this->fname = fname;
	std::ifstream infile;
	infile.open(fname.c_str(), std::ios::in);
	if (!infile)
	{
		std::cout<<"Error with file"<<std::endl;
		exit(1);
	}
	std::string line;
	size_t lineNo = 0;
	while (std::getline(infile, line))
	{
		lineNo++;
		std::string temp = line;
		if (temp.empty())
			continue;
		removeComment(temp);
		if (onlyWhitespace(temp))
			continue;
		parseLine(temp, lineNo);
	}
	infile.close();
}
void ConfigParser::removeComment(std::string &line)
{
	if (line.find(';') != line.npos)
		line.erase(line.find(';'));
}
bool ConfigParser::onlyWhitespace(const std::string &line)
{
	return (line.find_first_not_of(' ') == line.npos);
}
void ConfigParser::parseLine(std::string &line, size_t num)
{
	if (line.find('=') == line.npos)
	{
		std::cout<<"no separator in line "<<num<<std::endl;//exitWithError("CFG: Couldn't find separator on line: " + Convert::T_to_string(lineNo) + "\n");
		exit(1);
	}

	//if (!validLine(line))
	//	std::cout<<"bad format"<<std::endl;//exitWithError("CFG: Bad format for line: " + Convert::T_to_string(lineNo) + "\n");

	extractContents(line);
}
void ConfigParser::extractKey(std::string &key, size_t const &sepPos, const std::string &line)
{
	key = line.substr(0, sepPos);
	if (key.find('\t') != line.npos || key.find(' ') != line.npos)
		key.erase(key.find_first_of("\t "));
}
void ConfigParser::extractValue(std::string &value, size_t const &sepPos, const std::string &line)
{
	value = line.substr(sepPos + 1);
	value.erase(0, value.find_first_not_of("\t "));
	value.erase(value.find_last_not_of("\t ") + 1);
}

void ConfigParser::extractContents(std::string &line) 
{
	std::string temp = line;
	temp.erase(0, temp.find_first_not_of("\t "));
	size_t sepPos = temp.find('=');
	std::string key, value;
	extractKey(key, sepPos, temp);
	extractValue(value, sepPos, temp);
	
	configs.insert(std::pair<std::string, std::string>(key, value));
	/*if (!keyExists(key))
		configs.insert(std::pair<std::string, std::string>(key, value));
	else
		std::cout<<"need unique names"<<std::endl;//exitWithError("CFG: Can only have unique key names!\n");*/
}

ConfigParser::~ConfigParser()
{
}