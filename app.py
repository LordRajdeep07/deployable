"""
Entry point for the Render deployment.
This file imports the Flask server instance from src/app.py

Note: All imports that might cause errors on initial import are
handled inside src/app.py to ensure this file can be imported
without errors.
"""
import os
import sys

# Add the src directory to the path to ensure imports work correctly
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

# Import the server from the src package
from src.app import server

# This is what Gunicorn will use
app = server

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8050))) 