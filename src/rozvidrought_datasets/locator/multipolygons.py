from shapely.geometry import MultiPolygon
from .polygons import polygon_to_pixels


def multipolygon_to_pixels(multipolygon: MultiPolygon):
    pixels = set()

    for polygon in multipolygon.geoms:
        pixels.update(polygon_to_pixels(polygon))

    return sorted(pixels)