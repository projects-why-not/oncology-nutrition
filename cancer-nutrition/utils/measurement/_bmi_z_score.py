from ._protocol import MeasurementUtilProtocol


class BMI(MeasurementUtilProtocol):
    _required_keys = ["weight", "height"]

    @classmethod
    def compute(cls, **kwargs):
        cls._assert_keys(list(kwargs.keys()))
        w = kwargs["weight"]["kg"]
        h = kwargs["height"]["m"]
        bmi = w / (h * h)

        # TODO: discretize value
        bmi_class = None

        return bmi, bmi_class


class ZScore(MeasurementUtilProtocol):
    _required_keys = ["age", "BMI"]

    @classmethod
    def compute(cls, **kwargs):
        cls._assert_keys(list(kwargs.keys()))

        # TODO: operate with tables
