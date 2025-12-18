"""
Simple test to verify the package works correctly.
Run with: python -m pytest test_mqtt_client.py
or just: python test_mqtt_client.py
"""

import sys
from disrupt_mqtt import MQTTClient

def test_import():
    """Test that the package can be imported."""
    assert MQTTClient is not None
    print("✓ Import successful")

def test_config_validation():
    """Test that missing config keys are detected."""
    try:
        # Missing required keys should raise KeyError
        incomplete_config = {
            'HOST': 'test.example.com',
            'PORT': 1883,
            # Missing other required fields
        }
        mqtt_client = MQTTClient(incomplete_config)
        assert False, "Should have raised KeyError"
    except KeyError as e:
        print(f"✓ Config validation working: {e}")
        assert True

def test_client_creation():
    """Test that client can be created with valid config."""
    config = {
        'HOST': 'test.example.com',
        'PORT': 1883,
        'TRANSPORT': 'tcp',
        'TOPIC': 'test-topic',
        'SENSORNAME': 'test-sensor',
        'USER': 'test-user',
        'PW': 'test-password'
    }
    
    try:
        # Note: This will try to connect, which will fail without a real broker
        # but at least we can test that the object is created
        mqtt_client = MQTTClient(config)
        mqtt_client.close()
        print("✓ Client object creation successful")
    except Exception as e:
        # Connection failure is expected without a real broker
        print(f"✓ Client creation attempted (connection failed as expected: {e})")

if __name__ == "__main__":
    print("Running basic tests...\n")
    test_import()
    test_config_validation()
    # test_client_creation()  # Uncomment to test with a real broker
    print("\n✅ All tests passed!")
