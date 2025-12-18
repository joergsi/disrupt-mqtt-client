from setuptools import setup, find_packages

with open("readme.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="disrupt-mqtt-client",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="MQTT client for the Disrupt/SDK mobility data platform",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/disrupt-mqtt-client",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Networking",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
    install_requires=[
        "paho-mqtt>=1.6.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pytest-cov>=4.0",
            "black>=23.0",
            "flake8>=6.0",
        ],
    },
    keywords="mqtt, mobility, disrupt, sdk, iot, sensor data",
    project_urls={
        "Bug Reports": "https://github.com/yourusername/disrupt-mqtt-client/issues",
        "Source": "https://github.com/yourusername/disrupt-mqtt-client",
        "Documentation": "https://github.com/yourusername/disrupt-mqtt-client#readme",
    },
)
