# -*- coding: utf-8 -*-


#///////////////////////////////////////////////////
#---------------------------------------------------
# File: test_miniflow.py
# Author: Andreas Ntalakas  https://github.com/antalakas
#---------------------------------------------------

#///////////////////////////////////////////////////
# Python
#---------------------------------------------------
import time
import string
import random
import numpy as np

#///////////////////////////////////////////////////
# miniflow
#---------------------------------------------------
from miniflow.miniflow import *

#---------------------------------------------------
import unittest

#///////////////////////////////////////////////////
class TestMiniflow(unittest.TestCase):
    """
        `TestMiniflow()` class is unit-testing the
        miniflow module.
    """

    #///////////////////////////////////////////////////
    # def setUp(self):
    #     self.name = 'forward propagation'

    def forward_propagation(self):
        # print(self.name)

        x, y = Input(), Input()

        f = AddTwo(x, y)

        feed_dict = {x: 10, y: 5}

        sorted_nodes = topological_sort(feed_dict)
        output = forward_pass(f, sorted_nodes)

        # NOTE: because topological_sort set the values for the `Input` nodes we could also access
        # the value for x with x.value (same goes for y).
        print("{} + {} = {} (according to miniflow)".format(feed_dict[x], feed_dict[y], output))

        self.assertEqual(output, 15)

    def add_x_y_y(self):
        x, y = Input(), Input()

        f = AddTwo(x, y)
        g = AddTwo(f, y)

        feed_dict = {x: 10, y: 5}

        sorted_nodes = topological_sort(feed_dict)
        output = forward_pass(g, sorted_nodes)

        print("({} + {}) + {} = {} (according to miniflow)".format(feed_dict[x], feed_dict[y], feed_dict[y], output))

    def add_multiple(self):
        x, y, z = Input(), Input(), Input()

        f = Add(x, y, z)

        feed_dict = {x: 4, y: 5, z: 10}

        graph = topological_sort(feed_dict)
        output = forward_pass(f, graph)

        # should output 19
        print("{} + {} + {} = {} (according to miniflow)".format(feed_dict[x], feed_dict[y], feed_dict[z], output))

        self.assertEqual(output, 19)

    def mul_multiple(self):
        x, y, z = Input(), Input(), Input()

        f = Mul(x, y, z)

        feed_dict = {x: 4, y: 5, z: 10}

        graph = topological_sort(feed_dict)
        output = forward_pass(f, graph)

        # should output 200
        print("{} * {} * {} = {} (according to miniflow)".format(feed_dict[x], feed_dict[y], feed_dict[z], output))

        self.assertEqual(output, 200)

    def learning_and_loss(self):
        inputs, weights, bias = Input(), Input(), Input()

        f = LinearSimple(inputs, weights, bias)

        feed_dict = {
            inputs: [6, 14, 3],
            weights: [0.5, 0.25, 1.4],
            bias: 2
        }

        graph = topological_sort(feed_dict)
        output = forward_pass(f, graph)

        print("{} * {} + {} = {} (according to miniflow)".format(feed_dict[inputs], feed_dict[weights], feed_dict[bias], output))

        self.assertEqual(output, 12.7)

    def learning_transform(self):
        X, W, b = Input(), Input(), Input()

        f = Linear(X, W, b)

        X_ = np.array([[-1., -2.], [-1, -2]])
        W_ = np.array([[2., -3], [2., -3]])
        b_ = np.array([-3., -5])

        feed_dict = {X: X_, W: W_, b: b_}

        graph = topological_sort(feed_dict)
        output = forward_pass(f, graph)

        print("{} * {} + {} = {} (according to miniflow)".format(feed_dict[X], feed_dict[W], feed_dict[b],
                                                                 output))

        # self.assertEqual(output, [[-9., 4.], [-9., 4.]])