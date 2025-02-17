import unittest
import numpy as np

class TestClases(unittest.TestCase):
    def test_nan_is_string_for_nan(self):
        self.assertEqual(np.nan.__str__(), 'nan')
    def test_zero_to_nan(self):
        self.assertEqual(str(0*np.nan), 'nan')
    def test_nan_is_singletone(self):
        self.assertFalse(np.nan == np.nan)
    def test_inf_more_then_nan(self):
        self.assertFalse(np.inf>np.nan)

    def test_nan_minus_nan_is_nun(self):
        self.assertEqual(str(np.nan - np.nan), 'nan')

    def test_is_nan_in_set(self):
        # nan на самом деле равен nan-у, но имплементация сравнения (?) сделана, чтоб не был равен.
        # хотя пересоздание nan-ов делает их разными (??) https://github.com/numpy/numpy/issues/9358
        self.assertTrue(np.nan in {np.nan})

    def test_03_multiply(self):
        # конечно, как и везде, это разные значения из-за особенностей 2ичной системы счисления и округлений
        self.assertFalse(0.3 == 3*0.1)


if __name__ == '__main__':
    unittest.main()