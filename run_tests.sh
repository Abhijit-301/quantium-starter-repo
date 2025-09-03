#!/bin/bash

# Stop execution if any command fails
set -e

# Activate the virtual environment (Windows Git Bash path)
source venv/Scripts/activate

# Run the test suite
pytest test_app.py

# Check exit code
if [ $? -eq 0 ]; then
    echo "All tests passed!"
    exit 0
else
    echo "Some tests failed!"
    exit 1
fi

