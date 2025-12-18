"""
Example: Publishing batch data from a file or data source.

This example demonstrates:
- Reading multiple data points
- Publishing them in a batch
- Error handling for individual publishes
"""

import yaml
import json
from disrupt_mqtt import MQTTClient

def load_sample_data():
    """Simulate loading data from a file or database."""
    return [
        {
            "measurements": [{
                "tracking_id": 2001,
                "time": "2024-12-18T10:30:00.000000+01:00",
                "lat": 48.7758,
                "long": 11.4297,
                "class_id": 2,
                "velocity_ms": 12.5,
                "data": {"sensor_id": "sensor_001"}
            }]
        },
        {
            "measurements": [{
                "tracking_id": 2001,
                "time": "2024-12-18T10:30:01.000000+01:00",
                "lat": 48.7759,
                "long": 11.4298,
                "class_id": 2,
                "velocity_ms": 13.3,
                "data": {"sensor_id": "sensor_001"}
            }]
        },
        {
            "measurements": [{
                "tracking_id": 2001,
                "time": "2024-12-18T10:30:02.000000+01:00",
                "lat": 48.7760,
                "long": 11.4299,
                "class_id": 2,
                "velocity_ms": 13.9,
                "data": {"sensor_id": "sensor_001"}
            }]
        },
    ]

# Load configuration
with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f)

# Load data to publish
data_batch = load_sample_data()
print(f"Loaded {len(data_batch)} records to publish")

# Publish all data
published_count = 0
failed_count = 0

with MQTTClient(config) as mqtt_client:
    for idx, data in enumerate(data_batch, 1):
        print(f"Publishing record {idx}/{len(data_batch)}...", end=" ")
        
        if mqtt_client.publish(data):
            published_count += 1
            print("✓")
        else:
            failed_count += 1
            print("✗")

print("\n" + "="*50)
print(f"Results:")
print(f"  ✓ Published: {published_count}")
print(f"  ✗ Failed: {failed_count}")
print(f"  Total: {len(data_batch)}")
