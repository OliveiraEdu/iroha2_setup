    1  apt update
    2  apt-get install -y libssl-dev curl build-essential pkg-config iputils-ping nano git pip patchelf nano
    3  root/
    4  mkdir Git
    5  Git/
    6  git clone https://github.com/hyperledger/iroha.git --branch iroha2-lts
    7  curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
    8  source "$HOME/.cargo/env"
    9  rustc --version
   10  cargo - V
   11  cargo -V
   12  cd iroha/
   13  git status
   14  git checkout 9273a912c8a97f9ce1bfaa302c7192554f7abf00
   15  git status
   16  git statuscd iroha/
   17  ls
   18  cargo build -p iroha_client_cli --release
   19  cd ..
   20  git clone https://github.com/hyperledger/iroha-python/ --branch iroha2-edge
   21  cd iroha-python/
   22  pip install maturin
   23  maturin buil
   24  maturin build
   25  pip install ./target/wheels/iroha_python-*.whl
   26  cp -vfr ~/Git/iroha/configs/client/config.json example/config.json
   27  cd ..
   28  ls
   29* cp /iroha
   30  cp -vfr /iroha/configs/client/config.json example/config.json
   31  cp -vfr /iroha/configs/client_cli/config.json example/config.json
   32  cp -vfr /iroha/configs/client_cli/config.json .
   33  nano test.py 
   34  pip install jupyter
   35  jupyter notebook --allow-root
   36  ifconfig
   37  ip route
   38  hostname
   39  python3
   40  nano config.json 
   41  python3 test.py 
   42  ping 200.17.87.161
   43  nano config.json 
   44  python3 test.py 
   45  history 
   46  ls
   47  nano test.py 
   48  cp test.py test1.py
   49  nano test1.py 
   50  python3 test1.py 
   51  nano test1.py 
   52  history 
   53  history > hist.txt

