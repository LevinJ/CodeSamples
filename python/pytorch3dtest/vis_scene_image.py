"""
<!-- ******************************************
*  Author : Levin Jian  
*  Created On : Tue Jun 11 2024
*  File : vis_scene_image.py
******************************************* -->

"""


import os
import sys
import torch
need_pytorch3d=False
try:
    import pytorch3d
except ModuleNotFoundError:
    need_pytorch3d=True
if need_pytorch3d:
    if torch.__version__.startswith("2.2.") and sys.platform.startswith("linux"):
        # We try to install PyTorch3D via a released wheel.
        pyt_version_str=torch.__version__.split("+")[0].replace(".", "")
        version_str="".join([
            f"py3{sys.version_info.minor}_cu",
            torch.version.cuda.replace(".",""),
            f"_pyt{pyt_version_str}"
        ])
        get_ipython().system('pip install fvcore iopath')
        get_ipython().system('pip install --no-index --no-cache-dir pytorch3d -f https://dl.fbaipublicfiles.com/pytorch3d/packaging/wheels/{version_str}/download.html')
    else:
        # We try to install PyTorch3D from source.
        get_ipython().system("pip install 'git+https://github.com/facebookresearch/pytorch3d.git@stable'")


# In[ ]:


import os
import torch
import matplotlib.pyplot as plt

# Util function for loading meshes
from pytorch3d.io import load_objs_as_meshes, load_obj

# Data structures and functions for rendering
from pytorch3d.structures import Meshes
from pytorch3d.vis.plotly_vis import AxisArgs, plot_batch_individually, plot_scene
from pytorch3d.vis.texture_vis import texturesuv_image_matplotlib
from pytorch3d.renderer import (
    look_at_view_transform,
    FoVPerspectiveCameras, 
    PointLights, 
    DirectionalLights, 
    Materials, 
    RasterizationSettings, 
    MeshRenderer, 
    MeshRasterizer,  
    SoftPhongShader,
    TexturesUV,
    TexturesVertex
)

# add path for demo utils functions 
import sys
import os
sys.path.append(os.path.abspath(''))


# If using **Google Colab**, fetch the utils file for plotting image grids:

# In[ ]:


# get_ipython().system('wget https://raw.githubusercontent.com/facebookresearch/pytorch3d/main/docs/tutorials/utils/plot_image_grid.py')
from plot_image_grid import image_grid


# OR if running **locally** uncomment and run the following cell:

# In[ ]:


# from utils import image_grid


# ### 1. Load a mesh and texture file
# 
# Load an `.obj` file and its associated `.mtl` file and create a **Textures** and **Meshes** object. 
# 
# **Meshes** is a unique datastructure provided in PyTorch3D for working with batches of meshes of different sizes. 
# 
# **TexturesUV** is an auxiliary datastructure for storing vertex uv and texture maps for meshes. 
# 
# **Meshes** has several class methods which are used throughout the rendering pipeline.

# If running this notebook using **Google Colab**, run the following cell to fetch the mesh obj and texture files and save it at the path `data/cow_mesh`:
# If running locally, the data is already available at the correct path. 

# In[ ]:


# get_ipython().system('mkdir -p data/cow_mesh')
# get_ipython().system('wget -P data/cow_mesh https://dl.fbaipublicfiles.com/pytorch3d/data/cow_mesh/cow.obj')
# get_ipython().system('wget -P data/cow_mesh https://dl.fbaipublicfiles.com/pytorch3d/data/cow_mesh/cow.mtl')
# get_ipython().system('wget -P data/cow_mesh https://dl.fbaipublicfiles.com/pytorch3d/data/cow_mesh/cow_texture.png')


# In[ ]:




class App(object):
    def __init__(self):
        return
    def run(self):
        # Setup
        if torch.cuda.is_available():
            device = torch.device("cuda:0")
            torch.cuda.set_device(device)
        else:
            device = torch.device("cpu")

        # Set paths
        DATA_DIR = "./data"
        obj_filename = os.path.join(DATA_DIR, "cow_mesh/cow.obj")


        verts, faces_idx, _ = load_obj(obj_filename)
        faces = faces_idx.verts_idx

        # Initialize each vertex to be white in color.
        verts_rgb = torch.ones_like(verts)[None]  # (1, V, 3)
        textures = TexturesVertex(verts_features=verts_rgb.to(device))

        # Create a Meshes object
        mesh = Meshes(
            verts=[verts.to(device)],   
            faces=[faces.to(device)],
            textures=textures
        )
        R, T = look_at_view_transform(2.7, 0, [0, 180]) # 2 camera angles, front and back
        # Any instance of CamerasBase works, here we use FoVPerspectiveCameras
        cameras = FoVPerspectiveCameras(device=device, R=R, T=T)

        # Define the settings for rasterization and shading. Here we set the output image to be of size
        # 512x512. As we are rendering images for visualization purposes only we will set faces_per_pixel=1
        # and blur_radius=0.0. We also set bin_size and max_faces_per_bin to None which ensure that 
        # the faster coarse-to-fine rasterization method is used. Refer to rasterize_meshes.py for 
        # explanations of these parameters. Refer to docs/notes/renderer.md for an explanation of 
        # the difference between naive and coarse-to-fine rasterization. 
        raster_settings = RasterizationSettings(
            image_size=512, 
            blur_radius=0.0, 
            faces_per_pixel=1, 
        )

        lights = PointLights(device=device, location=[[0.0, 0.0, -3.0]])

        # # In[ ]:




        # Create a Phong renderer by composing a rasterizer and a shader. The textured Phong shader will 
        # interpolate the texture uv coordinates for each vertex, sample from a texture image and 
        # apply the Phong lighting model
        renderer = MeshRenderer(
            rasterizer=MeshRasterizer(
                cameras=cameras, 
                raster_settings=raster_settings
            ),
            shader=SoftPhongShader(
                device=device, 
                cameras=cameras,
                lights=lights
            )
        )


        # Place a point light in front of the object. As mentioned above, the front of the cow is facing the 
        # -z direction. 

        meshes = mesh.extend(2)

        images = renderer(meshes, cameras=cameras, lights=lights)
        image_grid(images.cpu().numpy(), rows=4, cols=5, rgb=True)

        # Render the plotly figure
        fig = plot_scene({
            "subplot1": {
                "cow_mesh": mesh,
                "cameras_trace_title": cameras,
            }
        })
        fig.show()

        plt.show()

        return 

if __name__ == "__main__":   
    obj= App()
    obj.run()
