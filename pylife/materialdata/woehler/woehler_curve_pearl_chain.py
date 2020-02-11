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

from pylife.core.data_validator import DataValidator
import numpy as np

class WoehlerCurvePearlChain:

    def __init__(self, curve_parameters, fatigue_data = None):
        self.fatigue_data = fatigue_data
        self.k = DataValidator.fill_member('k_1', curve_parameters)
        self.TS = DataValidator.fill_member('1/TS', curve_parameters)
        self.TN = DataValidator.fill_member('1/TN', curve_parameters)
        self.curve_parameters = curve_parameters

    def __str__ (self):
        return str(self.curve_parameters)