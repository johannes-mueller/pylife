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

from pylife.materialdata.woehler.woehler_curve import WoehlerCurve

class WoehlerCurveWithFixedParams(WoehlerCurve): 
    def __init__(self, fatigue_data, curve_parameters, p_opt, param_fix):
        super().__init__(fatigue_data, curve_parameters)
        self.p_opt = p_opt
        self.param_fix = param_fix