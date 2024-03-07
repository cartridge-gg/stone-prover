```bash
podman build -t fibonacci-prover -f prover.dockerfile .
```

```bash
podman run -i --rm fibonacci-prover < program_input.json > proof.json
```

```bash
podman build -t verifier -f verifier.dockerfile .
```

```bash
podman run -i --rm verifier < proof.json
```

```bash
podman push fibonacci-prover:latest docker.io/username/fibonacci-prover:latest
```

```bash
podman push verifier:latest docker.io/username/verifier:latest
```
