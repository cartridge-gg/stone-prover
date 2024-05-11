#!/usr/bin/env bash

source .venv/bin/activate && \
mkdir -p resources && \
cairo-compile \
  program.cairo \
  --output resources/compiled.json \
  --proof_mode && \
deactivate
