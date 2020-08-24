import sys

import pyximport
pyximport.install()

import iterate_over_points

# Approximate bbox for Beijing area
# minx, miny, maxx, maxy
BBOX = (114.613, 37.811, 118.93, 40.827)

if __name__ == '__main__':
    matching_points = iterate_over_points.find_intersecting_points(sys.argv[1], BBOX)
    print(matching_points)
    print(len(matching_points))
