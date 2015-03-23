# Copyright (c) 2015, Warren Weckesser.  All rights reserved.
# This software is licensed according to the "BSD 2-clause" license.

cimport cython


@cython.boundscheck(False)
cdef int bres_segment_count(int x0, int y0, int x1, int y1,
                            int[:, :] grid, int endpoint):
    """Bresenham's algorithm.

    See http://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm
    """

    cdef unsigned nrows, ncols
    cdef int e2, sx, sy, err
    cdef int dx, dy

    nrows = grid.shape[0]
    ncols = grid.shape[1]

    if x1 > x0:
        dx = x1 - x0
    else:
        dx = x0 - x1
    if y1 > y0:
        dy = y1 - y0
    else:
        dy = y0 - y1

    sx = 0
    if x0 < x1:
        sx = 1
    else:
        sx = -1
    sy = 0
    if y0 < y1:
        sy = 1
    else:
        sy = -1

    err = dx - dy

    while True:
        # When endpoint is 0, this test occurs before we increment the
        # grid value, so we don't count the last point.
        if endpoint == 0 and x0 == x1 and y0 == y1:
            break

        if (0 <= x0 < nrows) and (0 <= y0 < ncols):
            grid[x0, y0] += 1

        if x0 == x1 and y0 == y1:
            break

        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy

    return 0


def bres_curve_count(int[:] x, int[:] y, int[:, :] grid):
    cdef unsigned k
    cdef int x0, y0, x1, y1

    for k in range(len(x)-1):
        x0 = x[k]
        y0 = y[k]
        x1 = x[k+1]
        y1 = y[k+1]
        bres_segment_count(x0, y0, x1, y1, grid, 0)

    if 0 <= x1 < grid.shape[0] and 0 <= y1 < grid.shape[1]:
        # Count the last point in the curve.
        grid[x1, y1] += 1


def bres_segments_count(int[:, :] segments, int[:, :] grid):
    cdef unsigned k

    for k in range(segments.shape[0]):
        bres_segment_count(segments[k,0], segments[k, 1],
                           segments[k,2], segments[k, 3], grid, 1)
