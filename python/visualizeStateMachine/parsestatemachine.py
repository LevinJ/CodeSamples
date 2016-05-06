
from python.utility.LogParsing import LogParsing
from buildsatemachine import BuildSateMachine
import re

class ParseStateMachine(LogParsing):
    def __init__(self, buildsstatemachine):
        self.startProcess = False
        self.buildsstatemachine = buildsstatemachine
        return
    def processDone(self):
        self.buildsstatemachine.saveOutput()
        return
    def processLine(self, line):
        if (not self.startProcess):
            if (not 'entry state' in line):
                return
        if ('entry state=' in line):
            self.startProcess = True
            self.buildsstatemachine.buildMachineinXML(*self.processEntry(line))
            return
        if ('exit state=' in line):
            self.buildsstatemachine.buildMachineinXML(*self.processExit(line))
            return
        return
#     def run(self):
#         line = '16:34:35.487.0,Fsm,,DepositFsm,INFO1,L0103 TID0 6712 entry state= TerminateData  '
#         print self.processEntry(line)
#         line = '16:34:33.309.0,Fsm,,DepositFsm,INFO1,L0209 TID0 6644 exit state= WaitForClean/PollWithPauses/Poll 16:36:20.723 '
#         print self.processExit(line)
#         return
    def processEntry(self, line):
        m = re.search(r'(.*),,(.*),INFO1(.*)entry state= ([a-zA-Z0-9\/]*)(.*)', line)
        if not m:
            raise Exception("invalid line {}".format(line))
        return 'entry',   m.group(4).replace('/','.'), m.group(2)
    
    def processExit(self, line):
        m = re.search(r'(.*),,(.*),INFO1(.*)exit state= ([a-zA-Z0-9\/]*)(.*)', line)
        if not m:
            raise Exception("invalid line {}".format(line))
        return 'exit',   m.group(4).replace('/','.'), m.group(2)
    
    
    
if __name__ == "__main__":   
    obj= ParseStateMachine(BuildSateMachine())
    obj.run()