import sys

import pyximport
pyximport.install()

import iterate_over_points

# Approximate bbox for Beijing area
# minx, miny, maxx, maxy
BBOX = (114.613, 37.811, 118.93, 40.827)

if __name__ == '__main__':
    matching_points = iterate_over_points.find_intersecting_points(sys.argv[1], BBOX)
    print(len(matching_points))

    with open('output.csv', 'w') as out_file:
        out_file.write('latitude,longitude\n')
        for matching_point in matching_points:
            out_file.write(f'{matching_point[0]},{matching_point[1]}\n')
