[![PyPI version](https://badge.fury.io/py/pygenieacs.svg)](https://pypi.org/project/pygenieacs/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# pygenieacs

A Python **async** API client for [GenieACS](https://genieacs.com) — a TR-069 / CWMP Auto-Configuration Server.  
This library provides a simple interface to interact with the GenieACS **REST API** asynchronously.

---

## ✨ Features
- List, inspect, and delete devices
- Run tasks (reboot, factory reset, firmware upgrade, etc.)
- Manage presets
- Manage provisions
- Fully async, Pythonic interface

---

## 📦 Installation

```python
pip install pygenieacs
```
🚀 Usage
Initialize Client
```python

import asyncio
from pygenieacs import GenieACSClient, DevicesAPI, TasksAPI

async def main():
    async with GenieACSClient(base_url="http://localhost:7557") as client:
        devices = DevicesAPI(client)
        tasks = TasksAPI(client)

        # List devices
        all_devices = await devices.list()
        print(all_devices)

        # Get a specific device
        device_id = "001A2B3C4D"
        info = await devices.get(device_id)
        print(info)

        # Reboot a device
        await tasks.add(device_id, "reboot")

asyncio.run(main())
```
⚙️ Advanced

```python

from pygenieacs import PresetsAPI

async def create_presets(client):
    presets = PresetsAPI(client)

    # Apply to all devices
    await presets.create("daily-reboot", {
        "weight": 0,
        "precondition": "true",
        "configurations": [
            {"parameter": "InternetGatewayDevice.ManagementServer.PeriodicInformInterval", "value": "60"}
        ]
    })

    # Apply only to MikroTik devices
    await presets.create("mikrotik-provision", {
        "weight": 1,
        "precondition": "DeviceId.Manufacturer == 'MikroTik'",
        "configurations": [],
        "provisions": ["default-config"],
    })

    # Apply firmware upgrade if version < 6.48
    await presets.create("firmware-upgrade", {
        "weight": 10,
        "precondition": "Device.DeviceInfo.SoftwareVersion < '6.48'",
        "configurations": [],
        "provisions": ["upgrade-firmware"],
    })

    # Apply to devices with specific OUI
    await presets.create("oui-target", {
        "weight": 5,
        "precondition": "DeviceId.OUI == '001A2B'",
        "configurations": [
            {
                "parameter": "InternetGatewayDevice.LANDevice.1.LANHostConfigManagement.DHCPServerEnable",
                "value": False
            }
        ],
        "provisions": [],
    })
```
Provisions
```python

from pygenieacs import ProvisionsAPI

async def create_provision(client):
    provisions = ProvisionsAPI(client)

    # Ensure Inform Interval is set and default Wi-Fi SSID exists
    script = """
    let interval = declare("InternetGatewayDevice.ManagementServer.PeriodicInformInterval", {value: 1});
    if (interval.value[0] != 300) {
      declare("InternetGatewayDevice.ManagementServer.PeriodicInformInterval", null, {value: 300});
    }

    let ssid = declare("InternetGatewayDevice.LANDevice.1.WLANConfiguration.1.SSID", {value: 1});
    if (!ssid.value[0]) {
      declare("InternetGatewayDevice.LANDevice.1.WLANConfiguration.1.SSID", null, {value: "MyDefaultSSID"});
    }
    """

    await provisions.create("default-config", script)
```
🛠 Development
Clone the repo and install locally:
```python
git clone https://github.com/uberkie/pygenieacs.git
cd pygenieacs
pip install -e .
```
Run tests:
```python
pytest
```