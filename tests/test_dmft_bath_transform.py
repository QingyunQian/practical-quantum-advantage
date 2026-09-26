"""Check the analytic semicircle transform against independent quadrature."""

import math
import unittest

from numerics.dmft_semicircle_bath import discrete_delta, exact_delta, semicircle_bath


class SemicircleTransformTest(unittest.TestCase):
    def test_matsubara_transform(self):
        nodes, weights = semicircle_bath(2048)
        for beta in (16, 64, 128):
            for index in (0, 2, 10):
                omega = (2 * index + 1) * math.pi / beta
                numerical = discrete_delta(omega, nodes, weights)
                analytic = exact_delta(omega)
                self.assertLess(abs(numerical - analytic), 1e-8)


if __name__ == "__main__":
    unittest.main()
