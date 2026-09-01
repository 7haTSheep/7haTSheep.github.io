#!/bin/bash
# Double-click this on a Mac to preview the site at http://localhost:8080
cd "$(dirname "$0")"
echo "Serving at http://localhost:8080  —  press Ctrl+C to stop"
(sleep 1 && open http://localhost:8080) &
python3 -m http.server 8080
