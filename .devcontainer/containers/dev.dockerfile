FROM python:latest

# Install LaTeX and basic utilities
RUN apt-get update && apt-get install -y \
    texlive-full \
    make \
    git \
    curl \
    nano \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

USER $USERNAME
WORKDIR /workspaces