import sys
import os

from osgeo import ogr, osr

if os.path.exists('output_shapefile.shp'):
    os.remove('output_shapefile.shp')

source_srs = osr.SpatialReference()
source_srs.ImportFromEPSG(4326)

srs = osr.SpatialReference()
srs.ImportFromEPSG(3857)  # OSM's default EPSG

driver = ogr.GetDriverByName('ESRI Shapefile')
new_vector = driver.CreateDataSource('output_shapefile.shp')
new_layer = new_vector.CreateLayer(
    'output_shapefile', srs, geom_type=ogr.wkbPoint)
new_layer_defn = new_layer.GetLayerDefn()
with open('output.csv') as points:
    points.readline()  # skip the header line
    for line in points:
        y, x = [float(p) for p in line.strip().split(',')]
        #print(f'{y}, {x}')
        #sys.exit(1)
        new_feature = ogr.Feature(new_layer_defn)
        wkt = f'POINT ({x} {y})'
        new_geometry = ogr.CreateGeometryFromWkt(wkt)
        new_geometry.AssignSpatialReference(source_srs)
        new_geometry.TransformTo(srs)
        if new_geometry is None:
            print(f'Invalid wkt: {wkt}')
            sys.exit(1)

        new_feature.SetGeometry(new_geometry)
        new_layer.CreateFeature(new_feature)

new_layer = None
new_vector = None
