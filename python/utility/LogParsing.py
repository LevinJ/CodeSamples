import os, os.path

from optparse import OptionParser


class LogParsing:
    def __init__(self):
        return
    def processLine(self, line):
        print line
        return
    def processFile(self):
        options = self.parse_arguments()
        filename = options.input_path
        self.filename = filename
        with open(filename) as f:
                for line in f:
                    self.processLine(line)
        return
    def processDone(self):
        pass
        
    def parse_arguments(self):
        
        parser = OptionParser()
        parser.description = "Parsing log file"
    
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
    def run(self):
        self.processFile()
        self.processDone()
        return
    
    




if __name__ == "__main__":   
    obj= LogParsing()
    obj.run()