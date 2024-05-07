FROM localhost/stone5-poseidon3:latest

RUN pip install cairo-lang==0.13.1

ENTRYPOINT [ "prover-entrypoint.sh" ]
