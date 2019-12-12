
import pandas as pd

import pylife.utils.hotspot


def test_single_hotspot_1d():
    df = pd.DataFrame({'node_id':    [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8],
                       'element_id': [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7],
                       'x': [1.0, 2.0, 2.0, 3.0, 3.0, 4.0, 4.0, 5.0, 5.0, 6.0, 6.0, 7.0, 7.0, 8.0],
                       'y': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                       'v': [0.0, 1.0, 1.0, 2.0, 2.0, 9.9, 9.9, 9.0, 9.0, 8.0, 8.0, 2.0, 2.0, 0.0]
                       }).set_index(['node_id', 'element_id'])

    hs = df.hotspot.calc('v', 0.9)
    rf = pd.Series([0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0], name='hotspot', index=df.index)

    pd.testing.assert_series_equal(rf, hs)


def test_double_hotspot_1d():
    df = pd.DataFrame({'node_id':    [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8],
                       'element_id': [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7],
                       'x': [1.0, 2.0, 2.0, 3.0, 3.0, 4.0, 4.0, 5.0, 5.0, 6.0, 6.0, 7.0, 7.0, 8.0],
                       'y': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                       'v': [9.0, 9.9, 9.7, 9.0, 9.0, 1.0, 1.0, 2.0, 2.0, 9.0, 9.0, 9.5, 9.5, 9.0]
                       }).set_index(['node_id', 'element_id'])

    hs = df.hotspot.calc('v', 0.9)
    rf = pd.Series([1, 1, 1, 1, 1, 0, 0, 0, 0, 2, 2, 2, 2, 2], name='hotspot', index=df.index)

    pd.testing.assert_series_equal(rf, hs)


def test_hotspot_numerical_artefact():
    df = pd.DataFrame({'node_id':    [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8],
                       'element_id': [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7],
                       'x': [1.0, 2.0, 2.0, 3.0, 3.0, 4.0, 4.0, 5.0, 5.0, 6.0, 6.0, 7.0, 7.0, 8.0],
                       'y': [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                       'v': [9.0, 99, 9.7, 9.0, 9.0, 1.0, 1.0, 2.0, 2.0, 9.0, 9.0, 9.5, 9.5, 9.0]
                       }).set_index(['node_id', 'element_id'])

    hs = df.hotspot.calc('v', 0.9, artefact_threshold=20.0)
    rf = pd.Series([1, 1, 1, 1, 1, 0, 0, 0, 0, 2, 2, 2, 2, 2], name='hotspot', index=df.index)

    pd.testing.assert_series_equal(rf, hs)
