import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import matplotlib.mlab as mlab


class visualizedataProxy:
    
    def drawHist(self):
        plt.figure()  
        plt.subplot(211) 
        self.pltsubPlot('RebootKernelRam.csv')
        
        
        plt.subplot(212)
        self.pltsubPlot('RebootKernel.csv')
        plt.show()
        return
    def pltsubPlot(self, filename):
        df = pd.read_csv(filename)
        n, bins, patches = plt.hist(df['duration'], 15, normed=1, facecolor='green', alpha=0.75)
        # add a 'best fit' line
        mu = df['duration'].mean()
        sigma = df['duration'].std()
        y = mlab.normpdf( bins, mu, sigma)
        l = plt.plot(bins, y, 'r--', linewidth=1)   
        plt.xlabel('Duration')
        plt.ylabel('Frequency')
        plt.title(filename)
        plt.xlim([30,70])
        return
    
    


if __name__ == "__main__":
    obj = visualizedataProxy()
#     obj.drawHist('RebootKernel.csv')
    obj.drawHist()