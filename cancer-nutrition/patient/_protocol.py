
class PatientInfoProtocol:
    _tgt_keys = None

    def __init__(self, **kwargs):
        for key in self._tgt_keys:
            setattr(self, key, kwargs.get(key, None))

    def get_allowed_keys(self):
        return self._tgt_keys
