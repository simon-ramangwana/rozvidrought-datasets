from shapely.geometry import Polygon
from rozvidrought_datasets.locator import polygon_to_pixels


def test_polygon_to_pixels_returns_list():
    poly = Polygon([
        (30.0, -18.0),
        (30.1, -18.0),
        (30.1, -18.1),
        (30.0, -18.1),
        (30.0, -18.0),
    ])

    pixels = polygon_to_pixels(poly)

    assert isinstance(pixels, list)
    assert len(pixels) > 0