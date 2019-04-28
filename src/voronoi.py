
from scipy.spatial import Delaunay, delaunay_plot_2d, Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt
import numpy as np

w = h = 360

n = 6
np.random.seed(0)
pts = np.random.randint(0, w, (n, 2))

print(pts)

print(type(pts))
# <class 'numpy.ndarray'>

print(pts.shape)
# (6, 2)

tri = Delaunay(pts)

print(type(tri))
# <class 'scipy.spatial.qhull.Delaunay'>

#fig = delaunay_plot_2d(tri)
#fig.savefig('scipy_matplotlib_delaunay.png')


vor = Voronoi(pts)

print(type(vor))
# <class 'scipy.spatial.qhull.Voronoi'>

#fig = voronoi_plot_2d(vor)
#fig.savefig('scipy_matplotlib_voronoi.png')

fig, ax = plt.subplots(figsize=(4, 4))
delaunay_plot_2d(tri, ax)
voronoi_plot_2d(vor, ax, show_vertices=False)
#voronoi_plot_2d(vor, ax)

for region, c in zip([r for r in vor.regions if -1 not in r and r], ['yellow', 'pink']):
    ax.fill(vor.vertices[region][:, 0],
            vor.vertices[region][:, 1],
            color=c)

#ax.set_xlim(0, w)
#ax.set_ylim(0, h)
ax.grid(linestyle='--')

fig.savefig('scipy_matplotlib_delaunay_voronoi.png')