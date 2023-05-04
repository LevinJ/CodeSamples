import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from utility.poseinfo import PoseInfo

class App(object):
    def __init__(self) -> None:
        pass
    def draw_line(self, ax, pnt1, pnt2, text = "", color="red"):
        xs = []
        ys = []
        zs = []    
        for pnt in [pnt1, pnt2]:
            x,y, z = pnt 
            xs.append(x)
            ys.append(y)
            zs.append(z)
        ax.plot(xs, ys, zs,color=color)
        x, y, z = np.array(xs).mean(), np.array(ys).mean(),np.array(zs).mean()
        s = text
        ax.text(x, y, z, s)
        return
    def draw_axis(self, ax, px, py, pz, translate = None):
        po = [0,0,0]
        if translate is not None:
            po = np.array([0,0,0]) + np.array(translate) 
            px = np.array(px) + np.array(translate) 
            py = np.array(py) + np.array(translate) 
            pz = np.array(pz) + np.array(translate) 
        self.draw_line(ax, po, px, text = "x",color="red")
        self.draw_line(ax, po, py, text = "y",color="green")
        self.draw_line(ax, po, pz, text = "z",color="blue")  
        return
    def set_aspect_equal_3d(self, ax):
        """Fix equal aspect bug for 3D plots."""
    
        xlim = ax.get_xlim3d()
        ylim = ax.get_ylim3d()
        zlim = ax.get_zlim3d()
    
        from numpy import mean
        xmean = mean(xlim)
        ymean = mean(ylim)
        zmean = mean(zlim)
    
        plot_radius = max([abs(lim - mean_)
                           for lims, mean_ in ((xlim, xmean),
                                               (ylim, ymean),
                                               (zlim, zmean))
                           for lim in lims])
    
        ax.set_xlim3d([xmean - plot_radius, xmean + plot_radius])
        ax.set_ylim3d([ymean - plot_radius, ymean + plot_radius])
        ax.set_zlim3d([zmean - plot_radius, zmean + plot_radius])
    def gen_rect(self):
        res = []
        res.append([-1, 0, 0])
        res.append([-1, 5, 0.2])
        res.append([-1, 10, 0])
        res.append([1, 10, 0])
        res.append([1, 5, -0.1])
        res.append([1, 0, 0])
        return np.array(res)
    def transform_pnts(self, pnts, ypr = [20, 60, 130], t = [10, -10, 20]):
        Twb = PoseInfo().construct_fromyprt(ypr, t)
        xyzs = np.concatenate([pnts, np.ones((len(pnts), 1))], axis = 1)
        world_points = xyzs.dot(Twb.T.T)[:, :3]
        return world_points
    def check_plane_projection(self, pnts, Twp):
        xyzs = np.concatenate([pnts, np.ones((len(pnts), 1))], axis = 1)
        plane_points = xyzs.dot(Twp.I.T.T)[:, :3]
        print("prj pnts = {}".format(plane_points))

        proj_plane_points = plane_points.copy()
        proj_plane_points[:, 2] = 0
        proj_plane_points = np.concatenate([proj_plane_points, np.ones((len(proj_plane_points), 1))], axis = 1)
        proj_world_points = proj_plane_points.dot(Twp.T.T)[:, :3]
        return  proj_world_points, proj_plane_points[:, :3]
    def proj_pnts(self, pcs):
        Y = pcs
        pca = PCA(n_components=3)
        pca.fit(Y)
        V = pca.components_ * 3

        xyz_mean = pcs.mean(axis = 0)
        x_pca_axis, y_pca_axis, z_pca_axis = V[0, :], V[1, :], V[2, :]


        #plane center to world frame
        R = pca.components_.T
        t = xyz_mean
        Twp = PoseInfo().construct_fromRt(R, t)
        proj_world_points, plane_points = self.check_plane_projection(pcs, Twp)

        return x_pca_axis, y_pca_axis, z_pca_axis, xyz_mean, proj_world_points, plane_points
    def run(self):
        pcs = self.gen_rect()
        ypr = [40, 0, -0]
        t = [2, 10, -50]
        print("prev = {}".format(pcs))
        pcs = self.transform_pnts(pcs, ypr = ypr, t = t)
        print("after = {}".format(pcs))

        fig = plt.figure()
        plt.clf()
        ax = fig.add_subplot(111, projection="3d")
        ax.plot(pcs[:, 0], pcs[:, 1], pcs[:, 2],   alpha=0.4)

        x_pca_axis, y_pca_axis, z_pca_axis, xyz_mean, proj_world_points, plane_points = self.proj_pnts(pcs)

        ax.plot(proj_world_points[:, 0], proj_world_points[:, 1], proj_world_points[:, 2],   alpha=0.4)

        self.draw_axis(ax, x_pca_axis, y_pca_axis, z_pca_axis, translate=xyz_mean)

        self.set_aspect_equal_3d(ax)
        plt.show()
        return
    

if __name__ == "__main__":   
    obj= App()
    obj.run()
    
