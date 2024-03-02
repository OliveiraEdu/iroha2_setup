# Update package lists

FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
  libssl-dev \
  curl \
  build-essential \
  pkg-config \
  iputils-ping \
  nano \
  git \
  pip \
  patchelf

# Create Git directory and clone Iroha repository
RUN mkdir -p ~/Git && cd ~/Git && \
  git clone https://github.com/hyperledger/iroha.git --branch iroha2-lts

# Install Rust toolchain (nightly-2023-06-25)
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y \
  && source "$HOME/.cargo/env" \
  && rustup install nightly-2023-06-25 \
  && rustup target add wasm32-unknown-unknown --toolchain nightly-2023-06-25 \
  && rustup override set nightly-2023-06-25 \
  && rustup component add rust-src --toolchain nightly-2023-06-25

# Build Iroha client and create test directory
WORKDIR ~/Git/iroha
RUN cargo build -p iroha_client_cli --release
RUN mkdir -p test_docker

# Copy config and built client to test directory
COPY configs/client/config.json test_docker/
COPY target/release/iroha_client_cli test_docker/

# Set working directory for further commands (optional)
WORKDIR ~/Git/iroha/test_docker
