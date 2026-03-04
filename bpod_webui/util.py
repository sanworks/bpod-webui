from pathlib import Path
from typing import Optional

from platformdirs import user_config_dir

from bpod_core.bpod import discover_remote_bpod
from bpod_core.misc import SettingsDict


def get_settings_path():
    """ returns our platform-independent settings path """
    return Path(user_config_dir('bpod-webui'))


def get_settings() -> SettingsDict:
    """ returns our settings as a Bpod SettingsDict object """
    return SettingsDict(get_settings_path() / "settings.json")


def get_network_devices() -> list[dict]:
    _devices = []
    for event_type, address, properties in discover_remote_bpod(local=True, remote=True, timeout=5, poll_interval=.5):
        match event_type:
            case 'added':
                _devices.append({
                    'address': address,
                    'serial': properties.get('serial', '') or '',
                    'name': properties.get('name', '') or '',
                    'description': properties.get('description', '') or '',
                    'location': properties.get('location', '') or '',
                    'firmware': properties.get('firmware', '') or '',
                    'core': properties.get('core', '') or '',
                })
    return _devices


def get_example_devices(device_id:Optional[str]=None) -> list|dict|None:
    """ if no `device_id` is passed, returns a list of example bpod device dicts
    including various types and states of device;
    if a `device_id` is passed, returns the corresponding device dict or None  """
    _devices = [
        {
            "id": "bpod-01",
            "name": "Bpod State Machine r2.5",
            "status": "running",
            "ip": "192.168.1.101",
            "protocol": "Deary-Liewald task",
            "session": 2,
            "trials": 400,
            "operant": "M042",
            "ports": {
                "behavior": [1, 0, 0, 1],
                "module": [1, 0, 1, 1, 1]
            }
        },
        {
            "id": "bpod-02",
            "name": "Bpod State Machine 2+",
            "status": "online",
            "ip": "192.168.1.102",
            "protocol": "2AFC Training",
            "session": 2,
            "trials": 3,
            "operant": "Felix-7",
            "ports": {
                "behavior": [1, 1, 1, 1, 0],
                "module": [1, 0, 0]
            }
        },
        {
            "id": "bpod-03",
            "name": "Bpod State Machine r1",
            "status": "offline",
            "ip": "192.168.1.103",
            "protocol": None,
            "session": None,
            "trials": None,
            "operant": None,
            "ports": {
                "behavior": [1, 0, 0, 1, 1, 0, 0, 0],
                "module": [1, 0, 1]
            }
        },
        {
            "id": "bpod-04",
            "name": "Bpod State Machine r2.5",
            "status": "running",
            "ip": "192.168.1.104",
            "protocol": "Go / No-Go task",
            "session": 42,
            "trials": 156,
            "operant": "Whiskers",
            "ports": {
                "behavior": [1, 0, 0, 1],
                "module": [1, 0, 1, 1, 1]
            }
        },
        {
            "id": "bpod-05",
            "name": "Bpod State Machine r2.5",
            "status": "running",
            "ip": "192.168.1.105",
            "protocol": "Dot probe task",
            "session": 55,
            "trials": 78,
            "operant": "C57-003",
            "ports": {
                "behavior": [1, 0, 0, 1],
                "module": [1, 0, 1, 1, 1]
            }
        },
        {
            "id": "bpod-06",
            "name": "Bpod State Machine r2.5",
            "status": "crashed",
            "ip": "192.168.1.106",
            "protocol": "Spatial WM task",
            "session": 12,
            "trials": 89,
            "operant": "B6-Alpha",
            "ports": {
                "behavior": [1, 0, 1, 1],
                "module": [1, 1, 1, 0, 1]
            }
        }
    ]
    if device_id is None:
        return _devices
    return next(iter([device for device in _devices if device['id'] == device_id]), None)
