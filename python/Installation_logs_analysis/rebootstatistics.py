import numpy as np
from datetime import datetime
import pandas as pd
import re
import rebootVisualize


class rebootstatistics:
    def __init__(self,rebootname):
        self.startLine = ''
        self.endLine = ''
        self.startimeline_whole = ''
        self.startimelines = []
        self.startimelines_whole = []#the whole line
        self.endtimelines = []
        self.durations = []
        self.rebootname = rebootname
        self.beginlinemark = '[DEC/' + rebootname + '] Begin installing target'
        self.endlinemark = 'Target: DEC/'+rebootname+' installation succeeded'
        return

    def processLine(self, line):
        if self.beginlinemark in line:
            self.startLine=self.extracttime(line)
            self.startimeline_whole = line
            return
    # we are processing the end line
        if self.endlinemark in line:
            self.endLine = self.extracttime(line)
            duration = self.getDuration(self.startLine, self.endLine)
            #only append when we are sure we are getting a valid record
            self.startimelines.append(self.startLine)
            self.endtimelines.append(self.endLine)
            self.durations.append(duration)
            self.startimelines_whole.append(self.startimeline_whole )
            return
        return
    def getFinalResult(self,savefilepath):
        print self.rebootname + " statistics"
        tempDict = {'starTime' :  np.array(self.startimelines),
                'endTime' : np.array(self.endtimelines),
                'duration' : np.array(self.durations),
                'wholestartline' : np.array( self.startimelines_whole)}
        df =  pd.DataFrame(tempDict)
        print df.describe()
        df.to_csv(savefilepath + self.rebootname + ".csv")
        print "max duration record: " + str(df['duration'].idxmax())
        print df.loc[df['duration'].idxmax()][['duration','starTime','endTime']]
        return
    
    
    def extracttime(self, line):
        searchObj = re.search('^I, \[(.*)\.(.*)INFO -- ProductionScripts::Prc::Process::Packages::Install(.*)', line, re.M|re.I)
        return searchObj.group(1)
    def convertTime(self,line):
        date_object = datetime.strptime(line, '%Y-%m-%dT%H:%M:%S')
        return date_object
    def getDuration(self, lineStart, lineEnd):
        start = self.convertTime(lineStart)
        end = self.convertTime(lineEnd)
        return (end-start).total_seconds()


class rebootstatisticsProxy: 
    def __init__(self):
        self.ramkernel = rebootstatistics('RebootKernelRam')
        self.kernel = rebootstatistics('RebootKernel')
        
    def processLine(self,line):
        self.ramkernel.processLine(line)
        self.kernel.processLine(line)
        return
    def getFinalResult(self,savefilepath):
        self.ramkernel.getFinalResult(savefilepath)
        self.kernel.getFinalResult(savefilepath)
        obj = rebootVisualize.visualizedataProxy()
        obj.drawHist(savefilepath)

# test =  rebootstatistics('RebootKernelRam') 
# start = r'I, [2016-01-21T06:24:18.203720 #9160]  INFO -- ProductionScripts::Prc::Process::Packages::Install: event: [Info] => [DEC/RebootKernelRam] Begin installing target. Timeout value: 60[s]'
# end = r'I, [2016-01-21T06:25:05.344502 #9160]  INFO -- ProductionScripts::Prc::Process::Packages::Install: event: [Info] => SUCCESS: Target: DEC/RebootKernelRam installation succeeded'
# # print test.getDuration(start, end)
# # line1 = r'2016-01-21T07:30:11'
# # t1 = test. convertTime(line1)
# # line2 = r'2016-01-21T07:30:55'
# # t2= test. convertTime(line2)
# # d = test.getDuration(t1, t2)
# # print d
# test.processLine(start)
# test.processLine(end)
# test.getFinalResult()
