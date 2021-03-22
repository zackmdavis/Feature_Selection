import itertools
from random import random, choice
from math import sqrt

from PIL import Image
import numpy as np


# TODO fix before publicaiton: run analysis seems to have a bug for lavender?! Square lengths are non-constant!?


WIDTH = LENGTH = 473


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


color_map = {
    "RED": (200, 0, 0),
    "GREEN": (0, 200, 0),
    "BLUE": (0, 0, 200),
    "TEAL": (0, 150, 150),
    "LAVENDER": (150, 100, 200),
    "YELLOW": (240, 240, 0),
}

def read_label(label):
    return ''.join(chr(c) for c in label)

def triangle_points():
    return [(157*random(), 157*random()), (315+157*random(), 157+157*random()), (157*random(), 315+157*random())]


def in_triangle(q, points):
    s, t = cartesian_to_barycentric(q, *points)
    return s > 0 and t > 0 and 1 - s - t > 0


def noise(color):
    return [c + 10*random() for c in color]

def triangle_pixels(color):
    points = triangle_points()
    return [[noise(color) if in_triangle((x, y), points) else noise((0, 0, 0)) for x in range(WIDTH)] for y in range(LENGTH)]

def symmetric_params():
    return [(150 + 100*random())/2, 236 + 100*(random() - 0.5), 236 + 100*(random() - 0.5)]

def square_pixels(color):
    halflength, x_center, y_center = symmetric_params()
    pixels = []
    for x in range(WIDTH):
        row = []
        for y in range(LENGTH):
            if abs(x_center - x) < halflength and abs(y_center - y) < halflength:
                row.append(noise(color))
            else:
                row.append(noise((0, 0, 0)))
        pixels.append(row)
    return pixels

def circle_pixels(color):
    radius, x_center, y_center = symmetric_params()
    pixels = []
    for x in range(WIDTH):
        row = []
        for y in range(LENGTH):
            if sqrt((x - x_center)**2 + (y - y_center)**2) < radius:
                row.append(noise(color))
            else:
                row.append(noise((0, 0, 0)))
        pixels.append(row)
    return pixels

def data_array(pixels):
    data = []
    for row in pixels:
        for pixel in row:
            for channel in pixel:
                data.append(int(channel))
    return data

def count_burst_lengths(data):
    bursts = []
    counter = 0
    previous = None
    for datum in data:
        if datum >= 240:
            counter += 1
        else:
            # consecutive "ordinary" numbers mean the burst is over
            if counter and previous and previous < 240:
                bursts.append(counter)
                counter = 0
        previous = datum
    return bursts


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

import collections
from itertools import chain, repeat
import operator
def convolve(signal, kernel):
    # See:  https://betterexplained.com/articles/intuitive-convolution/
    # convolve(data, [0.25, 0.25, 0.25, 0.25]) --> Moving average (blur)
    # convolve(data, [1, -1]) --> 1st finite difference (1st derivative)
    # convolve(data, [1, -2, 1]) --> 2nd finite difference (2nd derivative)
    kernel = tuple(kernel)[::-1]
    n = len(kernel)
    window = collections.deque([0], maxlen=n) * n
    for x in chain(signal, repeat(0, n-1)):
        window.append(x)
        yield round(sum(map(operator.mul, kernel, window)), 2)


def smoothed(data):
    smoothed = []
    return list(convolve(data, [0.25, 0.25, 0.25, 0.25]))


def find_burst(seq):
    for i, el in enumerate(seq):
        if el > 100:
            return i


def do_shape(color_name, shape_name):
    color = color_map[color_name]
    if shape_name == "TRIANGLE":
        pixels = triangle_pixels(color)
    elif shape_name == "SQUARE":
        pixels = square_pixels(color)
    elif shape_name == "CIRCLE":
        pixels = circle_pixels(color)

    label = [ord(c) for c in "{} {}".format(color_name, shape_name)]
    data = data_array(pixels)
    run_analysis = high_runs(data)
    diffs = run_derivative(run_analysis)
    array = np.array(pixels, dtype=np.uint8)
    shape_image = Image.fromarray(array)
    shape_image.save("{}_{}.png".format(color_name.lower(), shape_name.lower()))
    return data, run_analysis, diffs, label


def do_random_shape(no_square=False):
    if no_square:
        shape_names = ["TRIANGLE", "SQUARE", "CIRCLE"]
    else:
        shape_names = ["TRIANGLE", "CIRCLE"]
    color_name = choice(list(color_map.keys()))
    shape_name = choice(shape_names)
    return do_shape(color_name, shape_name)
