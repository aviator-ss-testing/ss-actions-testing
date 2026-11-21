#!/bin/bash
set -euo pipefail

echo "Starting status site on port 8080..."
PORT=8080 nohup python3 status_server.py > /tmp/preview-server.log 2>&1 &

echo "Preview server started."
