import sys
import os

from osgeo import ogr

if os.path.exists('output_shapefile.shp'):
    os.remove('output_shapefile.shp')

driver = ogr.GetDriverByName('ESRI Shapefile')
new_vector = driver.CreateDataSource('output_shapefile.shp')
new_layer = new_vector.CreateLayer('output_shapefile', geom_type=ogr.wkbPoint)
new_layer_defn = new_layer.GetLayerDefn()
with open('output.csv') as points:
    points.readline()  # skip the header line
    for line in points:
        y, x = [float(p) for p in line.strip().split(',')]
        new_feature = ogr.Feature(new_layer_defn)
        wkt = f'POINT ({x} {y})'
        new_geometry = ogr.CreateGeometryFromWkt(wkt)
        if new_geometry is None:
            print(f'Invalid wkt: {wkt}')
            sys.exit(1)

        new_feature.SetGeometry(new_geometry)
        new_layer.CreateFeature(new_feature)

new_layer = None
new_vector = None
