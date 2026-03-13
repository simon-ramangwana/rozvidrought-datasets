from rozvidrought_datasets.grid import pixel_id_to_bounds


def test_pixel_bounds_shape():
    bounds = pixel_id_to_bounds(0)

    assert isinstance(bounds, tuple)
    assert len(bounds) == 4