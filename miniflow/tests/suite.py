# -*- coding: utf-8 -*-


#///////////////////////////////////////////////////
#---------------------------------------------------
# File: suite.py
# Author: Andreas Ntalakas  https://github.com/antalakas
#---------------------------------------------------

#///////////////////////////////////////////////////
# Python
#---------------------------------------------------
import os
#---------------------------------------------------
import unittest

#///////////////////////////////////////////////////
# miniflow Tests
#---------------------------------------------------
from tests.test_miniflow import TestMiniflow
#---------------------------------------------------

#///////////////////////////////////////////////////
def test_suite():
    """
        `test_suite()` method creates a test suite
        for the unit-tests of dbapi package.
    """

    allTests = unittest.TestSuite()

    # Adding TestMiniflow tests
    allTests.addTest(TestMiniflow('forward_propagation'))
    allTests.addTest(TestMiniflow('add_x_y_y'))
    allTests.addTest(TestMiniflow('add_multiple'))
    allTests.addTest(TestMiniflow('mul_multiple'))
    allTests.addTest(TestMiniflow('learning_and_loss'))
    allTests.addTest(TestMiniflow('learning_transform'))

    return allTests

