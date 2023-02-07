from mqt.predictor.devices.calibration import DeviceCalibration
from mqt.predictor.devices.device import Device
from mqt.predictor.devices.provider import Provider
from mqt.predictor.devices.ibm import IBMProvider
from mqt.predictor.devices.ionq import IonQProvider
from mqt.predictor.devices.oqc import OQCProvider
from mqt.predictor.devices.rigetti import RigettiProvider


def get_available_providers() -> list[Provider]:
    """
    Get a list of all available providers
    """
    return [IBMProvider(), IonQProvider(), OQCProvider(), RigettiProvider()]


def get_available_devices(sanitize_device: bool = False) -> list[Device]:
    """
    Get a list of all available devices

    Args:
        sanitize_device: whether to sanitize the device calibration data
    """
    return [
        dev for prov in get_available_providers() for dev in prov.get_available_devices(sanitize_device=sanitize_device)
    ]


def get_available_device_names() -> list[str]:
    """
    Get a list of all available device names
    """
    return [name for prov in get_available_providers() for name in prov.get_available_device_names()]


__all__ = [
    "Provider",
    "Device",
    "DeviceCalibration",
    "IBMProvider",
    "IonQProvider",
    "OQCProvider",
    "RigettiProvider",
    "get_available_providers",
    "get_available_devices",
    "get_available_device_names",
]
