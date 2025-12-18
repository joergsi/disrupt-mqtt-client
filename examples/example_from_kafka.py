"""
Example: Publishing data from a Kafka consumer to MQTT.

This simulates how the package is used in the gevas-kafka project.
Note: This requires kafka-python to be installed separately.
"""

import yaml
import time
from disrupt_mqtt import MQTTClient

# Simulated Kafka message processing
def simulate_kafka_consumer():
    """Simulate receiving messages from Kafka."""
    from datetime import datetime
    
    messages = [
        {
            "measurements": [{
                "tracking_id": 5001,
                "time": datetime.now().isoformat(),
                "lat": 48.7758,
                "long": 11.4297,
                "class_id": 5,  # Bus
                "velocity_ms": 12.5,
                "heading": 180.0,
                "data": {
                    "vid": "BUS_001",
                    "bus_no": 1
                }
            }]
        },
        {
            "measurements": [{
                "tracking_id": 2042,
                "time": datetime.now().isoformat(),
                "lat": 48.7759,
                "long": 11.4298,
                "class_id": 2,  # Car
                "velocity_ms": 16.7,
                "heading": 90.0,
                "data": {
                    "vid": "CAR_042"
                }
            }]
        },
    ]
    return messages

def main():
    # Load configuration
    with open('config.yaml', 'r') as f:
        config = yaml.safe_load(f)
    
    # Initialize MQTT client
    with MQTTClient(config) as mqtt_client:
        print("Started processing Kafka messages...")
        print("Press Ctrl+C to stop\n")
        
        try:
            # In real scenario, this would be an infinite loop
            # consuming from Kafka
            for _ in range(3):  # Simulate 3 rounds of messages
                messages = simulate_kafka_consumer()
                
                for msg in messages:
                    vehicle_id = msg["measurements"][0]["data"].get("vid", "unknown")
                    print(f"Processing vehicle: {vehicle_id}")
                    mqtt_client.publish(msg)
                
                time.sleep(2)  # Wait before next batch
                
        except KeyboardInterrupt:
            print("\nStopping consumer...")
    
    print("✓ Consumer stopped, MQTT connection closed")

if __name__ == "__main__":
    main()
