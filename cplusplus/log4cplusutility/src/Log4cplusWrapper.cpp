/*
 * Log4cplusWrapper.cpp
 *
 *  Created on: Nov 23, 2018
 *      Author: Levin Jian
 */

//https://stackoverflow.com/questions/17039665/how-to-access-modify-matrix-element-in-opencv-why-at-is-templatized
#include "Log4cplusWrapper.h"
#include <log4cplus/logger.h>
#include <log4cplus/fileappender.h>
#include <log4cplus/layout.h>
#include <log4cplus/ndc.h>
#include <log4cplus/helpers/loglog.h>
#include <log4cplus/helpers/property.h>
#include <log4cplus/loggingmacros.h>
#include <log4cplus/initializer.h>
#include "log4cplus/consoleappender.h"
#include <stdio.h>
#include <stdlib.h>
#include <ftw.h>
#include <string>

#include <stdio.h>
#include <stdlib.h>
#include <ftw.h>

using namespace log4cplus;
using namespace std;

static char g_module_name[] = "tracking";

static int rmFiles(const char *pathname, const struct stat *sbuf, int type, struct FTW *ftwb)
{
	if(remove(pathname) < 0)
	{
		perror("ERROR: remove");
		return -1;
	}
	return 0;
}

Log4cplusWrapper::Log4cplusWrapper() {
	// TODO Auto-generated constructor stub
	static log4cplus::Initializer initializer;
	helpers::LogLog::getLogLog()->setInternalDebugging(true);

	std::string log_path = "logs";

	//appender for logfiles
	if (nftw(log_path.c_str(), rmFiles,10, FTW_DEPTH|FTW_MOUNT|FTW_PHYS) >= 0)
	{
		log4cplus::tcout << "removed directory " << log_path << std::endl;
	}

	SharedFileAppenderPtr append_1(
			new RollingFileAppender(LOG4CPLUS_TEXT((log_path + "/log.txt").c_str()), 10*1024*1024, // 10 MB
					5, false, true));
	append_1->setName(LOG4CPLUS_TEXT("logfiles"));
	Logger::getRoot().addAppender(SharedAppenderPtr(append_1.get ()));

	//appender for console
	log4cplus::SharedAppenderPtr append_2(
			new log4cplus::ConsoleAppender(false, true));
	append_2->setName(LOG4CPLUS_TEXT("console"));
	Logger::getRoot().addAppender(SharedAppenderPtr(append_2.get ()));

}

Log4cplusWrapper::~Log4cplusWrapper() {
	// TODO Auto-generated destructor stub
}

void Log4cplusWrapper::test() {
	const int LOOP_COUNT = 5;
	// TODO Auto-generated constructor stub
	Logger root = Logger::getRoot();

	LOG4CPLUS_TRACE_Wrp("looks good, right?");
	LOG4CPLUS_DEBUG_Wrp("looks good, right?");
	LOG4CPLUS_INFO_Wrp("looks good, right?");
	LOG4CPLUS_WARN_Wrp("looks good, right?");
	LOG4CPLUS_ERROR_Wrp("looks good, right?");
	LOG4CPLUS_FATAL_Wrp("looks good, right?");

	LOG4CPLUS_INFO(root,
			LOG4CPLUS_TEXT("This is")
			        << LOG4CPLUS_TEXT(" a reall")
			        << LOG4CPLUS_TEXT("y long message.") << std::endl);

	for(int i=0; i<LOOP_COUNT; ++i) {
		LOG4CPLUS_DEBUG_Wrp("Entering loop #" << i);
	}
}

