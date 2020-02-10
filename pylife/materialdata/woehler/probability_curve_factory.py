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

from pylife.materialdata.woehler.probability_curve_creator_finite import ProbabilityCurveCreatorFinite
from pylife.materialdata.woehler.probability_curve_creator_infinite import ProbabilityCurveCreatorInfinite

class ProbabilityCurveFactory:
    def __init__(self, fatigue_data):
        self.probability_curve_creator_finite = ProbabilityCurveCreatorFinite(fatigue_data)
        self.probability_curve_creator_infinite = ProbabilityCurveCreatorInfinite(fatigue_data)
    
    def create_probability_curve_finite(self):
        return self.probability_curve_creator_finite.create_probability_curve()

    def create_probability_curve_infinite(self):
        return self.probability_curve_creator_infinite.create_probability_curve()
        

    