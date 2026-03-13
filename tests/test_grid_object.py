from rozvidrought_datasets.grid import RozviGrid


def test_grid_object_methods():
    grid = RozviGrid()

    pixel = grid.row_col_to_pixel(10, 20)
    row, col = grid.pixel_to_row_col(pixel)

    assert row == 10
    assert col == 20