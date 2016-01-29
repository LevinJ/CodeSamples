import re
from datetime import datetime
import numpy as np
import pandas as pd
import os

class Extract_Data_Proxy:
    def __init__(self):
        self.current_state="loopidline"
        self.rawlinesDict = {'loopidline': {'keysubstr':'SdaEngine Run Loop id:', 'nextstate':'orbstartline','rawline':''}, 
                             'orbstartline': {'keysubstr':'ORB ProcessJobsWhenAvailable start:','nextstate':'orbendline','rawline':''},
                             'orbendline': {'keysubstr':'ORB ProcessJobsWhenAvailable end:', 'nextstate':'notestartline','rawline':''},
                             'notestartline': {'keysubstr':'StateMgr ProcessJobs start:','nextstate':'noteendline','rawline':''},
                             'noteendline': {'keysubstr':'StateMgr ProcessJobs end:', 'nextstate':'loopidline','rawline':''},}
        
        self.overallStats = {'loopid': [], 'orbDuration':[], 'noteProcDuration': []}
#         self.overallStats = {'loopid': [], 'orbDuration':[], 'noteProcDuration': [], 'loopidline':[],'orbstartline':[],'orbendline':[],'notestartline':[],'noteendline':[]}
        return
    def processLine_protected(self,line):
        try:
            self.processline(line)
        except:
            print "Exception handling line :   ", line
            return False
        else:
            return True
    def processline(self, line):
        if self.rawlinesDict[self.current_state]['keysubstr'] in line:
            self.rawlinesDict[self.current_state]['rawline'] = line
#             print line
#             if 'StateMgr ProcessJobs end:' in line :
            if self.current_state == 'noteendline':
                self.processrecord()
            #go to next state    
            self.current_state = self.rawlinesDict[self.current_state]['nextstate']
        return           
    def processrecord(self): 
        self.overallStats['orbDuration'].append(self.getOrbDuration())
        self.overallStats['noteProcDuration'].append(self.getNoteProcDuration())
        self.overallStats['loopid'].append(self.getCurrentLoopId())
#         self.overallStats['loopidline'].append(self.rawlinesDict['loopidline']['rawline'])
#         self.overallStats['orbstartline'].append(self.rawlinesDict['loopidline']['rawline'])
#         self.overallStats['orbendline'].append(self.rawlinesDict['loopidline']['rawline'])
#         self.overallStats['notestartline'].append(self.rawlinesDict['loopidline']['rawline'])
#         self.overallStats['noteendline'].append(self.rawlinesDict['loopidline']['rawline'])
        return 
    def getCurrentLoopId(self): 
        loopline = self.rawlinesDict['loopidline']['rawline']
        return self.getLoopId(loopline)
    def getOrbDuration(self):
        timeStart = self.rawlinesDict['orbstartline']['rawline']
        timeEnd = self.rawlinesDict['orbendline']['rawline']
        return self.getDuration(timeStart, timeEnd)
    def getNoteProcDuration(self):
        timeStart = self.rawlinesDict['notestartline']['rawline']
        timeEnd = self.rawlinesDict['noteendline']['rawline']
        return self.getDuration(timeStart, timeEnd)
    def getDuration(self,timeStart, timeEnd):
        timeStart = self.__getTime(timeStart)
        timeEnd = self.__getTime(timeEnd)
        timeStart = datetime.strptime(timeStart, '%H:%M:%S.%f')
        timeEnd = datetime.strptime(timeEnd, '%H:%M:%S.%f')
        if ((timeEnd -timeStart).microseconds) == 0:
            return 0
        return ((timeEnd -timeStart).microseconds)/1000
    def __getTime(self,line):
        return line[-14:-2] 
    def calStatistics(self):
        df = pd.DataFrame(self.overallStats)
        print df.describe()
        df.to_csv("data.csv")
        
        return
    
    def iterateFiles(self,dir):
        all_files = []
        for subdir, dirs, files in os.walk(dir):
            for filename in files:
#                 print os.path.join(subdir, filename)
                all_files.append(os.path.join(subdir, filename))
        return all_files
    def getLoopId(self,line): 
        searchObj = re.search( r'(.*)SdaEngine Run Loop id:  (.*)', line[:-15], re.M|re.I)
        return searchObj.group(2)       
    def process(self, input_path):
        all_files = self.iterateFiles(input_path)
        for filename in all_files:
            print filename
            with open(filename) as f:
                for line in f:
                    res = self.processLine_protected(line)
                    if not res:
                        return
        self.calStatistics()
        return
    
    

if __name__ == "__main__":
    obj = Extract_Data_Proxy()
    obj.iterateFiles(r'C:\Projects\Issues\unexpected_notes\traces')
    obj.process(r'C:\Projects\Issues\unexpected_notes\traces')