from .bounds import pixel_id_to_bounds


def pixel_id_to_polygon(pixel_id):
    left, bottom, right, top = pixel_id_to_bounds(pixel_id)

    return [
        (left, bottom),
        (left, top),
        (right, top),
        (right, bottom),
        (left, bottom),
    ]