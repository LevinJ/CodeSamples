import time

import lcm
from exlcm import example_t
import numpy as np
from exlcm import point2d_list_t
import traceback
from  enginetargetlanes_pb2 import EngineTargetLanes


class TestLcmLog(object):
    def __init__(self):
        self.mode = "r"

        self.lc = lcm.LCM("file:///media/levin/DATADRIVE1/mapmatch/2019_11_01_17_05_27.log?mode={}&speed=15".format(self.mode))
        
        self.map_obj = EngineTargetLanes()
        self.channel_handler_list = []
        self.channel_handler_list.append(("PROTO_EngineTargetLanes", self.map_obj))
        return
    def run(self):
        if self.mode == "w":
            self.send()
        else:
            self.recv()
        return
    def lcm_handler(self, channel, data):
        print("channel = {}".format(channel))
        for sub, proto_obj in self.channel_handler_list:
            if sub != channel:
                continue
            proto_obj.ParseFromString(data)
            
        return
    
    
    def recv(self):

        for sub, _proto_obj in self.channel_handler_list:
            self.lc.subscribe(sub, self.lcm_handler)

        try:
            while True:
                self.lc.handle()
        except Exception as e:
            print("{}, {}".format(e, traceback.format_exc()))
            pass
        
        
        return
    
if __name__ == "__main__":
    obj = TestLcmLog()
    obj.run()