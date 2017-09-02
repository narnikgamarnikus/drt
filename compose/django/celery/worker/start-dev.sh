#!/bin/sh

set -o errexit
set -o nounset
set -o xtrace

celery -A drt.taskapp worker -l INFO
