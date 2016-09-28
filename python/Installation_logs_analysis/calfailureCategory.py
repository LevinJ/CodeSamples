#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import os.path
import sys
import shutil
import os
import glob
import re
import rebootstatistics




import os, os.path

from optparse import OptionParser

from openpyxl import Workbook
    

def parse_arguments():
        
    parser = OptionParser()
    parser.description = \
        "This program takes a detections.data_sequence created by ./objects_detection and converts it into the Caltech dataset evaluation format"

    parser.add_option("-i", "--input", dest="input_path",
                       metavar="FILE", type="string",
                       help="path to the installation result file")
                                                  
    (options, args) = parser.parse_args()
    # print (options, args)

    if options.input_path:
        if not os.path.exists(options.input_path):
            parser.error("Could not find the input file")
    else:
        parser.error("'input' option is required to run this program")

    return options 

current_state="searchStart"
current_loopStr=""
wb = Workbook()
ws = wb.active
ws.append(["NO", "RealFailure","Category","Loop", "SessionID","USB issue times","Failure details"])
current_numId=0
current_failureLine=""
current_errorcategory=""
current_usbfailedtimes=0
current_sessionid = ''
reboottimestatistic = rebootstatistics.rebootstatisticsProxy()
def getErrorCategory(failedinstallation,line):
    if 'FAILED: Target: DEC/RebootKernel installation failed, error: eInstallTimeout' in line:
        return "USB"
    if 'exception: ' in line:
        return "PRC_LZMA"
    if 'eInstallTimeout' in line:
        return "eInstallTimeout"
    if 'eUnknownError' in line:
        return "eUnknownError"
    if 'eConfigError' in line:
        return "eConfigError"
    if 'install operation failed due to exception!' in line:
        return "PRC"
    if not failedinstallation:
        return "PRC"
    return "Others"
def getLoopNumber(line):
    m = re.search('this is loop (.*) out of', line)
    if m:
        loopnum = m.group(1)
        return loopnum
    return "NOT FOUND"

def markSessionId(line):
    global current_sessionid
    if not 'ProductionScripts::Prc::Common::Session: created token session' in line:
        return
    #only process the first seesionid used to handle usb enumeration issue
    if current_sessionid !='':
        return

    m = re.search('(.*)INFO -- ProductionScripts::Prc::Common::Session: created token session (.*)-(.*)-(.*)', line)
    if m:
        current_sessionid = m.group(4)
        return
    current_sessionid = "NOT FOUND"

def markUSBfailedTimes(line):
    global current_usbfailedtimes
    if 'ProductionScripts::Prc::Process::Packages::Verify ' in line:
        current_usbfailedtimes = current_usbfailedtimes + 1
        
def processtheline(line):
    global current_state
    global current_loopStr
    global current_numId
    global current_failureLine
    global current_errorcategory
    global ws;
    global current_usbfailedtimes
    global reboottimestatistic
    global current_sessionid
    markUSBfailedTimes(line)
    markSessionId(line)
    reboottimestatistic.processLine(line)
    if(current_state=="searchStart"):
        if 'this is loop' in line:
            current_state="searchFailureorEnd"
            current_loopStr = line
            current_usbfailedtimes = 0
            current_sessionid = ''
#           print(line)
        #exit the search start state
        return
    if(current_state=="searchRealFailureOrEnd"):
        #find a false failure, log it and then start next iteration
        if '## total=' in line: 
            current_state="searchStart"
            ws.append([current_numId, "FALSE",getErrorCategory(False,current_failureLine),getLoopNumber(current_loopStr), current_sessionid,current_usbfailedtimes,current_failureLine])
            #return here since we've reached the end of this iteration
            return
        #find a real failure, log it and then start next iteration
        if 'Error: Installation failed at loop' in line:
            current_state="searchStart"
            ws.append([current_numId, "TRUE",getErrorCategory(True,current_failureLine),getLoopNumber(current_loopStr),current_sessionid, current_usbfailedtimes,current_failureLine])
            #return here since we've found the first error occurence
            return
        return
    #Here we can be sure we are in the searchFailureorEnd state now
    if(current_state=="searchFailureorEnd"):
        if '## total=' in line:
            current_state="searchStart"
            #return here since we've reached the end of this iteration
            return
        #find the first occurence of failure, log it and then start next iteration
        if ('failed' in line) or ('exception: ' in line):
            current_state="searchRealFailureOrEnd"
            current_failureLine=line
            print(getLoopNumber(current_loopStr))
            print(line)
            current_numId += 1;
            #return here since we've found the first error occurence
            return
        return
    
def main():
    global wb
    global reboottimestatistic
    options = parse_arguments()   
    print (options)
    with open(options.input_path) as f:
            for line in f:
                processtheline(line)
#     with open(options.input_path) as f:
#         for line in f:  
#     wb.save("sample.xlsx")
    wb.save(options.input_path+".xlsx")  
#     reboottimestatistic.getFinalResult(options.input_path) 
    return
      
main()

def test():
#     wb = Workbook()
#     ws = wb.active
#     ws.append(["NO", "Loop", "Failure details"])
#     ws.append([4, 5, 6])
#     wb.save("sample.xlsx")
#     print("ok")
    global current_sessionid
    line = r'I, [2016-01-21T20:34:02.605865 #9160]  INFO -- ProductionScripts::Prc::Common::Session: created token session 947409-589761-207319'
    markSessionId(line)
    print(current_sessionid)
    return
# test()
