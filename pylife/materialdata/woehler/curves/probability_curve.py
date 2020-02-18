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

class ProbabilityCurve:
    def __init__(self, fatigue_data, curve_parameters):
        self.fatigue_data = fatigue_data        
        
        self.X = DataValidator.fill_member('X', curve_parameters)
        self.Y = DataValidator.fill_member('Y', curve_parameters)
        self.a = DataValidator.fill_member('a', curve_parameters)
        self.b = DataValidator.fill_member('b', curve_parameters)
        self.T = DataValidator.fill_member('T', curve_parameters)
        self.curve_parameters = curve_parameters 

    def __str__ (self):
        return str(self.curve_parameters)