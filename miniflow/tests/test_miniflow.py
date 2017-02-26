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

#///////////////////////////////////////////////////
# miniflow
#---------------------------------------------------
from miniflow.miniflow import Node

#---------------------------------------------------
import unittest

#///////////////////////////////////////////////////
class TestMiniflow(unittest.TestCase):
    """
        `TestMiniflow()` class is unit-testing the class
        Node().
    """

    #///////////////////////////////////////////////////
    def setUp(self):
        self.name = 'My name'

    def test_print_name(self):
        print(self.name)