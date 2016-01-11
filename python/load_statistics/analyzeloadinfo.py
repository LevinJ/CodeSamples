#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import visualizeLoadInfo

import os.path
import sys
import shutil
import os
import glob
import re




import os, os.path

from optparse import OptionParser

    
global_itemdict={}
global_loadinfoList=[]

global_current_state ="searchStart"
global_idCount = 0

def parse_arguments():
        
    parser = OptionParser()
    parser.description = \
        "This program takes a detections.data_sequence created by ./objects_detection and converts it into the Caltech dataset evaluation format"

    parser.add_option("-i", "--input", dest="input_path",
                       metavar="FILE", type="string",
                       help="path to the system resource log file")
                                                  
    (options, args) = parser.parse_args()
    # print (options, args)

    if options.input_path:
        if not os.path.exists(options.input_path):
            parser.error("Could not find the input file")
    else:
        parser.error("'input' option is required to run this program")

    return options 

def processMemory(line):
#     print("processMemory")
    global global_itemdict
    searchObj = re.search( r'Mem: (.*)K used, (.*)K free, (.*)K shrd, (.*)K buff, (.*)K cached', line, re.M|re.I)
    global_itemdict['mem']={}
    global_itemdict['mem']['used'] = searchObj.group(1)
    global_itemdict['mem']['free'] = searchObj.group(2)

def processCPU(line):
#     print(line)
    global global_itemdict
    searchObj = re.search('CPU:\s+(.*)% usr (.*)% sys  (.*)% nic (.*)% idle  (.*)% io  (.*)% irq\s+(.*)% sirq', line, re.M|re.I)
    global_itemdict['cpu']={}
    global_itemdict['cpu']['usr'] = searchObj.group(1)
    global_itemdict['cpu']['sys'] = searchObj.group(2)
    global_itemdict['cpu']['idle'] = searchObj.group(4)
    
def processLoad(line):
#     print("processLoad")
    global global_itemdict
    searchObj = re.search( r'Load average: (.*) (.*) (.*) (.*) (.*)', line, re.M|re.I)
    global_itemdict['loadvag']={}
    global_itemdict['loadvag']['1'] = searchObj.group(1)
    global_itemdict['loadvag']['5'] = searchObj.group(2)
    global_itemdict['loadvag']['15'] = searchObj.group(3)

def processCooridnator(line):
#     print("processCoordinatorServ")
    if r'/data/coordinator/CoordinatorServ' in line:
        global global_itemdict
        searchObj = re.search( r'(.*) (.*) /data/coordinator(.*)', line, re.M|re.I)
        global_itemdict['process_coord']={}
        global_itemdict['process_coord']['cpuper'] = searchObj.group(2)
    
    
def procesSda(line):
#     print("processSda")
    if r'/sda_ram/SdaApplication' in line:
        global global_itemdict
        searchObj = re.search( r'(.*) (.*) /sda_ram/SdaApplication(.*)', line, re.M|re.I)
        global_itemdict['process_sda']={}
        global_itemdict['process_sda']['cpuper'] = searchObj.group(2)
        
def processExtractPrc(line):
#     print("processExtractPrc")
    processCooridnator(line)
    procesSda(line)
    
def addDicItem():
    global global_current_state
    global global_itemdict
    global global_loadinfoList
    global global_idCount
    global_idCount = global_idCount + 1
    global_itemdict['id'] = global_idCount;
    global_loadinfoList.append(global_itemdict.copy())
    global_itemdict.clear()
    
    
def processtheline(line):
    global global_current_state
    global global_itemdict
    global global_loadinfoList
    global global_idCount
    while True:
        if(global_current_state=="searchStart"):
            if 'Mem: ' in line:
                global_current_state="Mem_STATE"
            
        if(global_current_state=="Mem_STATE"):
            processMemory(line)
            global_current_state="CPU_STATE"
            return
        
        if(global_current_state=="CPU_STATE"):
            if 'CPU: ' in line:
                processCPU(line)
                global_current_state="LOAD_AVG_STATE"
            return
        if(global_current_state=="LOAD_AVG_STATE"):
            if 'Load average: ' in line:
                processLoad(line)
                global_current_state="EXTRACT_PRC_STATE"
            return
        
        if(global_current_state=="EXTRACT_PRC_STATE"):
            if 'Mem: ' in line:
                #store last dict object in the list
                addDicItem()
                global_current_state="Mem_STATE"
            else:
                processExtractPrc(line)
                return
                
    
def main():
    global global_current_state
    global global_itemdict
    global global_loadinfoList
    global global_idCount
    options = parse_arguments()   
    print (options)
    with open(options.input_path) as f:
            for line in f:
                processtheline(line)  
    #store the last item
    addDicItem()
    visualizeLoadInfo.drawScatter(global_loadinfoList)
#     print(global_loadinfoList)
    return
      
main()

# global_itemdict={}
# global_loadinfoList=[]
# def test():
#     global global_itemdict
#     line = r"  877     1 root     S     283m 56.0   0  7.9 /sda_ram/SdaApplication -n /data/"
#     searchObj = re.search( r'(.*) (.*) /sda_ram/SdaApplication(.*)', line, re.M|re.I)
#     global_itemdict['process_sda']={}
#     global_itemdict['process_sda']['cpuper'] = searchObj.group(2)
#     print(searchObj)
#      
# test()
