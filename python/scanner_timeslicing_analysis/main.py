#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import extractData

import os.path
import sys
import shutil
import os
import glob
import re




import os, os.path

from optparse import OptionParser

    


def parse_arguments():
        
    parser = OptionParser()
    parser.description = \
        "This program takes in a bundh of scanner log files and output time slicing statistics for two tasks: note processing and orb communication"

    parser.add_option("-i", "--input", dest="input_path",
                       metavar="FILE", type="string",
                       help="path to the log file")
                                                  
    (options, args) = parser.parse_args()
    # print (options, args)

    if options.input_path:
        if not os.path.exists(options.input_path):
            parser.error("Could not find the input file")
    else:
        parser.error("'input' option is required to run this program")

    return options 

  
def main():
    options = parse_arguments()   
    print (options)
    exData = extractData.Extract_Data_Proxy()
    exData.process(options.input_path)
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
