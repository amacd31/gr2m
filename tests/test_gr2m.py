import os
import unittest

import pandas as pd
import numpy as np
from numpy.testing import assert_array_equal, assert_array_almost_equal

from gr2m import gr2m

class Gr2mTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_gr2m(self):
        data = pd.read_csv(
            os.path.join(
                os.path.dirname(__file__),
                '410730_mm_data.csv'
            ),
            skiprows=34,
            parse_dates = True,
            index_col = 'Timestamp'
        )
        qsim_expected = np.loadtxt(
            os.path.join(
                os.path.dirname(__file__),
                'results_test_one.csv'
            )
        )

        params = {
                    'X1': 1065.39379,
                    'X2': 0.891360253,
                }

        qsim = gr2m(data['P (mm)'], data['PE (mm)'], params)

        assert_array_almost_equal(qsim, qsim_expected, 12)

    def test_gr2m_states(self):

        params = {
            'X1': 1.,
            'X2': 1.,
        }

        expected = [
            0.0009450053530676,
            0.0327630181266177,
            0.2055971698811440,
            0.6632149029988140,
            0.9919273718874510,
            1.0533436405957100,
            0.9029856114321760,
        ]

        expected_state = {
            'production_store': 0.1792526700466929,
            'routing_store': 6.922989036389427,
        }

        initial_qsim, state = gr2m(
            [1., 2., 3., 4.],
            [1., 1., 1., 1.],
            params,
            return_state = True
        )

        later_qsim, state = gr2m(
            [3., 2., 1.],
            [1., 1., 1.],
            params,
            states = state,
            return_state = True
        )

        qsim = initial_qsim + later_qsim

        self.assertEqual(expected_state, state)
        assert_array_almost_equal(expected, qsim, 12)

if __name__ == '__main__':
    unittest.main()
