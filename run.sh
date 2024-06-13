#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Run tests in parallel
pytest -n 2 tests/
