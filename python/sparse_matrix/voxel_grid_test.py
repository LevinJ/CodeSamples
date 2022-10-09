import numpy as np
import laspy as lp
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from utility.duration import Duration

class TestVoxel(object):
    def __init__(self):
        return
    def grid_subsampling(self, points, voxel_size):
        tk = Duration()
        nb_vox=np.ceil((np.max(points, axis=0) - np.min(points, axis=0))/voxel_size)
        non_empty_voxel_keys, inverse, nb_pts_per_voxel= np.unique(((points - np.min(points, axis=0)) // voxel_size).astype(int), axis=0, return_inverse=True, return_counts=True)
        idx_pts_vox_sorted=np.argsort(inverse)
        voxel_grid={}
        grid_barycenter,grid_candidate_center=[],[]
        last_seen=0
        print("voxel grid {:.3f}, {}".format(tk.end(), len(points)))

        tk.start()    
        for idx,vox in enumerate(non_empty_voxel_keys):
            voxel_grid[tuple(vox)]=points[idx_pts_vox_sorted[last_seen:last_seen+nb_pts_per_voxel[idx]]]
            grid_barycenter.append(np.mean(voxel_grid[tuple(vox)],axis=0))
            grid_candidate_center.append(voxel_grid[tuple(vox)][np.linalg.norm(voxel_grid[tuple(vox)]-np.mean(voxel_grid[tuple(vox)],axis=0),axis=1).argmin()])
            last_seen+=nb_pts_per_voxel[idx]
        print("process cell {:.3f}, {}".format(tk.end(), len(non_empty_voxel_keys)))    
        return grid_candidate_center
    def load_data2(self):
        input_path="/home/levin/temp/1008/3DML_urban_point_cloud.xyz"
        # data = np.loadtxt(input_path, skiprows=1)
        point_cloud = pd.read_csv(input_path, sep=' ')
        
        #point cloud decimation
        points = np.vstack((point_cloud.X, point_cloud.Y, point_cloud.Z)).transpose()
        colors = np.vstack((point_cloud.R, point_cloud.G, point_cloud.B)).transpose()
        return points, colors
    def load_data(self):
        input_path="/home/levin/temp/1008/NZ19_Wellington.las"
        point_cloud=lp.file.File(input_path, mode="r")
        
        points = np.vstack((point_cloud.x, point_cloud.y, point_cloud.z)).transpose()
        colors = np.vstack((point_cloud.red, point_cloud.green, point_cloud.blue)).transpose()
        return points, colors
    def decimate_subsmapling(self):
        points, colors = self.load_data()
        factor=160
        decimated_points = points[::factor]
        #decimated_colors = colors[::factor]
        res = len(decimated_points)
        print(res)
        
        decimated_colors = colors[::factor]
        ax = plt.axes(projection='3d')
        ax.scatter(decimated_points[:,0], decimated_points[:,1], decimated_points[:,2], 
                   c = decimated_colors/65535, s=0.01)
        plt.show()
        return
    def run(self):
        # return self.decimate_subsmapling()
        points, _colors = self.load_data()
        grid_sampled_point_cloud = self.grid_subsampling(points, 6)
        return 
    
if __name__ == "__main__":   
    obj= TestVoxel()
    obj.run()

