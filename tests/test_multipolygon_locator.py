from shapely.geometry import Polygon, MultiPolygon
from rozvidrought_datasets.locator import multipolygon_to_pixels


def test_multipolygon_to_pixels_returns_list():
    poly1 = Polygon([
        (30.0, -18.0),
        (30.1, -18.0),
        (30.1, -18.1),
        (30.0, -18.1),
        (30.0, -18.0),
    ])

    poly2 = Polygon([
        (30.2, -18.0),
        (30.3, -18.0),
        (30.3, -18.1),
        (30.2, -18.1),
        (30.2, -18.0),
    ])

    mp = MultiPolygon([poly1, poly2])
    pixels = multipolygon_to_pixels(mp)

    assert isinstance(pixels, list)
    assert len(pixels) > 0