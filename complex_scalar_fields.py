import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate
import shapely.geometry as geom
import random

fig, ax = plt.subplots()

phi = np.linspace(0, 2*np.pi, 100)
R = 1
array_x = R * np.cos(phi)
array_y = R * np.sin(phi)

spline_coords, figure_spline_part = interpolate.splprep([array_x, array_y], s=0)
spline_curve = interpolate.splev(figure_spline_part, spline_coords)

curve_coords = []
points_coords = []
for i in range(len(spline_curve[0])):
    curve_coords.append([spline_curve[0][i], spline_curve[1][i]])

polygon = geom.Polygon(curve_coords)
points_number_per_side = 100
x_pictures_limits = [-1, 1]
y_pictures_limits = [-1, 1]

for x_point_coord in np.linspace(*x_pictures_limits, points_number_per_side):
    for y_point_coord in np.linspace(*y_pictures_limits, points_number_per_side):
        p = geom.Point(x_point_coord, y_point_coord)
        if p.within(polygon):
            points_coords.append(x_point_coord)
            points_coords.append(y_point_coord)

x_p = np.array(points_coords[0::2])
y_p = np.array(points_coords[1::2])

def bell_function(x, y, intensity=1, dec_rate=[0.5, 0.5]):
    scalar_field = intensity*np.exp(-dec_rate[0] * x**2 - dec_rate[1] * y**2)
    return scalar_field

intensity_centrums_x = [-0.5, 0.5, -0.4, 0.0, 0.4]
intensity_centrums_y = [-0.3, 0.3, -0.5, -0.7, -0.5]
intensity_values = [1.7, 1.7, 1, 0.7, 1]

def scalar_function(x, y, int_cen_x, int_cen_y, int_vel):
    scalar_field = 0
    for i in range(0, len(int_cen_x)):
        scalar_field += int_vel[i] * bell_function(x - int_cen_x[i], y - int_cen_y[i], 30, [5, 5])
    return scalar_field

sc_plot = ax.scatter(x_p, y_p, c=scalar_function(x_p, y_p, 5400, [10, 10])) 

ax.set_xlabel('Координата x, м')
ax.set_ylabel('Координата y, м')

cbar = fig.colorbar(sc_plot)
cbar.set_label('Интенсивность скалярного поля, *C')
plt.axis('equal')
plt.savefig("complex_scalar_fields.png")