# from .unit_util import UnitUtil
# from .proxy_base import ProxyBase
# from .fitness_device_feedback import FitnessDeviceFeedback
# from .fitness_device_listener import FitnessDeviceListenerBase
# from .fitness_device import FitnessDevice
# from .fitnes_device_proxy import FitnessDeviceProxy
# from .fitness_device_sync_manager import FitnessDeviceSyncManager
# import inspect
#
#
# def register_proxy(name, cls, proxy):
#     for attr in dir(cls):
#         if inspect.ismethod(getattr(cls, attr)) and not attr.startswith("__"):
#             proxy._exposed_ += (attr,)
#             setattr(proxy, attr,
#                     lambda s: object.__getattribute__(s, '_callmethod')(attr))
#     FitnessDeviceSyncManager.register(name, cls, proxy)
#
# register_proxy('fitness_device', FitnessDevice, FitnessDeviceProxy)
