from rozvidrought_datasets.grid import (
    row_col_to_pixel_id,
    pixel_id_to_row_col,
)


def test_row_col_roundtrip():
    row = 10
    col = 20

    pixel = row_col_to_pixel_id(row, col)
    r, c = pixel_id_to_row_col(pixel)

    assert r == row
    assert c == col