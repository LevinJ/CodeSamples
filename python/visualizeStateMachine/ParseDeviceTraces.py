from parseDECTraces import ParseDecTraces
from buildsatemachine import BuildSateMachine
import re
import sys



class ParseDeviceTraces(ParseDecTraces):
    def __init__(self, buildsstatemachine):
        ParseDecTraces.__init__( self,buildsstatemachine)
        return
    def processEntry(self, line):
        m = re.search(r'(.*)entry state= (.*)', line)
        if not m:
            raise Exception("invalid line {}".format(line))
        return 'entry',   m.group(2).replace('/','.'), None
    
    def processExit(self, line):
        m = re.search(r'(.*)exit state= (.*)', line)
        if not m:
            raise Exception("invalid line {}".format(line))
        return 'exit',   m.group(2).replace('/','.'), None
#     def run(self):
#         line = 'i=985   t=1703.791672s  n=nhc   s=states        v=entry state= flushDispatcher'
#         print self.processEntry(line)
#         line = 'i=990   t=1703.831672s  n=nhc   s=states        v=exit state= stopTransport'
#         print self.processExit(line)
#         return
    
    
    



if __name__ == "__main__":   
    obj= ParseDeviceTraces(BuildSateMachine())
    obj.run()