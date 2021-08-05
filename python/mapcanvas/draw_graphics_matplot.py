from matplotlib.path import Path
from matplotlib.patches import PathPatch
from matplotlib import pyplot as plt

fig, ax = plt.subplots()

# Define drawing instructions and control point coordinates
path_data = [
         (Path.MOVETO, (0, 1)), # The starting point of the drawing. From here, 4 points behind control a 3rd-degree Bezier curve
    (Path.CURVE4, (-1, 1)),
    (Path.CURVE4, (-2, 3)),
    (Path.CURVE4, (-1, 2)),
         (Path.LINETO, (0, 2)), # draw a straight line. From here, 3 points behind control a 2nd order Bezier curve
    (Path.CURVE3, (1, 2)),
    (Path.CURVE3, (2, 3)),
         (Path.CLOSEPOLY, (0, 1)) # The last point, finish drawing. Let it be equal to the first point, which is closed, to form a figure
]

# Sequence unpacking and zip reorganization, put instructions together, put coordinates together (get two tuples)
codes, verts = zip(*path_data) # The equal sign here is also a sequence unpacking, and [(), ()] is solved into two ()

# Create Path objects based on vertices and instructions
path = Path(verts, codes)
# Create a graphic object based on the Path object
path_patch = PathPatch(path, facecolor='g', alpha=0.8)
# Add this graphic to the image
ax.add_patch(path_patch)

# Draw control points and lines
x, y = zip(*verts)
line, = ax.plot(x, y,'bo-') # blue, dot, straight line

ax.grid()

ax.axis('equal') # coordinate axis scales are equal in size

plt.plot()
plt.show()