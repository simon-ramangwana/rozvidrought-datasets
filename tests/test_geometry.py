from rozvidrought_datasets.grid import pixel_id_to_polygon


def test_pixel_polygon_is_closed():
    poly = pixel_id_to_polygon(0)

    assert isinstance(poly, list)
    assert len(poly) == 5
    assert poly[0] == poly[-1]