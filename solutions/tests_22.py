import unittest
import numpy as np


def normalize (vec: np.ndarray):
    sum = np.sum(vec, axis=1)[:, np.newaxis]
    return vec/sum


class TestClass(unittest.TestCase):
    def test_normalize(self):

        ones = np.ones([5])
        v = np.random.randint(low=0, high=100, size=[5, 5])

        normalized = normalize(v)
        print(normalized.sum(axis=1))

        # флакует. Где-то не сходится иррациональная сумма
        self.assertTrue((normalized.sum(axis=1) == ones).all())

if __name__ == '__main__':
    unittest.main()