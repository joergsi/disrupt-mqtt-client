"""
MQTT Client for Disrupt/SDK Platform.

This module provides a client for publishing mobility data to the Disrupt/SDK platform
via MQTT. It supports both TCP and WebSocket transports with TLS encryption.
"""

import paho.mqtt.client as mqtt
import json
import logging
from typing import Dict, Any, Optional, Union

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class MQTTClient:
    """
    MQTT Client for publishing data to the Disrupt/SDK platform.
    
    Attributes:
        host (str): MQTT broker hostname
        port (int): MQTT broker port
        topic (str): MQTT topic for publishing (constructed from TOPIC/SENSORNAME)
        transport (str): Transport protocol ('tcp' or 'websockets')
        client: Paho MQTT client instance
    
    Example:
        >>> config = {
        ...     'HOST': 'city.app.sdk-cloud.de',
        ...     'PORT': 443,
        ...     'TRANSPORT': 'websockets',
        ...     'TOPIC': 'MQTT Ingest Topic',
        ...     'SENSORNAME': 'MQTT Sensor Name',
        ...     'USER': 'MQTT User',
        ...     'PW': 'MQTT Password'
        ... }
        >>> mqtt_client = MQTTClient(config)
        >>> mqtt_client.publish({'timestamp': 1234567890, 'value': 42})
        >>> mqtt_client.close()
    """
    
    def __init__(self, config: Dict[str, Any]):
        """
        Initialize the MQTT client.
        
        Args:
            config (dict): Configuration dictionary containing:
                - HOST (str): MQTT broker hostname
                - PORT (int): MQTT broker port
                - TRANSPORT (str): 'tcp' or 'websockets'
                - TOPIC (str): Base topic UUID
                - SENSORNAME (str): Sensor identifier (appended to topic)
                - USER (str): Authentication username
                - PW (str): Authentication password
        
        Raises:
            KeyError: If required configuration keys are missing
            Exception: If connection to broker fails
        """
        # Validate required config keys
        required_keys = ['HOST', 'PORT', 'TRANSPORT', 'TOPIC', 'SENSORNAME', 'USER', 'PW']
        missing_keys = [key for key in required_keys if key not in config]
        if missing_keys:
            raise KeyError(f"Missing required configuration keys: {', '.join(missing_keys)}")
        
        self.host = config['HOST']
        self.port = config['PORT']
        self.topic = f"{config['TOPIC']}/{config['SENSORNAME']}"
        self.transport = config['TRANSPORT']
        
        logger.info(f"Initializing MQTT client for {self.host}:{self.port} (transport: {self.transport})")
        
        # Create MQTT client
        self.client = mqtt.Client(transport=self.transport)
        
        # Configure WebSocket-specific settings
        if self.transport == "websockets":
            self.client.ws_set_options(path="/mqtt")
            self.client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)
        
        # Set authentication
        self.client.username_pw_set(config['USER'], config['PW'])
        
        # Set up callbacks for better error handling
        self.client.on_connect = self._on_connect
        self.client.on_disconnect = self._on_disconnect
        self.client.on_publish = self._on_publish
        
        # Connect to broker
        try:
            self.client.connect(self.host, self.port, 60)
            self.client.loop_start()
            logger.info(f"Connected to MQTT broker at {self.host}:{self.port}")
        except Exception as e:
            logger.error(f"Failed to connect to MQTT broker: {e}")
            raise
    
    def _on_connect(self, client, userdata, flags, rc):
        """Callback for when the client receives a CONNACK response from the server."""
        if rc == 0:
            logger.info("Successfully connected to MQTT broker")
        else:
            logger.error(f"Connection failed with code {rc}")
    
    def _on_disconnect(self, client, userdata, rc):
        """Callback for when the client disconnects from the broker."""
        if rc != 0:
            logger.warning(f"Unexpected disconnection (code: {rc})")
    
    def _on_publish(self, client, userdata, mid):
        """Callback for when a message is published."""
        logger.debug(f"Message {mid} published successfully")
    
    def publish(self, payload: Union[Dict[str, Any], list], indent: Optional[int] = 2) -> bool:
        """
        Publish data to the MQTT broker.
        
        Args:
            payload (dict or list): Data to publish (will be JSON-serialized)
            indent (int, optional): JSON indentation for readability. Defaults to 2.
        
        Returns:
            bool: True if publish was successful, False otherwise
        
        """
        try:
            json_payload = json.dumps(payload, indent=indent)
            result = self.client.publish(self.topic, json_payload)
            
            if result.rc == mqtt.MQTT_ERR_SUCCESS:
                logger.debug(f"Published to {self.topic}")
                return True
            else:
                logger.error(f"Publish failed with code {result.rc}")
                return False
        except Exception as e:
            logger.error(f"Error publishing message: {e}")
            return False
    
    def close(self):
        """
        Close the MQTT connection gracefully.
        
        Should be called when done publishing to ensure proper cleanup.
        """
        logger.info("Closing MQTT connection")
        self.client.loop_stop()
        self.client.disconnect()
    
    def __enter__(self):
        """Context manager entry."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit - ensures connection is closed."""
        self.close()
