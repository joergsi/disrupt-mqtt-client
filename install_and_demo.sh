#!/bin/bash
# Installation and demonstration script for disrupt-mqtt-client

set -e  # Exit on error

echo "=================================================="
echo "  Disrupt MQTT Client - Installation & Demo"
echo "=================================================="
echo ""

# Get the directory where the script is located
PACKAGE_DIR="/home/uu878/disrupt/disrupt-mqtt-client"

echo "📦 Step 1: Installing package dependencies..."
pip install paho-mqtt>=1.6.0

echo ""
echo "📦 Step 2: Installing disrupt-mqtt-client package..."
pip install -e "$PACKAGE_DIR"

echo ""
echo "✅ Installation complete!"
echo ""

echo "🧪 Step 3: Testing the installation..."
python3 << 'EOF'
try:
    from disrupt_mqtt import MQTTClient
    print("  ✓ Package import successful!")
    print("  ✓ MQTTClient class available")
    print("")
    print("Package version:", MQTTClient.__module__)
except ImportError as e:
    print(f"  ✗ Import failed: {e}")
    exit(1)
EOF

echo ""
echo "=================================================="
echo "  ✅ Installation Successful!"
echo "=================================================="
echo ""
echo "📖 Next Steps:"
echo ""
echo "1. View documentation:"
echo "   cat $PACKAGE_DIR/PACKAGE_INFO.md"
echo ""
echo "2. Check examples:"
echo "   ls -la $PACKAGE_DIR/examples/"
echo ""
echo "3. Test with your config:"
echo "   cd $PACKAGE_DIR/examples"
echo "   # Edit config.yaml with your credentials"
echo "   python example_basic.py"
echo ""
echo "4. Use in your projects:"
echo "   # In your Python code:"
echo "   from disrupt_mqtt import MQTTClient"
echo ""
echo "=================================================="
