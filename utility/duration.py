import datetime
import time
import dateutil.relativedelta

class Duration:
    def __init__(self):
        self.start()
        return
    def start(self):
#         print('start timer')
        self.startTime =  time.time()
        return
    def end(self, num_epoch = 1, num_iteration=1):
        self.endTime =  time.time()
        rd = self.endTime - self.startTime
#         print('end timer')
#         self.dispDuration(num_epoch, num_iteration)
        return rd
    def dispDuration(self, num_epoch, num_iteration):
        rd = self.endTime - self.startTime
        print("elapsed time={} seconds".format(rd))
#         logging.debug( "Duration: %d:%d:%d One epoch %f minutes, One iteration %f minutes" % (rd.hours, rd.minutes, rd.seconds, 
#                                                                                               (rd.hours *60.0 + rd.minutes + rd.seconds/60.0)/num_epoch,
#                                                                                               (rd.hours *60.0 + rd.minutes+ rd.seconds/60.0)/num_iteration))
#         logging.debug "Duration: %d years, %d months, %d days, %d hours, %d minutes and %d seconds" \
#         % (rd.years, rd.months, rd.days, rd.hours, rd.minutes, rd.seconds)
            
        
        return
    
if __name__ == "__main__":   
    obj= Duration()
    obj.start()
    time.sleep(0.001)
    print(obj.end())
    obj.end()