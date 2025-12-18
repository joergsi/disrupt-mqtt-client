# Installation
```bash
# Step 1: Install dependencies
pip install paho-mqtt>=1.6.0

# Step 2: Install the package
pip install -e /home/uu878/disrupt/disrupt-mqtt-client

# Or use the provided installation script:
bash /home/uu878/disrupt/disrupt-mqtt-client/install_and_demo.sh
```

# config.yaml
```yaml
HOST: "city.app.sdk-cloud.de"
PORT: 443
TRANSPORT: "websockets"
TOPIC: "MQTT Ingest Topic"
USER: "MQTT User"
PW: "MQTT Password"
SENSORNAME: "MQTT Sensor Name"
```

# Configuration Parameters
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `HOST` | string | Yes | MQTT broker hostname |
| `PORT` | integer | Yes | MQTT broker port (443 for WSS, 1883 for TCP) |
| `TRANSPORT` | string | Yes | Transport protocol: `"websockets"` or `"tcp"` |
| `TOPIC` | string | Yes | Base topic UUID from Disrupt platform |
| `SENSORNAME` | string | Yes | Sensor identifier (appended to topic) |
| `USER` | string | Yes | Authentication username (UUID) |
| `PW` | string | Yes | Authentication password |

# Usage Example
```python
import yaml
from disrupt_mqtt import MQTTClient  # ← Only change needed!

# Load your existing config file
with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f)

# Publish
mqtt_client = MQTTClient(config)
mqtt_client.publish({
    "tracking_id": 1,
    "class_id": 2, 
    "time": "2024-10-22T10:25:26+02",
    "long": 11.4253, 
    "lat": 48.7751
    })
mqtt_client.close()
```

See the `examples/` directory for complete working examples:
- `example_basic.py` - Basic usage example
- `example_context_manager.py` - Using context manager
- `example_from_kafka.py` - Publishing from Kafka consumer
- `example_batch_publish.py` - Publishing multiple messages

# class_id
- `-1`: Unknown
- `0`: Pedestrian
- `1`: Bicycle
- `2`: Car
- `3`: Motorcycle
- `5`: Bus
- `7`: Truck
- `10`: E-scooter
