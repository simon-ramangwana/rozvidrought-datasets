from shapely.geometry import Polygon
from rozvidrought_datasets.locator import polygon_pixel_overlap


def test_polygon_pixel_overlap_returns_fractions():
    poly = Polygon([
        (30.0, -18.0),
        (30.1, -18.0),
        (30.1, -18.1),
        (30.0, -18.1),
        (30.0, -18.0),
    ])

    overlaps = polygon_pixel_overlap(poly)

    assert isinstance(overlaps, list)
    assert len(overlaps) > 0
    assert isinstance(overlaps[0][0], int)
    assert 0 < overlaps[0][1] <= 1