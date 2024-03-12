```bash
podman build -t prover -f prover.dockerfile .
```

```bash
podman run -i --rm prover < program_input.json > proof.json
```

```bash
podman build -t verifier -f verifier.dockerfile .
```

```bash
podman run -i --rm verifier < proof.json
```

```bash
podman push localhost/prover:latest docker.io/username/prover:latest
```

```bash
podman push localhost/verifier:latest docker.io/username/verifier:latest
```
