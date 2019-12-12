# -*- coding: utf-8 -*-

"""Data for test evaluation"""

import numpy as np


# (relative amplitude, frequency)
coll_haibach_mod_rel = np.array(
    [[1.25e-01, 6.05e+05],
     [2.75e-01, 2.80e+05],
     [4.25e-01, 9.20e+04],
     [5.75e-01, 2.00e+04],
     [7.25e-01, 2.72e+03],
     [8.50e-01, 2.80e+02],
     [9.50e-01, 1.60e+01],
     [1.00e+00, 2.00e+00]]
)


coll_haibach_mod_acc = np.array(
    [[1.250000e-01, 1.000018e+06],
     [2.750000e-01, 3.950180e+05],
     [4.250000e-01, 1.150180e+05],
     [5.750000e-01, 2.301800e+04],
     [7.250000e-01, 3.018000e+03],
     [8.500000e-01, 2.980000e+02],
     [9.500000e-01, 1.800000e+01],
     [1.000000e+00, 2.000000e+00]]
)


coll_elementar_acc = np.array(
    [[100, 1000000],
     [150,  100000],
     [200,    10000],
     [250,    1000],
     [300,     100],
     [350,      10]])


collective_normalized = np.array(
    [[2.52100840e-02, 1.90733000e+05],
     [4.20168067e-02, 1.81542000e+05],
     [5.88235294e-02, 1.69283000e+05],
     [7.56302521e-02, 1.53244000e+05],
     [9.24369748e-02, 1.24473000e+05],
     [1.09243697e-01, 1.13752000e+05],
     [1.26050420e-01, 8.68020000e+04],
     [1.42857143e-01, 8.11170000e+04],
     [1.59663866e-01, 5.77180000e+04],
     [1.76470588e-01, 5.57260000e+04],
     [1.93277311e-01, 4.17500000e+04],
     [2.10084034e-01, 3.90330000e+04],
     [2.26890756e-01, 3.08470000e+04],
     [2.43697479e-01, 2.80070000e+04],
     [2.60504202e-01, 2.31770000e+04],
     [2.77310924e-01, 2.05320000e+04],
     [2.94117647e-01, 1.78600000e+04],
     [3.10924370e-01, 1.54540000e+04],
     [3.27731092e-01, 1.38670000e+04],
     [3.44537815e-01, 1.16010000e+04],
     [3.61344538e-01, 1.07650000e+04],
     [3.78151261e-01, 8.83100000e+03],
     [3.94957983e-01, 8.44900000e+03],
     [4.11764706e-01, 6.68200000e+03],
     [4.28571429e-01, 6.50400000e+03],
     [4.45378151e-01, 5.04400000e+03],
     [4.62184874e-01, 4.96700000e+03],
     [4.78991597e-01, 3.80100000e+03],
     [4.95798319e-01, 3.72000000e+03],
     [5.12605042e-01, 2.77500000e+03],
     [5.29411765e-01, 2.67100000e+03],
     [5.46218487e-01, 2.01400000e+03],
     [5.63025210e-01, 1.82500000e+03],
     [5.79831933e-01, 1.40300000e+03],
     [5.96638655e-01, 1.19500000e+03],
     [6.13445378e-01, 9.54000000e+02],
     [6.30252101e-01, 7.17000000e+02],
     [6.47058824e-01, 6.40000000e+02],
     [6.63865546e-01, 4.18000000e+02],
     [6.80672269e-01, 3.93000000e+02],
     [6.97478992e-01, 2.57000000e+02],
     [7.14285714e-01, 2.56000000e+02],
     [7.47899160e-01, 1.52000000e+02],
     [7.81512605e-01, 1.04000000e+02],
     [7.98319328e-01, 6.30000000e+01],
     [8.15126050e-01, 6.20000000e+01],
     [8.31932773e-01, 3.40000000e+01],
     [8.48739496e-01, 3.20000000e+01],
     [8.82352941e-01, 1.80000000e+01],
     [8.99159664e-01, 1.20000000e+01],
     [9.15966387e-01, 9.00000000e+00],
     [9.32773109e-01, 5.00000000e+00],
     [9.66386555e-01, 3.00000000e+00],
     [1.00000000e+00, 1.00000000e+00]]
)

collective = np.array(
    [[4.687500e-02, 1.907330e+05],
     [7.812500e-02, 1.815420e+05],
        [1.093750e-01, 1.692830e+05],
        [1.406250e-01, 1.532440e+05],
        [1.718750e-01, 1.244730e+05],
        [2.031250e-01, 1.137520e+05],
        [2.343750e-01, 8.680200e+04],
        [2.656250e-01, 8.111700e+04],
        [2.968750e-01, 5.771800e+04],
        [3.281250e-01, 5.572600e+04],
        [3.593750e-01, 4.175000e+04],
        [3.906250e-01, 3.903300e+04],
        [4.218750e-01, 3.084700e+04],
        [4.531250e-01, 2.800700e+04],
        [4.843750e-01, 2.317700e+04],
        [5.156250e-01, 2.053200e+04],
        [5.468750e-01, 1.786000e+04],
        [5.781250e-01, 1.545400e+04],
        [6.093750e-01, 1.386700e+04],
        [6.406250e-01, 1.160100e+04],
        [6.718750e-01, 1.076500e+04],
        [7.031250e-01, 8.831000e+03],
        [7.343750e-01, 8.449000e+03],
        [7.656250e-01, 6.682000e+03],
        [7.968750e-01, 6.504000e+03],
        [8.281250e-01, 5.044000e+03],
        [8.593750e-01, 4.967000e+03],
        [8.906250e-01, 3.801000e+03],
        [9.218750e-01, 3.720000e+03],
        [9.531250e-01, 2.775000e+03],
        [9.843750e-01, 2.671000e+03],
        [1.015625e+00, 2.014000e+03],
        [1.046875e+00, 1.825000e+03],
        [1.078125e+00, 1.403000e+03],
        [1.109375e+00, 1.195000e+03],
        [1.140625e+00, 9.540000e+02],
        [1.171875e+00, 7.170000e+02],
        [1.203125e+00, 6.400000e+02],
        [1.234375e+00, 4.180000e+02],
        [1.265625e+00, 3.930000e+02],
        [1.296875e+00, 2.570000e+02],
        [1.328125e+00, 2.560000e+02],
        [1.390625e+00, 1.520000e+02],
        [1.453125e+00, 1.040000e+02],
        [1.484375e+00, 6.300000e+01],
        [1.515625e+00, 6.200000e+01],
        [1.546875e+00, 3.400000e+01],
        [1.578125e+00, 3.200000e+01],
        [1.640625e+00, 1.800000e+01],
        [1.671875e+00, 1.200000e+01],
        [1.703125e+00, 9.000000e+00],
        [1.734375e+00, 5.000000e+00],
        [1.796875e+00, 3.000000e+00],
        [1.859375e+00, 1.000000e+00]]
)

collective_original = np.array(
    [[0.015625, 190733.0],
     [0.046875, 190733.0],
     [0.078125, 181542.0],
     [0.109375, 169283.0],
     [0.140625, 153244.0],
     [0.171875, 124473.0],
     [0.203125, 113752.0],
     [0.234375, 86802.0],
     [0.265625, 81117.0],
     [0.296875, 57718.0],
     [0.328125, 55726.0],
     [0.359375, 41750.0],
     [0.390625, 39033.0],
     [0.421875, 30847.0],
     [0.453125, 28007.0],
     [0.484375, 23177.0],
     [0.515625, 20532.0],
     [0.546875, 17860.0],
     [0.578125, 15454.0],
     [0.609375, 13867.0],
     [0.640625, 11601.0],
     [0.671875, 10765.0],
     [0.703125, 8831.0],
     [0.734375, 8449.0],
     [0.765625, 6682.0],
     [0.796875, 6504.0],
     [0.828125, 5044.0],
     [0.859375, 4967.0],
     [0.890625, 3801.0],
     [0.921875, 3720.0],
     [0.953125, 2775.0],
     [0.984375, 2671.0],
     [1.015625, 2014.0],
     [1.046875, 1825.0],
     [1.078125, 1403.0],
     [1.109375, 1195.0],
     [1.140625, 954.0],
     [1.171875, 717.0],
     [1.203125, 640.0],
     [1.234375, 418.0],
     [1.265625, 393.0],
     [1.296875, 257.0],
     [1.328125, 256.0],
     [1.359375, 152.0],
     [1.390625, 152.0],
     [1.421875, 104.0],
     [1.453125, 104.0],
     [1.484375, 63.0],
     [1.515625, 62.0],
     [1.546875, 34.0],
     [1.578125, 32.0],
     [1.609375, 18.0],
     [1.640625, 18.0],
     [1.671875, 12.0],
     [1.703125, 9.0],
     [1.734375, 5.0],
     [1.765625, 3.0],
     [1.796875, 3.0],
     [1.828125, 1.0],
     [1.859375, 1.0],
     [1.890625, 0],
     [1.921875, 0],
     [1.953125, 0],
     [1.984375, 0]]
)


S_collective_normalized = np.array(
    [0.02521008, 0.04201681, 0.05882353, 0.07563025, 0.09243697,
     0.1092437, 0.12605042, 0.14285714, 0.15966387, 0.17647059,
     0.19327731, 0.21008403, 0.22689076, 0.24369748, 0.2605042,
     0.27731092, 0.29411765, 0.31092437, 0.32773109, 0.34453782,
     0.36134454, 0.37815126, 0.39495798, 0.41176471, 0.42857143,
     0.44537815, 0.46218487, 0.4789916, 0.49579832, 0.51260504,
     0.52941176, 0.54621849, 0.56302521, 0.57983193, 0.59663866,
     0.61344538, 0.6302521, 0.64705882, 0.66386555, 0.68067227,
     0.69747899, 0.71428571, 0.74789916, 0.78151261, 0.79831933,
     0.81512605, 0.83193277, 0.8487395, 0.88235294, 0.89915966,
     0.91596639, 0.93277311, 0.96638655, 1.]
)

S_collective = np.array(
    [0.046875, 0.078125, 0.109375, 0.140625, 0.171875, 0.203125,
     0.234375, 0.265625, 0.296875, 0.328125, 0.359375, 0.390625,
     0.421875, 0.453125, 0.484375, 0.515625, 0.546875, 0.578125,
     0.609375, 0.640625, 0.671875, 0.703125, 0.734375, 0.765625,
     0.796875, 0.828125, 0.859375, 0.890625, 0.921875, 0.953125,
     0.984375, 1.015625, 1.046875, 1.078125, 1.109375, 1.140625,
     1.171875, 1.203125, 1.234375, 1.265625, 1.296875, 1.328125,
     1.390625, 1.453125, 1.484375, 1.515625, 1.546875, 1.578125,
     1.640625, 1.671875, 1.703125, 1.734375, 1.796875, 1.859375]
)

S_collective_original = np.array(
    [0.015625, 0.046875, 0.078125, 0.109375, 0.140625, 0.171875,
     0.203125, 0.234375, 0.265625, 0.296875, 0.328125, 0.359375,
     0.390625, 0.421875, 0.453125, 0.484375, 0.515625, 0.546875,
     0.578125, 0.609375, 0.640625, 0.671875, 0.703125, 0.734375,
     0.765625, 0.796875, 0.828125, 0.859375, 0.890625, 0.921875,
     0.953125, 0.984375, 1.015625, 1.046875, 1.078125, 1.109375,
     1.140625, 1.171875, 1.203125, 1.234375, 1.265625, 1.296875,
     1.328125, 1.359375, 1.390625, 1.421875, 1.453125, 1.484375,
     1.515625, 1.546875, 1.578125, 1.609375, 1.640625, 1.671875,
     1.703125, 1.734375, 1.765625, 1.796875, 1.828125, 1.859375,
     1.890625, 1.921875, 1.953125, 1.984375])


N_collective_accumulated = np.array(
    [1.90733e+05, 1.81542e+05, 1.69283e+05, 1.53244e+05, 1.24473e+05,
     1.13752e+05, 8.68020e+04, 8.11170e+04, 5.77180e+04, 5.57260e+04,
     4.17500e+04, 3.90330e+04, 3.08470e+04, 2.80070e+04, 2.31770e+04,
     2.05320e+04, 1.78600e+04, 1.54540e+04, 1.38670e+04, 1.16010e+04,
     1.07650e+04, 8.83100e+03, 8.44900e+03, 6.68200e+03, 6.50400e+03,
     5.04400e+03, 4.96700e+03, 3.80100e+03, 3.72000e+03, 2.77500e+03,
     2.67100e+03, 2.01400e+03, 1.82500e+03, 1.40300e+03, 1.19500e+03,
     9.54000e+02, 7.17000e+02, 6.40000e+02, 4.18000e+02, 3.93000e+02,
     2.57000e+02, 2.56000e+02, 1.52000e+02, 1.04000e+02, 6.30000e+01,
     6.20000e+01, 3.40000e+01, 3.20000e+01, 1.80000e+01, 1.20000e+01,
     9.00000e+00, 5.00000e+00, 3.00000e+00, 1.00000e+00]
)

N_collective_accumulated_original = np.array(
    [1.90733e+05, 1.90733e+05, 1.81542e+05, 1.69283e+05, 1.53244e+05,
     1.24473e+05, 1.13752e+05, 8.68020e+04, 8.11170e+04, 5.77180e+04,
     5.57260e+04, 4.17500e+04, 3.90330e+04, 3.08470e+04, 2.80070e+04,
     2.31770e+04, 2.05320e+04, 1.78600e+04, 1.54540e+04, 1.38670e+04,
     1.16010e+04, 1.07650e+04, 8.83100e+03, 8.44900e+03, 6.68200e+03,
     6.50400e+03, 5.04400e+03, 4.96700e+03, 3.80100e+03, 3.72000e+03,
     2.77500e+03, 2.67100e+03, 2.01400e+03, 1.82500e+03, 1.40300e+03,
     1.19500e+03, 9.54000e+02, 7.17000e+02, 6.40000e+02, 4.18000e+02,
     3.93000e+02, 2.57000e+02, 2.56000e+02, 1.52000e+02, 1.52000e+02,
     1.04000e+02, 1.04000e+02, 6.30000e+01, 6.20000e+01, 3.40000e+01,
     3.20000e+01, 1.80000e+01, 1.80000e+01, 1.20000e+01, 9.00000e+00,
     5.00000e+00, 3.00000e+00, 3.00000e+00, 1.00000e+00, 1.00000e+00,
     0.00000e+00, 0.00000e+00, 0.00000e+00, 0.00000e+00])



N_collective_relative = np.array(
    [9.1910e+03, 1.2259e+04, 1.6039e+04, 2.8771e+04, 1.0721e+04,
     2.6950e+04, 5.6850e+03, 2.3399e+04, 1.9920e+03, 1.3976e+04,
     2.7170e+03, 8.1860e+03, 2.8400e+03, 4.8300e+03, 2.6450e+03,
     2.6720e+03, 2.4060e+03, 1.5870e+03, 2.2660e+03, 8.3600e+02,
     1.9340e+03, 3.8200e+02, 1.7670e+03, 1.7800e+02, 1.4600e+03,
     7.7000e+01, 1.1660e+03, 8.1000e+01, 9.4500e+02, 1.0400e+02,
     6.5700e+02, 1.8900e+02, 4.2200e+02, 2.0800e+02, 2.4100e+02,
     2.3700e+02, 7.7000e+01, 2.2200e+02, 2.5000e+01, 1.3600e+02,
     1.0000e+00, 1.0400e+02, 4.8000e+01, 4.1000e+01, 1.0000e+00,
     2.8000e+01, 2.0000e+00, 1.4000e+01, 6.0000e+00, 3.0000e+00,
     4.0000e+00, 2.0000e+00, 2.0000e+00, 1.0000e+00]
)

# original data - 0 cycles included
N_collective_relative_original = np.array(
    [0.0000e+00, 9.1910e+03, 1.2259e+04, 1.6039e+04, 2.8771e+04,
     1.0721e+04, 2.6950e+04, 5.6850e+03, 2.3399e+04, 1.9920e+03,
     1.3976e+04, 2.7170e+03, 8.1860e+03, 2.8400e+03, 4.8300e+03,
     2.6450e+03, 2.6720e+03, 2.4060e+03, 1.5870e+03, 2.2660e+03,
     8.3600e+02, 1.9340e+03, 3.8200e+02, 1.7670e+03, 1.7800e+02,
     1.4600e+03, 7.7000e+01, 1.1660e+03, 8.1000e+01, 9.4500e+02,
     1.0400e+02, 6.5700e+02, 1.8900e+02, 4.2200e+02, 2.0800e+02,
     2.4100e+02, 2.3700e+02, 7.7000e+01, 2.2200e+02, 2.5000e+01,
     1.3600e+02, 1.0000e+00, 1.0400e+02, 0.0000e+00, 4.8000e+01,
     0.0000e+00, 4.1000e+01, 1.0000e+00, 2.8000e+01, 2.0000e+00,
     1.4000e+01, 0.0000e+00, 6.0000e+00, 3.0000e+00, 4.0000e+00,
     2.0000e+00, 0.0000e+00, 2.0000e+00, 0.0000e+00, 1.0000e+00,
     0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00])


i_full_damage = np.array(
    [False, False, False, False, False, False, False, False, False,
     False, False, False, False, False, False, False, False, False,
     False, False, False, False, False, False, False, False, False,
     False, False,  True,  True,  True,  True,  True,  True,  True,
        True,  True,  True,  True,  True,  True,  True,  True,  True,
        True,  True,  True,  True,  True,  True,  True,  True,  True]
)

i_reduced_damage = np.array(
    [True,  True,  True,  True,  True,  True,  True,  True,  True,
        True,  True,  True,  True,  True,  True,  True,  True,  True,
        True,  True,  True,  True,  True,  True,  True,  True,  True,
        True,  True, False, False, False, False, False, False, False,
     False, False, False, False, False, False, False, False, False,
     False, False, False, False, False, False, False, False, False]
)
