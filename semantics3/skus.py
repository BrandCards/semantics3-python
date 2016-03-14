try:
    from .semantics3 import Semantics3Request
except ImportError:
    from semantics3 import Semantics3Request

class Skus(Semantics3Request):
    def __init__(self, api_key, api_secret, api_base='https://api.semantics3.com/v1/'):
        Semantics3Request.__init__(self, api_key, api_secret, 'skus', api_base)

    def get_skus(self):
        return self.get()

    def skus_field(self, *field):
        return self.field(*field)