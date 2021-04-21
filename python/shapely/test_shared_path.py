from shapely.ops import shared_paths
from shapely.geometry import Polygon, LineString, Point, MultiPoint


from shapely.geometry import LineString, MultiPoint
from shapely.ops import split
import numpy as np
from mock.mock import self

# line = LineString([(0, 0), (5, 0), (10, 0)])
# seg_len = 0.25
# splitter = [line.interpolate(i, normalized=False) for i in np.arange(seg_len, line.length, seg_len)]
# spillter = []
# spillter.extend([ (pnt.x, pnt.y) for pnt in splitter])
# print(splitter)

class UtilLine(object):
    def __init__(self):
        return
    def get_cloest_points(self, coords, pnt, k=2):
        return

def segment_line(coords, seg_len):
    line = LineString(coords)
    res = [line.interpolate(i, normalized=False) for i in np.arange(seg_len, line.length, seg_len)]
    res = [ (pnt.x, pnt.y) for pnt in res]
    res.insert(0, coords[0])
    res.append(coords[-1])
    return res

coords = [(0, 0), (5, 0), (10, 0)]
seg_len = 0.25
res = segment_line(coords, seg_len)
print(res)
# point = Point(1, 1)
#
# line = LineString([(0, 0), (5, 0), (5, 3)])
#
# res = line.project(point, normalized=False)
#
#
# res = point.distance(line)
# print(res)
