
# TODO: *actually* get devices ;-)

def get_devices():
    return [
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
