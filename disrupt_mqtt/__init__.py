"""
Disrupt MQTT Client - A Python package for connecting to the Disrupt/SDK mobility data platform.

This package provides a simple interface to publish mobility data to the 
city.app.sdk-cloud.de (formerly disrupt.sdk.efs.ai) MQTT broker.
"""

from .mqtt_client import MQTTClient

__version__ = "0.1.0"
__all__ = ["MQTTClient"]
