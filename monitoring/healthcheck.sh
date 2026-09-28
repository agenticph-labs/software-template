#!/bin/sh
# Docker HEALTHCHECK command for software-template
# Usage in Dockerfile:
#   HEALTHCHECK --interval=30s --timeout=5s --retries=3 \
#     CMD ./monitoring/healthcheck.sh

set -euo pipefail

URL="${HEALTHCHECK_URL:-http://localhost:8000/health}"

response=$(curl -s -o /dev/null -w "%{http_code}" --max-time 5 "$URL" 2>/dev/null)

if [ "$response" = "200" ]; then
    echo "Health check passed (HTTP $response)"
    exit 0
else
    echo "Health check failed (HTTP $response)"
    exit 1
fi
