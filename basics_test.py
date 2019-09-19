import unittest
import statistics as stats
import random as rd
import get_column_stats as gcs
import os


class TestStats(unittest.TestCase):

    def tearDown(self):
        os.remove('data.txt')

    def test_mean_empty(self):
        # Test handling of empty files in col_mean_finder function
        test_file = open('data.txt', 'w')
        test_file.close()
        self.assertRaises(ZeroDivisionError,
                          gcs.col_mean_finder, 'data.txt', 0)

    def test_stdev_empty(self):
        # Test handling of empty files in col_stdev_finder function
        test_file = open('data.txt', 'w')
        test_file.close()
        self.assertRaises(ZeroDivisionError, gcs.col_stdev_finder,
                          'data.txt', 0)

    def test_stdev_nonnumber(self):
        # Test handling of non-number entry errors in col_stdev_finder function
        test_file = open('data.txt', 'w')
        test_file.write('foo')
        test_file.close()
        self.assertRaises(ValueError, gcs.col_stdev_finder,
                          'data.txt', 0)

    def test_mean_nonnumber(self):
        # Test handling of non-number entry errors in col_mean_finder function
        test_file = open('data.txt', 'w')
        test_file.write('foo')
        test_file.close()
        self.assertRaises(ValueError, gcs.col_mean_finder,
                          'data.txt', 0)

    def test_mean_constant(self):
        # Test col_mean_finder on data set populated with one number 100 times
        # Such that the mean is that number
        test_data = []
        open('data.txt', 'w')
        for i in range(1, 100):
            test_data.append(1)
        test_file = open('data.txt', 'a')
        for element in test_data:
            print(element, file=test_file)
        test_file.close()
        self.assertEqual(gcs.col_mean_finder('data.txt', 0), 'mean: 1.0')

    def test_stdev_constant(self):
        # Test col_stdev_finder on dataset populated with one number 100 times
        # Such that stdev should be 0
        test_data = []
        open('data.txt', 'w')
        for i in range(1, 100):
            test_data.append(1)
        test_file = open('data.txt', 'a')
        for element in test_data:
            print(element, file=test_file)
        test_file.close()
        self.assertEqual(gcs.col_stdev_finder('data.txt', 0), 'stdev: 0.0')

    def test_mean_variable(self):
        # Test col_mean_finder on a random data set 100 times
        for i in range(1, 100):
            test_data = []
            open('data.txt', 'w')
            # Populate data set with 100 random numbers 1-10000
            for i in range(1, 100):
                x = rd.randint(1, 10000)
                test_data.append(x)
            test_file = open('data.txt', 'a')
            for element in test_data:
                print(element, file=test_file)
            test_file.close()
            test_mean = sum(test_data) / len(test_data)
            self.assertEqual(gcs.col_mean_finder('data.txt', 0),
                             'mean: ' + str(test_mean))

    def test_stdev_variable(self):
        # I will use another module 'statistics' to test whether
        # col_stdev_finder is working
        # Additionally, I will test 1000 random data sets
        for i in range(1, 1000):
            test_data = []
            open('data.txt', 'w')
            # Populate data set with 100 random numbers 1-10000
            for i in range(1, 100):
                x = rd.randint(1, 10000)
                test_data.append(x)
            test_file = open('data.txt', 'a')
            for element in test_data:
                print(element, file=test_file)
            test_file.close()
            test_stdev = stats.stdev(test_data)
            # due to rounding errors, assert that
            # the first few decimal places match
            self.assertIn('stdev: ' + str(float(str(test_stdev)[:-7])),
                          gcs.col_stdev_finder('data.txt', 0))


if __name__ == '__main__':
    unittest.main()
