import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# plt.plot([1,2,3,4])
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16],linewidth=2.0)
# plt.ylabel('some numbers')
# plt.show()
def transformData(global_loadinfoList):
    id_list = []
    cpu_list = []
    sda_cpu_list = []
    coord_cpu_list = []
    load_list = []
    mem_free_list = []
    canspy_cpu_list = []
    for item in global_loadinfoList:
        cpu_list.append(100-float(item['cpu']['idle']))
        mem_free_list.append(int(item['mem']['free'])/1024)
        id_list.append(item['id'])
        if 'process_sda' in item:
            sda_cpu_list.append(float(item['process_sda']['cpuper']))
        else:
            sda_cpu_list.append(0.0)
        if 'process_coord' in item:
            coord_cpu_list.append(float(item['process_coord']['cpuper']))
        else:
            coord_cpu_list.append(0.0)
        if 'process_CanSpy' in item:
            canspy_cpu_list.append(float(item['process_CanSpy']['cpuper']))
        else:
            canspy_cpu_list.append(0.0)
        load_list.append(float(item['loadvag']['1']))
    #generate the dictionary structure
    tempDict = { 'id_list' : np.array(id_list),
                'cpu_list' :  np.array(cpu_list),
                'sda_cpu_list' : np.array(sda_cpu_list),
                'coord_cpu_list' : np.array(coord_cpu_list),
                'canspy_cpu_list' : np.array(canspy_cpu_list),
                'load_list' : np.array(load_list),
                'mem_free_list' : np.array(mem_free_list)}
    return tempDict
        
def saveCSV(tempDict):
    df =  pd.DataFrame(tempDict)
    dispres = df[['cpu_list','sda_cpu_list','coord_cpu_list','canspy_cpu_list','load_list','mem_free_list']].describe()
    print dispres
    plt.figure(2)
    plt.text(0, 0.15, dispres)
    plt.savefig('summary.pdf')
    df.to_csv("loadinfo.csv")
#     df.to_csv("loadinfo.csv",header=True,cols=['id_list', 'cpu_list', 'sda_cpu_list', 'coord_cpu_list','load_list','mem_free_list'])
    return
            
def drawScatter(global_loadinfoList):
    tempDict = transformData(global_loadinfoList)
    saveCSV(tempDict)
 
    plt.figure(1)   
    ax=plt.subplot(311)
    ax.plot(tempDict['id_list'], tempDict['cpu_list'],label="CPU usage")
    ax.plot(tempDict['id_list'], tempDict['sda_cpu_list'],label="SDA CPU usage")
    ax.plot(tempDict['id_list'], tempDict['coord_cpu_list'], label="Coord CPU usage")
    ax.plot(tempDict['id_list'], tempDict['canspy_cpu_list'], label="Canspy CPU usage")
    plt.ylabel('cpu usage')
    plt.xlabel('Polling ID')
    ax.legend(loc='upper right', shadow=True)
    
    ax=plt.subplot(312)
    ax.plot(tempDict['id_list'], tempDict['load_list'],label="load status")
    idlength = tempDict['id_list'].shape[0]
    ax.plot(tempDict['id_list'], np.ones(idlength),label="Caution level")
    plt.ylabel('load percentage')
    plt.xlabel('Polling ID')
    ax.legend(loc='upper right', shadow=True)
    
    ax=plt.subplot(313)
    ax.plot(tempDict['id_list'], tempDict['mem_free_list'],label="Free memory amount")
    plt.ylabel('Memory status')
    plt.xlabel('Polling ID')
    ax.legend(loc='upper right', shadow=True)
    plt.savefig('loadtrend.pdf')
    plt.show()