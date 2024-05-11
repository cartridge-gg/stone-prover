# Project Setup and Deployment Guide

Welcome to our project documentation. This guide provides detailed instructions on setting up your local environment, compiling the project, building the necessary components, and verifying the build through proof scripts. Additionally, we include instructions on pushing the final build to a Docker repository using Podman. Please follow these steps in sequence to ensure a smooth setup and deployment process.

## Scripts Execution

To get started, you need to execute a series of scripts that prepare your environment and compile the necessary components of the project. Below is the order in which the scripts should be executed:

1. **`0-venv.sh`**: This script sets up the virtual environment for the project. It ensures that all dependencies are isolated and managed without affecting other projects on your system.

2. **`1-compile.sh`**: Run this script to compile the source code into an executable format. It handles any necessary preprocessing and prepares the code for the next stages of the build process.

3. **`2-build.sh`**: This script builds the project from the compiled sources. It creates the necessary binaries or libraries that are required for the project to run.

4. **`3-prove.sh`**: Finally, execute this script to verify the build. It runs tests or proofs to ensure that the build meets all specified requirements and behaves as expected.

## Pushing to Docker Repository Using Podman

Once you have verified the build, you can push the project to a Docker repository. The following command utilizes Podman, a container management tool, to push the build to your Docker.io repository:

```bash
podman push localhost/stone-prover-cairo0:latest docker.io/username/stone-prover-cairo0:latest
```

### Command Explanation

- `podman push`: This command tells Podman to push a container image.
- `localhost/stone-prover-cairo0:latest`: Specifies the local image to push. Replace `stone-prover-cairo0` with the name of your local image.
- `docker.io/username/stone-prover-cairo0:latest`: Indicates the remote Docker repository to which the image should be pushed. Replace `username` with your Docker.io username.

Ensure that you are logged into your Docker.io account and have the necessary permissions to push to the repository.
