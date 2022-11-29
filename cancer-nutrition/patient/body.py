from ._protocol import PatientInfoProtocol
from ..utils.measurement import BMI, ZScore


class Body(PatientInfoProtocol):
    _tgt_keys = ["age", "weight", "height"]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bmi = BMI.compute()  # FIXME: add parameters
        self.z_score = ZScore.compute()  # FIXME: add parameters
