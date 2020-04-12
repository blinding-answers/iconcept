from multiprocessing.managers import NamespaceProxy
class ProxyBase(NamespaceProxy):
    _exposed_ = ('__getattribute__', '__setattr__', '__delattr__')
