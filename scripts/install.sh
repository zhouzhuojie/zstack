#!/usr/bin/env bash
# Thin launcher; all logic lives in install.py.
here="$(cd "$(dirname "$0")" && pwd)"
for py in python3 python py; do
  if command -v "$py" >/dev/null 2>&1 && "$py" --version >/dev/null 2>&1; then
    exec "$py" "$here/install.py" "$@"
  fi
done
echo "no working Python (python3 / python / py); install from python.org" >&2
exit 1
