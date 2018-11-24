/*
 * Log4cplusWrapper.h
 *
 *  Created on: Nov 23, 2018
 *      Author: Levin Jian
 */

#ifndef LOG4CPLUSWRAPPER_H_
#define LOG4CPLUSWRAPPER_H_

#define LOG4CPLUS_TRACE_Wrp(logEvent) LOG4CPLUS_TRACE(Logger::getRoot(), LOG4CPLUS_TEXT(g_module_name)<<": "<<logEvent)
#define LOG4CPLUS_DEBUG_Wrp(logEvent) LOG4CPLUS_DEBUG(Logger::getRoot(), LOG4CPLUS_TEXT(g_module_name)<<": "<<logEvent)
#define LOG4CPLUS_INFO_Wrp(logEvent) LOG4CPLUS_INFO(Logger::getRoot(), LOG4CPLUS_TEXT(g_module_name)<<": "<<logEvent)
#define LOG4CPLUS_WARN_Wrp(logEvent) LOG4CPLUS_WARN(Logger::getRoot(), LOG4CPLUS_TEXT(g_module_name)<<": "<<logEvent)
#define LOG4CPLUS_ERROR_Wrp(logEvent) LOG4CPLUS_ERROR(Logger::getRoot(), LOG4CPLUS_TEXT(g_module_name)<<": "<<logEvent)
#define LOG4CPLUS_FATAL_Wrp(logEvent) LOG4CPLUS_FATAL(Logger::getRoot(), LOG4CPLUS_TEXT(g_module_name)<<": "<<logEvent)

class Log4cplusWrapper {
public:
	static Log4cplusWrapper& getInstance()
	{
		static Log4cplusWrapper    instance; // Guaranteed to be destroyed.
		// Instantiated on first use.
		return instance;
	}
	void test();
	virtual ~Log4cplusWrapper();

	Log4cplusWrapper(Log4cplusWrapper const&)               = delete;
	void operator=(Log4cplusWrapper const&)  = delete;
//	void log_debug(string module_name, string message);
private:
	Log4cplusWrapper();
};

#endif /* LOG4CPLUSWRAPPER_H_ */
