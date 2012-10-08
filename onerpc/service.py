from zerorpc import Client
import imp


_SERVICES_LOC = {}


class Service(object):
    def __init__(self, name):
        location = _SERVICES_LOC.get(name)
        if location is not None:
            self.client = Client()
            self.client.connect(location)
        else:
            # direct import
            self.client = None
            self._mod = imp.load_module(name, *imp.find_module(name))

    def __getattr__(self, name):
        return self._runner(name)

    def _runner(self, name):
        def __runner(*args):
            if self.client is not None:
                return self.client(name, *args)
            else:
                return getattr(self._mod, name)(*args)
        return __runner


def locate_service(name, location):
    _SERVICES_LOC[name] = location
