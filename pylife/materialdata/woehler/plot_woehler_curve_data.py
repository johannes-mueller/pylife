# Copyright (c) 2019 - for information on the respective copyright owner
# see the NOTICE file and/or the repository
# https://github.com/boschresearch/pylife
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

__author__ = "Mustapha Kassem"
__maintainer__ = "Johannes Mueller"

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy import stats
from pylife.materialdata.woehler.woehler_curve_graph import WoehlerCurveGraph
from pylife.materialdata.woehler.whole_woehler_curve import WholeWoehlerCurve

class PlotWoehlerCurveData:
    def __init__(self, woehler_curve, y_min = None, y_max = None, ax = None):
        self.woehler_curve = woehler_curve
        self.y_min = self.woehler_curve.fatigue_data.loads_min*0.8 if y_max == None else y_max
        self.y_max = self.woehler_curve.fatigue_data.loads_max*1.2 if y_min == None else y_min
        self.xlim_WL = (round(min(self.woehler_curve.fatigue_data.data.cycles)*0.4,-1), round(max(self.woehler_curve.fatigue_data.data.cycles)*2,-1))
        self.ylim_WL = (round(min(self.woehler_curve.fatigue_data.data.loads)*0.8,-1), round(max(self.woehler_curve.fatigue_data.data.loads)*1.2,-1)) 
        self.ax = self.__default_ax_config() if ax == None else ax

    def __default_ax_config(self):
        fig, ax = plt.subplots()
        #need setter for the title
        #ax.set_title('Initial data')
        ax.set_xlim(self.xlim_WL)
        ax.set_ylim(self.ylim_WL)
        ax.set_xscale('log')
        ax.set_yscale('log')
        ax.grid(True)
        ax.set_xlabel('Number of cycles', fontsize = 11)
        ax.set_ylabel('Amplitude' + ' (' + 'Stress' +') in ' + '$N/mm^2$' + '(log scaled)')
        fig.tight_layout()
        matplotlib.rcParams.update({'font.size': 11})
        return ax


    def plot_basic_fatigue_data(self):
        self.ax.plot(self.woehler_curve.fatigue_data.runouts.cycles, self.woehler_curve.fatigue_data.runouts.loads, 'bo', mfc='none', label='Runout')   
        self.ax.plot(self.woehler_curve.fatigue_data.fractures.cycles, self.woehler_curve.fatigue_data.fractures.loads, 'bo', label='Failure')
        self.ax.legend(loc='upper right', fontsize=11)
        return self

    def plot_endurance_limit(self):
        self.ax.axhline(y=self.woehler_curve.fatigue_data.fatg_lim, linewidth=2, color='r', label='Endurance limit') 

    def plot_woehler_curve(self):
        woehler_curve_graph = WoehlerCurveGraph(self.woehler_curve, self.y_min, self.y_max)
        self.ax.plot(woehler_curve_graph.points[:,1], woehler_curve_graph.points[:,0], color='r', linewidth=2., label=u'WL, $P_A$=50%')
        self.ax.legend(loc='upper right', fontsize=11)
        return self
    
    def plot_pearl_chain_method(self):
        fatigue_data = self.woehler_curve.fatigue_data
        self.ax.plot(fatigue_data.N_shift, np.ones(len(fatigue_data.N_shift))*fatigue_data.Sa_shift,
                    'go',label='PCM shifted probes', marker="v")
        self.ax.plot(self.xlim_WL, np.ones(len(self.xlim_WL))*fatigue_data.Sa_shift,'g')
        self.ax.legend(loc='upper right', fontsize=11)
        return self
        
    
    def plot_deviation(self):
        woehler_curve_graph = WoehlerCurveGraph(self.woehler_curve, self.y_min, self.y_max)
        self.ax.plot(woehler_curve_graph.calc_shifted_woehlercurve_points(0.1)[:, 1],
                woehler_curve_graph.points[:, 0], 'r', linewidth=1.5,
                linestyle='--', label=u'WL, $P_A$=10% u. 90%')
        self.ax.plot(woehler_curve_graph.calc_shifted_woehlercurve_points(0.9)[:, 1],
                woehler_curve_graph.points[:, 0], 'r', linewidth=1.5, 
                linestyle='--')
        text = '$k$ = '+str(np.round(self.woehler_curve.k, decimals=2)) + '\n'
        text += '$1/T_N$ = ' + str(np.round(self.woehler_curve.TN, decimals=2)) + '\n'
        text += '$1/T_S^*$ = ' + str(np.round(self.woehler_curve.TS, decimals=2))

        self.ax.text(0.01, 0.03, text, verticalalignment='bottom',
                    horizontalalignment='left', transform=self.ax.transAxes,
                    bbox={'facecolor': 'grey', 'alpha': 0.2, 'pad': 10})                
        self.ax.legend(loc='upper right', fontsize=11)
        return self

    def plot_whole_woehler_curve_graph(self, k_2):
        whole_woehler_curve_graph = WholeWoehlerCurve(self.woehler_curve, k_2, self.y_min, self.y_max)
        WL_50 = whole_woehler_curve_graph.graph_50
        WL_10 = whole_woehler_curve_graph.graph_10
        WL_90 = whole_woehler_curve_graph.graph_90
        self.ax.plot(WL_50[:, 1], WL_50[:, 0], 'r', linewidth=2., label=u'WC, $P_A$=50%')
        self.ax.plot(WL_10[:, 1], WL_10[:, 0], 'r', linewidth=1.5, linestyle='--', label=u'WC, $P_A$=10% u. 90%')
        self.ax.plot(WL_90[:, 1], WL_90[:, 0], 'r', linewidth=1.5, linestyle='--')
        self.ax.legend(loc='upper right', fontsize=11)

        text = '$k_1$ = '+str(np.round(self.woehler_curve.k,decimals=2)) + '\n'
        text += '$k_2$ = '+str(np.round(k_2,decimals=2)) + '\n'
        text += '$1/T_N$ = ' + str(np.round(self.woehler_curve.TN,decimals=2)) + '\n'
        text += '$1/T_S^*$ = ' + str(np.round(self.woehler_curve.TN**(1./self.woehler_curve.k), decimals=2)) + '\n'
        text += '$S_{D,50}$ = ' + str(np.round(self.woehler_curve.SD_50,decimals=1)) + '\n'
        text += '$N_{D,50}$ = ' + '{:1.2e}'.format(self.woehler_curve.ND_50) + '\n'
        text += '$1/T_S$ = ' + str(np.round(self.woehler_curve.TS,decimals=2))

        self.ax.text(0.01, 0.03, text,
                 verticalalignment='bottom',horizontalalignment='left',
                 transform=self.ax.transAxes, bbox={'facecolor':'grey', 'alpha':0.2, 'pad':10})       
        return self

    def plot_slope(self):
        text = '$k$ = '+str(np.round(k, decimals=2))
        self.ax.text(0.01, 0.03, text, verticalalignment='bottom', 
            horizontalalignment='left', transform=self.ax.transAxes, 
            bbox={'facecolor': 'grey', 'alpha': 0.2, 'pad': 10})
        self.plot_basic_fatigue_data()
        self.plot_woehler_curve()
        return self

