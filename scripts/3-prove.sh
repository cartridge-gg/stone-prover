#!/usr/bin/env bash

podman run -i --rm stone-prover-cairo0 < input.json > resources/proof.json
