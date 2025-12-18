from pathlib import Path
from setuptools import setup, find_packages

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="disrupt-mqtt-client",
    version="0.1.0",
    author="joergsi",
    author_email="joergsi@users.noreply.github.com",
    description="MQTT client for the Disrupt/SDK mobility data platform",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/joergsi/disrupt-mqtt-client",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Networking",
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
        "Bug Reports": "https://github.com/joergsi/disrupt-mqtt-client/issues",
        "Source": "https://github.com/joergsi/disrupt-mqtt-client",
        "Documentation": "https://github.com/joergsi/disrupt-mqtt-client#readme",
    },
)
