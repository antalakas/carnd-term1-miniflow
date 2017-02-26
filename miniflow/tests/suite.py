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
from test_miniflow import TestMiniflow
#---------------------------------------------------

#///////////////////////////////////////////////////
def test_suite():
    """
        `test_suite()` method creates a test suite
        for the unit-tests of dbapi package.
    """

    allTests = unittest.TestSuite()

    # Adding TestMiniflow tests
    allTests.addTest(TestMiniflow('test_print_name'))

    return allTests

