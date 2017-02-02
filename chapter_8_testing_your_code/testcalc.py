import unittest
import calc

#
# Define the test class
#

class testCalc(unittest.TestCase):

    def testSimpleAdd(self):
        result, msg = calc.calc(1, '+', 1)
        self.assertEqual(result, 2.0)

    def testLargeProduct(self):
        result, msg = calc.calc(123456789.0, '*', 987654321.0)
        self.assertEqual(result, 1.2193263111263526e+17)

    def testDivByZero(self):
        result, msg = calc.calc(6, '/', 0)
        self.assertEqual(msg, 'ZeroDivisionError')

#
# Create the test suite
#
TestSuite = unittest.TestSuite()

#
# Add tests to the suite
#
TestSuite.addTest(testCalc('testSimpleAdd'))
TestSuite.addTest(testCalc('testLargeProduct'))
TestSuite.addTest(testCalc('testDivByZero'))
#
# Create the test runner
#
runner = unittest.TextTestRunner()

#
# Execute the tests
#
runner.run(TestSuite)
