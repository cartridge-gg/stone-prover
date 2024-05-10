```bash
podman build -t stone5-poseidon3 .
```

```bash
podman push localhost/stone5-poseidon3:latest docker.io/username/stone5-poseidon3:latest
```

```bash
podman run -i --rm stone5-poseidon3 < input.json > proof.json
```
