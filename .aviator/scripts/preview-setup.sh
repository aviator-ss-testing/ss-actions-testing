#!/bin/bash
set -euo pipefail

echo "Starting preview server on port 8080..."
nohup python3 -m http.server 8080 > /tmp/preview-server.log 2>&1 &

echo "Preview server started."
