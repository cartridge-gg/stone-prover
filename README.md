```bash
podman build -t stone5-poseidon3 -f prover.dockerfile .
```

```bash
podman push localhost/stone5-poseidon3:latest docker.io/username/stone5-poseidon3:latest
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
podman push localhost/verifier:latest docker.io/username/verifier:latest
```
