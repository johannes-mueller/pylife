# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 07:28:32 2020

@author: KRD2RNG
"""

import numpy as np
import pandas as pd
from pylife.stress import frequencysignal as fsig

def test_rms_psd():
    psd_nCode = pd.DataFrame([[0,0.05873,0.05099,0.009817],[400,1.265,1.003,0.2959],
                   [800,2.215,2.291,0.7709],[1200,1.407,1.479,0.3021],
                   [1600,1.083,0.6476,0.1402],[2000,0.3998,0.1892,0.139],
                   [2400,0.06213,0.03343,0.02849],[2800,0.01297,0.006958,0.006106],
                   [3200,0.006231,0.005423,0.004105],[3600,0.008619,0.006453,0.005322],
                   [4000,0.0119,0.005596,0.005025],[4400,0.01317,0.004346,0.003961],
                   [4800,0.01143,0.001543,0.002799],[5200,0.007748,5.323E-4,0.001033],
                   [5600,0.005334,2.958E-4,4.617E-4],[6000,0.004206,2.962E-4,8.804E-4],
                   [6400,0.002729,2.179E-4,0.001231]])
    psd_nCode = psd_nCode.set_index(psd_nCode.columns[0])
    rms = fsig.psdSignal.rms_psd(psd_nCode)
    rms.name = 'RMS'
    rms_nCode = pd.Series([51.27226649,47.85658056,26.20561707],name = 'RMS',index = [1,2,3])
    pd.testing.assert_series_equal(rms,rms_nCode, check_less_precise = 1)



def test_psd_smoother():
    psd_df = pd.DataFrame(data = [4,4,2,2,1,1],
                          index = [1,10,10.01,100,100.1,1000])
    f_fine = np.logspace(np.log10(psd_df.index.values.min()),np.log10(
                              psd_df.index.values.max()),1024)
    # Only 1 freq selected:
    test_psd = fsig.psdSignal.psd_smoother(psd_df,[50],0)
    np.testing.assert_almost_equal(max(test_psd.values),2)
    test_psd = fsig.psdSignal.psd_smoother(psd_df,[50],1)
    
    pd.testing.assert_series_equal(fsig.psdSignal.rms_psd(test_psd),
                                    fsig.psdSignal.rms_psd(pd.DataFrame(10**np.interp(f_fine,
                                                                                      psd_df.index.values,
                                                                                      np.log10(psd_df.values.flatten())),
                                                                        index = f_fine)),
                                     check_less_precise = 1)

         
          

test_psd_smoother()
# test_rms_psd()




