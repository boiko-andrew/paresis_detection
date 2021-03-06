import numpy as np


def shape_to_np_array(lib_shape, data_type="int"):
    # Initialize the list of (x, y)-coordinates
    coords = np.zeros((68, 2), dtype=data_type)
    # Loop over the 68 facial landmarks and convert them
    # to a 2-tuple of (x, y)-coordinates
    for i in range(0, 68):
        coords[i] = (lib_shape.part(i).x, lib_shape.part(i).y)
    # Return the list of (x, y)-coordinates
    return coords


def shape_to_row_array(lib_shape):
    # Initialize an empty list of coordinates
    coords = []
    for i in range(0, 68):
        coords.append(int(lib_shape.part(i).x))
        coords.append(int(lib_shape.part(i).y))
    # Return the row vector of coordinates (x-coordinate then y coordinate,
    # then next x-coordinate and so on...
    return coords


def row_array_to_np_array(row_array, data_type="int"):
    # Initialize the list of (x, y)-coordinates
    coords = np.zeros((68, 2), dtype=data_type)
    # Loop over the 68 facial landmarks and convert them
    # to a 2-tuple of (x, y)-coordinates
    for i in range(0, 68):
        coords[i] = (row_array[i * 2], row_array[i * 2 + 1])
    # Return the list of (x, y)-coordinates
    return coords
