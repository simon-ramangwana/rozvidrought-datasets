from rozvidrought_datasets.grid import coord_to_pixel_id, coord_to_row_col


def point_to_pixel(lon: float, lat: float) -> int:
    return coord_to_pixel_id(lon, lat)


def point_to_row_col(lon: float, lat: float):
    return coord_to_row_col(lon, lat)