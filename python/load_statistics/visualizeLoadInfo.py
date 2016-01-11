import matplotlib.pyplot as plt
import numpy as np


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
        load_list.append(float(item['loadvag']['1']))
    return np.array(id_list), np.array(cpu_list),np.array(sda_cpu_list),np.array(coord_cpu_list),np.array(load_list),np.array(mem_free_list)
        
        
def drawScatter(global_loadinfoList):
    id_list, cpu_list,sda_cpu_list, coord_cpu_list,load_list,mem_free_list = transformData(global_loadinfoList)
 
    plt.figure(1)   
    ax=plt.subplot(311)
    ax.plot(id_list, cpu_list,label="CPU usage")
    ax.plot(id_list, sda_cpu_list,label="SDA CPU usage")
    ax.plot(id_list, coord_cpu_list, label="Coord CPU usage")
    plt.ylabel('cpu usage')
    plt.xlabel('Polling ID')
    ax.legend(loc='upper right', shadow=True)
    
    ax=plt.subplot(312)
    ax.plot(id_list, load_list,label="load status")
    plt.ylabel('load percentage')
    plt.xlabel('Polling ID')
    ax.legend(loc='upper right', shadow=True)
    
    ax=plt.subplot(313)
    ax.plot(id_list, mem_free_list,label="Free memory amount")
    plt.ylabel('Memory status')
    plt.xlabel('Polling ID')
    ax.legend(loc='upper right', shadow=True)
    plt.show()