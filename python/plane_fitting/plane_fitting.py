import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from utility.poseinfo import PoseInfo
import cv2

class PlaneExtraction(object):
    def __init__(self) -> None:
        return 
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
        V = pca.components_ 

        xyz_mean = pcs.mean(axis = 0)
        x_pca_axis, y_pca_axis = V[0, :], V[1, :]
        z_pca_axis = np.cross(x_pca_axis, y_pca_axis)



        #plane center to world frame
        R = np.array([x_pca_axis, y_pca_axis, z_pca_axis])
        R = R.T
        t = xyz_mean
        Twp = PoseInfo().construct_fromRt(R, t)
        proj_world_points, plane_points = self.check_plane_projection(pcs, Twp)

        return Twp, x_pca_axis, y_pca_axis, z_pca_axis, xyz_mean, proj_world_points, plane_points
    def extract_bdbox(self, Twp, plane_points):
        plane_points = plane_points[:, :2].astype(np.float32)
        use_cv2 = False
        box = []
        if not use_cv2:
            minx, maxx = plane_points[:, 0].min(), plane_points[:, 0].max()
            miny, maxy = plane_points[:, 1].min(), plane_points[:, 1].max()
        
            box.append([minx, miny])
            box.append([maxx, miny])
            box.append([maxx, maxy])
            box.append([minx, maxy])
        else:
            rect = cv2.minAreaRect(plane_points)
            box = cv2.boxPoints(rect)
        
        box = np.concatenate([box, np.zeros((len(box), 1))], axis = 1)
        box = np.concatenate([box, np.ones((len(box), 1))], axis = 1)

        proj_box = box.dot(Twp.T.T)[:, :3]
        return proj_box
    

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
    def gen_rect2(self):
        res = []
        res.append([-1, 0, 0])
        res.append([-1, 5, 0])
        res.append([-1, 10, 0.1])
        res.append([-2, 10, 0])
        res.append([0, 13, 0])
        res.append([2, 10, 0])
        res.append([1, 10, -0.01])
        res.append([1, 5, 0])
        res.append([1, 0, 0])
        return np.array(res)
    def transform_pnts(self, pnts, ypr = [20, 60, 130], t = [10, -10, 20]):
        Twb = PoseInfo().construct_fromyprt(ypr, t)
        xyzs = np.concatenate([pnts, np.ones((len(pnts), 1))], axis = 1)
        world_points = xyzs.dot(Twb.T.T)[:, :3]
        return world_points
    def draw_boundary(self, ax, pcs, connect = True, color = 'black'):
        pcs = np.append(pcs, [pcs[0, :]], axis=0)
        ax.plot(pcs[:, 0], pcs[:, 1], pcs[:, 2],   color = color, alpha=0.4)
        return
    
    def run(self):
        pcs = self.gen_rect2()
        ypr = [-45, 5, -5]
        t = [10, 20, -40]
        print("prev = {}".format(pcs))
        pcs = self.transform_pnts(pcs, ypr = ypr, t = t)
        print("after = {}".format(pcs))

        fig = plt.figure()
        plt.clf()
        ax = fig.add_subplot(111, projection="3d")

        self.draw_boundary(ax, pcs, connect = True, color = 'black')

        pe = PlaneExtraction()
        Twp, x_pca_axis, y_pca_axis, z_pca_axis, xyz_mean, proj_world_points, plane_points = pe.proj_pnts(pcs)
        self.draw_axis(ax, x_pca_axis, y_pca_axis, z_pca_axis, translate=xyz_mean)
        proj_box = pe.extract_bdbox(Twp, plane_points)

        self.draw_boundary(ax, proj_box, connect = True, color = 'red')

        # ax.plot(proj_world_points[:, 0], proj_world_points[:, 1], proj_world_points[:, 2],   alpha=0.4)

        

        self.set_aspect_equal_3d(ax)
        plt.show()
        return
    

if __name__ == "__main__":   
    obj= App()
    obj.run()
    
