"""
Context manager example for disrupt-mqtt-client.

Using the context manager ensures the connection is properly closed
even if an error occurs.
"""

import yaml
import time
from disrupt_mqtt import MQTTClient

# Load configuration
with open('config.yaml', 'r') as f:
    config = yaml.safe_load(f)

# Use context manager - connection will be closed automatically
with MQTTClient(config) as mqtt_client:
    
    # Simulate sensor readings
    for i in range(5):
        from datetime import datetime
        
        data = {
            "measurements": [{
                "tracking_id": 1001,
                "time": datetime.now().isoformat(),
                "lat": round(48.7758 + (i * 0.0001), 6),  # Slightly moving position
                "long": round(11.4297 + (i * 0.0001), 6),
                "class_id": 2,  # Car
                "heading": 90.0,
                "velocity_ms": round(13.9 + (i * 0.5), 2),  # Increasing speed
                "data": {
                    "reading_number": i + 1
                }
            }]
        }
        
        print(f"Publishing reading {i+1}/5...")
        mqtt_client.publish(data)
        time.sleep(1)  # Wait 1 second between readings
    
    print("✓ All readings published successfully!")

# Connection is automatically closed here
print("Context manager exited, connection closed")
