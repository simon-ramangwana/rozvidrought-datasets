from .spec import (
    ORIGIN_X,
    ORIGIN_Y,
    PIXEL_SIZE_X,
    PIXEL_SIZE_Y,
    WIDTH,
    HEIGHT,
)

from .indexing import row_col_to_pixel_id


def coord_to_row_col(lon: float, lat: float):
    col = int((lon - ORIGIN_X) / PIXEL_SIZE_X)
    row = int((lat - ORIGIN_Y) / PIXEL_SIZE_Y)

    if not (0 <= row < HEIGHT and 0 <= col < WIDTH):
        raise ValueError("Coordinate outside Rozvi grid")

    return row, col


def coord_to_pixel_id(lon: float, lat: float):
    row, col = coord_to_row_col(lon, lat)
    return row_col_to_pixel_id(row, col)