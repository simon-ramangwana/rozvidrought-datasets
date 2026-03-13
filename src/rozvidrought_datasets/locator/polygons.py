from shapely.geometry import Polygon
from rozvidrought_datasets.grid import RozviGrid, pixel_id_to_polygon


def polygon_to_pixels(polygon: Polygon):
    grid = RozviGrid()
    pixels = []

    for pixel_id in range(grid.width * grid.height):
        cell_poly = Polygon(pixel_id_to_polygon(pixel_id))

        if polygon.intersects(cell_poly):
            pixels.append(pixel_id)

    return pixels