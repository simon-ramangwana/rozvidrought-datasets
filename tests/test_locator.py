from rozvidrought_datasets.grid import coord_to_pixel_id


def test_coord_inside_grid():
    lon = 30.0
    lat = -18.0

    pixel = coord_to_pixel_id(lon, lat)

    assert isinstance(pixel, int)