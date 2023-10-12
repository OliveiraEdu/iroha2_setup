apt update
apt-get install -y libssl-dev curl build-essential pkg-config iputils-ping nano git pip patchelf nano

git clone https://github.com/hyperledger/iroha.git --branch iroha2-lts
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source "$HOME/.cargo/env"

#--- Updating rust toolchain
rustup install nightly-2023-06-25
rustup target add wasm32-unknown-unknown --toolchain nightly-2023-06-25
rustup override set nightly-2023-06-25
rustup component add rust-src --toolchain nightly-2023-06-25

# --- Installing the Bash Client
cd ~/Git/iroha
cargo build -p iroha_client_cli --release
mkdir -p test_docker
cp ./configs/client/config.json test_docker/
cp ./target/release/iroha_client_cli test_docker/
cd ~/Git/iroha/test_docker

