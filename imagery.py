import itertools
from random import random

from PIL import Image
import numpy as np


# https://stackoverflow.com/a/14382692
def cartesian_to_barycentric(q, p0, p1, p2):
    d = 0.5 * (
        -p1[1] * p2[0]
        + p0[1] * (-p1[0] + p2[0])
        + p0[0] * (p1[1] - p2[1])
        + p1[0] * p2[1]
    )
    s = (
        1
        / (2 * d)
        * (
            p0[1] * p2[0]
            - p0[0] * p2[1]
            + (p2[1] - p0[1]) * q[0]
            + (p0[0] - p2[0]) * q[1]
        )
    )
    t = (
        1
        / (2 * d)
        * (
            p0[0] * p1[1]
            - p0[1] * p1[0]
            + (p0[1] - p1[1]) * q[0]
            + (p1[0] - p0[0]) * q[1]
        )
    )
    return s, t


def triangle_points():
    return [(100*random(), 100*random()) for _ in range(3)]


def in_triangle(q, points):
    s, t = cartesian_to_barycentric(q, *points)
    return s > 0 and t > 0 and 1 - s - t > 0


def square_points():
    ...

def noise(color):
    return [c + 10*random() for c in color]


def triangle_pixels(color):
    points = triangle_points()
    # points = [(50, 10), (10, 50), (90, 90)]
    return [[noise(color) if in_triangle((x, y), points) else noise((0, 0, 0)) for x in range(100)] for y in range(100)]


def data_array(pixels):
    data = []
    for row in pixels:
        for pixel in row:
            for channel in pixel:
                data.append(int(channel))
    return data

def high_runs(data):
    runs = []
    high_counter = 0
    low_counter = 0
    for datum in data:
        if datum > 100:
            high_counter += 1
            low_counter = 0
        if datum < 100:
            low_counter += 1
        if low_counter > 3 and high_counter > 1:
            runs.append(high_counter)
            low_counter = high_counter = 0
    return runs

def run_derivative(run_sequence):
    diffs = []
    previous = run_sequence[0]
    for run in run_sequence[1:]:
        diffs.append(run - previous)
        previous = run
    return diffs

pixels = triangle_pixels((120, 20, 250))
array = data_array(pixels)
print(array)
print(len(array))
run_analysis = high_runs(array)
print(run_analysis)
print(len(run_analysis))
print(run_derivative(run_analysis))

array = np.array(pixels, dtype=np.uint8)
shape_image = Image.fromarray(array)
shape_image.save("shape.png")
