#!/usr/bin/env bash

podman run -i --rm localhost/stone-cairo:recursive < resources/cairo/example.json > resources/cairo/proof.json
echo "Proof generated in resources/cairo/proof.json"