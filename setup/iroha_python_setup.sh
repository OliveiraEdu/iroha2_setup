#succesfull setup for Iroha Python 17OCT2023
apt update
apt-get install -y libssl-dev curl build-essential pkg-config iputils-ping nano git pip patchelf nano
mkdir -p ~/Git
cd ~/Git
git clone https://github.com/hyperledger/iroha.git --branch iroha2-lts
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source "$HOME/.cargo/env"
rustc --version
cargo -V
cd ~/Git/iroha
git status
git checkout 9273a912c8a97f9ce1bfaa302c7192554f7abf00
git status
cargo build -p iroha_client_cli --release
cd ~/Git
git clone https://github.com/hyperledger/iroha-python/ --branch iroha2-edge
cd ~/Git/iroha-python
pip install maturin
maturin build
pip install ./target/wheels/iroha_python-*.whl
cp -vfr ~/Git/iroha/configs/client_cli/config.json example/config.json
pip install icecream
