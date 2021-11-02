#!/usr/bin/env sh

set -e

export FLASK_APP=app
export FLASK_ENV=development
export FLASK_DEBUG=True

python -m flask run