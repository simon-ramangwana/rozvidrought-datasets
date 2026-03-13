from .spec import WIDTH, HEIGHT
from .indexing import row_col_to_pixel_id, pixel_id_to_row_col
from .locator import coord_to_pixel_id, coord_to_row_col
from .bounds import pixel_id_to_bounds


class RozviGrid:

    def __init__(self):
        self.width = WIDTH
        self.height = HEIGHT

    def row_col_to_pixel(self, row, col):
        return row_col_to_pixel_id(row, col)

    def pixel_to_row_col(self, pixel_id):
        return pixel_id_to_row_col(pixel_id)

    def coord_to_pixel(self, lon, lat):
        return coord_to_pixel_id(lon, lat)

    def coord_to_row_col(self, lon, lat):
        return coord_to_row_col(lon, lat)

    def pixel_bounds(self, pixel_id):
        return pixel_id_to_bounds(pixel_id)