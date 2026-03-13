from rozvidrought_datasets.grid import pixel_id_to_bounds


def test_pixel_bounds_order():
    left, bottom, right, top = pixel_id_to_bounds(0)

    assert left < right
    assert bottom < top