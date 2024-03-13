```bash
podman build -t stone5-poseidon -f prover.dockerfile .
```

```bash
podman run -i --rm stone5-poseidon < program_input.json > proof.json
```

```bash
podman build -t example-program -f example-program.dockerfile .
```

```bash
podman run -i --rm example-program < program_input.json > proof.json
```

```bash
podman run -i --rm verifier < proof.json
```

```bash
podman push localhost/stone5-poseidon:latest docker.io/username/stone5-poseidon:latest
```

```bash
podman push localhost/verifier:latest docker.io/username/verifier:latest
```
