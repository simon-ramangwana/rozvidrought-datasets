from shapely.geometry import Polygon
from rozvidrought_datasets.grid import pixel_id_to_polygon, RozviGrid


def polygon_pixel_overlap(polygon: Polygon):
    grid = RozviGrid()
    results = []

    for pixel_id in range(grid.width * grid.height):
        cell_poly = Polygon(pixel_id_to_polygon(pixel_id))

        if polygon.intersects(cell_poly):
            inter = polygon.intersection(cell_poly)
            frac = inter.area / cell_poly.area
            results.append((pixel_id, frac))

    return results