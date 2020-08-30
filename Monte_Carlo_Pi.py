#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from numpy.random import rand

class MonteCarloPi(object):

    def __init__(self, n):
        self.number_of_points = n
        self.array_xy = []
        self.pi = 0

    # Function that generates the random points and stores them in array_xy
    def generate_points(self):
        x_rand = rand(self.number_of_points)
        y_rand = rand(self.number_of_points)
        self.array_xy = [(x_rand[i], y_rand[i]) for i in range(self.number_of_points)]

    # Function that applies Monte Carlo method to calculate Pi
    def monte_carlo(self):

        ratio = 0
        for point in self.array_xy:
            # distance from origin
            dist_squared = point[0]**2 + point[1]**2
            # We count the point if it fell in the circumference
            if dist_squared < 1:
                ratio += 1
        ratio = ratio / self.number_of_points

        # This ratio is (pi*1^2)/4 // 1*1, so
        self.pi = ratio * 4

    # Function that plots the points
    def plot(self):

        array_in, array_out = [],[]
        fig, ax = plt.subplots(figsize=(5,5))
        for pair in self.array_xy:
            if pair[0]**2 + pair[1]**2 < 1:
                array_in.append(pair)
            else: array_out.append(pair)

        plt.scatter(*zip(*array_in), color='red')
        plt.scatter(*zip(*array_out), color='blue')
        plt.title('nb_of_points: ' + str(self.number_of_points))
        plt.show()


if __name__ == '__main__':

    # number of random points
    N = 10000

    Pi = MonteCarloPi(N)
    Pi.generate_points()
    Pi.monte_carlo()
    print('Value of Pi:', Pi.pi)
    Pi.plot()
