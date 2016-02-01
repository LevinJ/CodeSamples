import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class visualizedataProxy:
    def __init__(self):
        self.df = pd.read_csv('data.csv')
        return
    
    def drawLines(self):
        plt.figure(1)   
#         ax=plt.subplot(111)
        plt.plot(self.df['loopid'], self.df['orbDuration'],label="orbDuration")
        plt.plot(self.df['loopid'], self.df['noteProcDuration'],label="noteProcDuration")
        plt.legend(loc='upper right', shadow=True)
        plt.ylabel('Time duration')
        plt.xlabel('Looping  ID')
        plt.show()
        return
    
    


if __name__ == "__main__":
    obj = visualizedataProxy()
    obj.drawLines()