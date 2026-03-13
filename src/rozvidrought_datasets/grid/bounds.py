from .spec import (
    ORIGIN_X,
    ORIGIN_Y,
    PIXEL_SIZE_X,
    PIXEL_SIZE_Y,
)

from .indexing import pixel_id_to_row_col


def pixel_id_to_bounds(pixel_id: int) -> tuple[float, float, float, float]:
    row, col = pixel_id_to_row_col(pixel_id)

    left = ORIGIN_X + (col * PIXEL_SIZE_X)
    right = left + PIXEL_SIZE_X

    top = ORIGIN_Y + (row * PIXEL_SIZE_Y)
    bottom = top + PIXEL_SIZE_Y

    return left, bottom, right, top