

def find_intersecting_points(filepath, bbox):
    cdef float minx = bbox[0]
    cdef float miny = bbox[1]
    cdef float maxx = bbox[2]
    cdef float maxy = bbox[3]
    cdef float lat, lon
    cdef int counter = 0

    intersecting_points = set()
    points_file = open(filepath, 'r')
    points_file.readline()  # skip header
    for line in points_file:
        if (counter % 100000) == 0:
            print(counter)

        counter += 1
        lat, lon = [float(c) for c in line.split(',')[-3:-1]]

        if not minx <= lon <= maxx:
            continue

        if not miny <= lat <= maxx:
            continue

        intersecting_points.add((lat, lon))

    return intersecting_points
