import unittest
from criticaltests import suite as critical
from extendedtests import suite as extended

alltests = unittest.TestSuite((critical, extended))
