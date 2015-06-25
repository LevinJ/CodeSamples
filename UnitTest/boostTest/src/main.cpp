//============================================================================
// Name        : boostTest.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <boost/lambda/lambda.hpp>
#include <boost/regex.hpp>
#include <iterator>
#include <algorithm>
#include <iostream>
using namespace std;

int main() {
	cout<<"this is ok"<<endl;
	std::string line;
	boost::regex pat( "^Subject: (Re: |Aw: )*(.*)" );
//
//	while (std::cin)
//	{
//		std::getline(std::cin, line);
//		boost::smatch matches;
//		if (boost::regex_match(line, matches, pat))
//			std::cout << matches[2] << std::endl;
//	}
	//	using namespace boost::lambda;
	//	typedef std::istream_iterator<int> in;
	//
	//	std::for_each(
	//			in(std::cin), in(), std::cout << (_1 * 3) << " " );
	return 0;
}
