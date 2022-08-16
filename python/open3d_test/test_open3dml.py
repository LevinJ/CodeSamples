import open3d.ml.torch as ml3d  # or open3d.ml.tf as ml3d
from vis import Visualizer



# construct a dataset by specifying dataset_path
dataset = ml3d.datasets.NuScenes(dataset_path='/home/levin/workspace/data/temp/nuscenes/v1.0-mini')

# get the 'all' split that combines training, validation and test set
all_split = dataset.get_split('train')

# print the attributes of the first datum
print(all_split.get_attr(0))

# print the shape of the first point cloud
print(all_split.get_data(0)['point'].shape)

# show the first 100 frames using the visualizer
vis = Visualizer()
vis.visualize_dataset(dataset, 'train', indices=range(10))