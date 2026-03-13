from shapely.geometry import MultiPolygon
from .overlap import polygon_pixel_overlap


def multipolygon_pixel_overlap(multipolygon: MultiPolygon):
    merged = {}

    for polygon in multipolygon.geoms:
        for pixel_id, frac in polygon_pixel_overlap(polygon):
            merged[pixel_id] = merged.get(pixel_id, 0.0) + frac

    return sorted(
        [(pixel_id, min(frac, 1.0)) for pixel_id, frac in merged.items()],
        key=lambda x: x[0],
    )