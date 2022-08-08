import open3d as o3d
# import open3d.visualization as vis
from poseinfo import PoseInfo 
import numpy as np

print("Let's draw a box using o3d.geometry.LineSet.")

# lines = [
#     [0, 1],
#     [0, 2],
#     [1, 3],
#     [2, 3],
#     [4, 5],
#     [4, 6],
#     [5, 7],
#     [6, 7],
#     [0, 4],
#     [1, 5],
#     [2, 6],
#     [3, 7],
# ]


class Polygons(object):
    def __init__(self,pg, Tvo):
        self.polygongs = pg
        self.Tvo = Tvo
        return
#
# class Pillars(object):
#     def __init__(self, xyz, ):
#         return

class Dashed_Lane(Polygons):
    def __init__(self,pg, Tvo):
        Polygons.__init__(self, pg, Tvo)
        return
    @classmethod
    def gen_lane_seg_polygon(self, y_start, y_end, lane_width):
        half_lane_width = lane_width/2.0
        p1 = [half_lane_width, y_start, 0]
        p2 = [half_lane_width, y_end, 0]
        p3 = [-half_lane_width, y_end, 0]
        p4 = [-half_lane_width, y_start, 0]
        return [p1, p2, p3,p4]
    @classmethod
    def from_spec(cls, name, lane_len, Tvo):
        lane_seg_len = 4 
        lane_width = 0.2
        lane_seg_gap = 1
        
        y_start = 0
        
        pgs = []
        while y_start < lane_len:
            y_end = y_start + lane_seg_len
            if y_end > lane_len:
                y_end = lane_len 
            pgs.append(Dashed_Lane.gen_lane_seg_polygon(y_start, y_end, lane_width))
            #preparee for next cycle
            y_start = y_end + lane_seg_gap
        obj = cls(pgs, Tvo) 
        obj.name = name
        return obj
class ForwardArraow(object):
    def __init__(self, pg, Tvo):
        Polygons.__init__(self, pg, Tvo)
        return





def draw_polygon(points, colors, T ):
    line_indices = [[i, i + 1] for i in range(0, len(points))]
    line_indices[-1][-1] = 0
    # line_indices = [[0,1],[1,2],[2, 0]]
    line_set = o3d.geometry.LineSet(
    points=o3d.utility.Vector3dVector(points),
    lines=o3d.utility.Vector2iVector(line_indices))
    line_set.colors = o3d.utility.Vector3dVector(colors)
    line_set.transform(T)
    return line_set
def draw_polygon_list(points_list, colors, T ):
    res = []
    for points in points_list:
        res.append(draw_polygon(points, colors, T ))
    return res

def draw_bd(x, y, z, colors, T):
    
    mesh_box = o3d.geometry.TriangleMesh.create_box(width=x,
                                                height=y,
                                                depth=z)
    # mesh_box.compute_vertex_normals()
    mesh_box.paint_uniform_color(colors)
    mesh_box.translate(np.array([-x/2.0, -y/2.0, 0]))
    mesh_box.transform(T)
    return mesh_box

# lane1 = Dashed_Lane([points], T)
gemotry_list = []
lane_len = 100
lane_colors = [[0, 0, 1] for i in np.arange(4)]

T = PoseInfo().construct_fromyprt([0, 0, 0], [1, 0, 0])
lane1 = Dashed_Lane.from_spec("lane1", lane_len, T)
line_set = draw_polygon_list(lane1.polygongs, lane_colors, T.T)
gemotry_list.extend(line_set)

T = PoseInfo().construct_fromyprt([0, 0, 0], [-1, 0, 0])
lane2 = Dashed_Lane.from_spec("lane1", lane_len, T)
line_set = draw_polygon_list(lane1.polygongs, lane_colors, T.T)
gemotry_list.extend(line_set)

# mesh_box = o3d.geometry.TriangleMesh.create_box(width=0.6,
#                                                 height=3.0,
#                                                 depth=0.6)
# mesh_box.compute_vertex_normals()
# mesh_box.paint_uniform_color([0.9, 0.1, 0.1])
width=0.6
height=0.6
depth= 3

T = PoseInfo().construct_fromyprt([0, 0, 0], [1.5, 5, 0])
mesh_box = draw_bd(width, height, depth, [0.9, 0.1, 0.1], T.T)
gemotry_list.append(mesh_box)

T = PoseInfo().construct_fromyprt([0, 0, 0], [-1.5, 5, 0])
mesh_box = draw_bd(width, height, depth, [0.9, 0.1, 0.1], T.T)
gemotry_list.append(mesh_box)


orig = o3d.geometry.TriangleMesh.create_coordinate_frame()

gemotry_list.append(orig)

vis = o3d.visualization.Visualizer()
vis.create_window()

for gs in gemotry_list:
    if isinstance(gs, list):
        for g in gs:
            vis.add_geometry(g)
    else:
        vis.add_geometry(gs)

filename = "viewpoint.json"
ctr = vis.get_view_control()
param = o3d.io.read_pinhole_camera_parameters(filename)
# param.extrinsic = np.array([[1, 0, 0, 0],[0, -1, 0, 0],[0, 0, -1, 20],[0, 0, 0, 1]])
ctr.convert_from_pinhole_camera_parameters(param)
    
    
vis.run()
# param = vis.get_view_control().convert_to_pinhole_camera_parameters()
# o3d.io.write_pinhole_camera_parameters(filename, param)
vis.destroy_window()
    
# vis.draw([mesh, mesh_box, line_set])



