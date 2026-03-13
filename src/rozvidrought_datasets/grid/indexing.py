from .spec import WIDTH, HEIGHT, TOTAL_CELLS


def row_col_to_pixel_id(row: int, col: int) -> int:
    if not (0 <= row < HEIGHT):
        raise ValueError(f"row must be between 0 and {HEIGHT - 1}")
    if not (0 <= col < WIDTH):
        raise ValueError(f"col must be between 0 and {WIDTH - 1}")
    return row * WIDTH + col


def pixel_id_to_row_col(pixel_id: int) -> tuple[int, int]:
    if not (0 <= pixel_id < TOTAL_CELLS):
        raise ValueError(f"pixel_id must be between 0 and {TOTAL_CELLS - 1}")
    row = pixel_id // WIDTH
    col = pixel_id % WIDTH
    return row, col