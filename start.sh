#!/bin/bash

# Make venv
python -m venv venv

# Switch to venv
source venv/bin/activate

# Install packages
pip install requirements

# Run
python3 server.py