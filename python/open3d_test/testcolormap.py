"""
<!-- ******************************************
*  Author : Levin Jian  
*  Created On : Tue Dec 31 2024
*  File : testcolormap.py
******************************************* -->

"""
import open3d as o3d
from open3d.core import Tensor, concatenate
from open3d.visualization import rendering, draw
from open3d.ml.vis import Colormap

class App(object):
    def __init__(self):
        return
    def run(self):


        # Create a helix point cloud. We will use the Z values to assign colors.
        values = Tensor.arange(start=0.0, stop=1.0, step=0.001,
                            dtype=o3d.core.float32).reshape((-1, 1))
        period = 0.2
        xyz = concatenate(
            ((6.28 / period * values).sin(), (6.28 / period * values).cos(), values), 1)
        pcd = o3d.t.geometry.PointCloud(xyz)
        # Use a special point property to specify colormap lookup values for the point
        # cloud.
        pcd.point['__visualization_scalar'] = values
        # Use a default rainbow colormap
        colormap = Colormap.make_rainbow()
        # Add alpha channel and convert to Gradient Points
        colormap = list(
            rendering.Gradient.Point(pt.value, pt.color + [1.0])
            for pt in colormap.points)
        # Now create the material
        material = rendering.MaterialRecord()
        material.shader = "unlitGradient"
        material.gradient = rendering.Gradient(colormap)
        material.gradient.mode = rendering.Gradient.GRADIENT
        material.scalar_min = 0.0
        material.scalar_max = 1.0

        draw(
            {
            'name': 'helix',
            'geometry': pcd,
            'material': material
            },
            point_size=3,
            show_skybox=False)
        return 

if __name__ == "__main__":   
    obj= App()
    obj.run()
