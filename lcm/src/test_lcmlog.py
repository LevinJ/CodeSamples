import time

import lcm
from exlcm import example_t


class TestLcmLog(object):
    def __init__(self):
        self.mode = "r"

        self.lc = lcm.LCM("file:///home/levin/workspace/codesamples/lcm/src/data/logfile?mode={}&speed=15".format(self.mode))
        return
    def run(self):
        if self.mode == "w":
            self.send()
        else:
            self.recv()
        return
    def my_handler(self, channel, data):
        msg = example_t.decode(data)
        print("Received message on channel \"%s\"" % channel)
        print("   timestamp   = %s" % str(msg.timestamp))
        print("   position    = %s" % str(msg.position))
        print("   orientation = %s" % str(msg.orientation))
        print("   ranges: %s" % str(msg.ranges))
        print("   name        = '%s'" % msg.name)
        print("   enabled     = %s" % str(msg.enabled))
        print("")
        return
    
    def send(self):
        msg = example_t()
        msg.timestamp = 0
        msg.position = (1, 2, 3)
        msg.orientation = (1, 0, 0, 0)
        msg.ranges = range(15)
        msg.num_ranges = len(msg.ranges)
        msg.name = "example string"
        msg.enabled = True
        
        
        for ind in range(10):
            msg.timestamp = ind
            self.lc.publish("EXAMPLE", msg.encode())
            time.sleep(0.5)
            print("message written")
        return
    def recv(self):
        subscription = self.lc.subscribe("EXAMPLE", self.my_handler)
        try:
            while True:
                self.lc.handle()
        except KeyboardInterrupt:
            pass
        
        
        return
    
if __name__ == "__main__":
    obj = TestLcmLog()
    obj.run()