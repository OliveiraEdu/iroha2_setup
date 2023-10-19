eduardo@blockchain:~/Git/iroha$ git show
commit da74b8c29f26670db5639503c5c141363aa05820 (HEAD -> iroha2-dev, origin/iroha2-dev)


eduardo@blockchain:~/Git/iroha$ docker compose -f docker-compose.dev.yml up

iroha-iroha1-1  | 2023-10-08T19:53:03.641739Z  INFO request{method=POST path=/query version=HTTP/1.1 remote.addr=192.168.208.1:45628}: warp::filters::trace: processing request
iroha-iroha1-1  | 2023-10-08T19:53:03.641796Z  INFO request{method=POST path=/query version=HTTP/1.1 remote.addr=192.168.208.1:45628}:request{method=POST path=/query version=HTTP/1.1 remote.addr=192.168.208.1:45628}: warp::filters::trace: processing request
iroha-iroha1-1  | 2023-10-08T19:53:03.641891Z  WARN request{method=POST path=/query version=HTTP/1.1 remote.addr=192.168.208.1:45628}:request{method=POST path=/query version=HTTP/1.1 remote.addr=192.168.208.1:45628}: warp::filters::trace: unable to serve request (client error) status=404 error=Some(Rejection(NotFound))
iroha-iroha1-1  | 2023-10-08T19:53:03.642450Z  WARN request{method=POST path=/query version=HTTP/1.1 remote.addr=192.168.208.1:45628}: warp::filters::trace: unable to serve request (client error) status=404 error=None


root@60a4ef221ae2:~/Git/iroha/test_docker# ./iroha_client_cli domain list all
Error: 
   0: Failed to get all domains
   1: Other error
   2: Failed to send http POST request to http://200.17.87.161:8081/query
   3: Io Error: Connection refused (os error 111)

Location:
   client_cli/src/main.rs:426



Backtrace omitted. Run with RUST_BACKTRACE=1 environment variable to display it.
Run with RUST_BACKTRACE=full to include source snippets

#-------

eduardo@blockchain:~/Git/iroha$ git branch
* iroha2-dev
  iroha2-lts
  iroha2-stable

eduardo@blockchain:~/Git/iroha$ nano docker-compose.dev.single.yml 

#0 573.6   running: "musl-g++" "-O3" "-ffunction-sections" "-fdata-sections" "-fPIC" "-m64" "-Wall" "-Wextra" "-o" "/iroha/target/x86_64-unknown-linux-musl/deploy/build/link-cplusplus-37414c682fb6de70/out/19ea84752e352604-dummy.o" "-c" "/iroha/target/x86_64-unknown-linux-musl/deploy/build/link-cplusplus-37414c682fb6de70/out/dummy.cc"
#0 573.6 
#0 573.6   --- stderr
#0 573.6 
#0 573.6 
#0 573.6   error occurred: Failed to find tool. Is `musl-g++` installed?
#0 573.6 
#0 573.6 
#0 573.6 warning: build failed, waiting for other jobs to finish...
------
failed to solve: executor failed running [/bin/sh -c cargo build  --target x86_64-unknown-linux-musl --features vendored --profile deploy]: exit code: 101




LTS
root@60a4ef221ae2:~/Git/iroha/test_docker# git branch
  iroha2-dev
* iroha2-lts
  iroha2-stable
root@60a4ef221ae2:~/Git/iroha/test_docker# 

 Compiling clap_lex v0.2.4
   Compiling console v0.15.1
   Compiling tungstenite v0.16.0
error: failed to run custom build command for `iroha_client v2.0.0-pre-rc.9 (/root/Git/iroha/client)`

Caused by:
  process didn't exit successfully: `/root/Git/iroha/target/release/build/iroha_client-8772db2a4d73b4d8/build-script-build` (exit status: 1)
  --- stdout
  cargo:rerun-if-changed=tests/integration/smartcontracts

  --- stderr
  error: toolchain 'nightly-2022-08-15-x86_64-unknown-linux-gnu' is not installed
  Error: Failed to build smartcontracts in directory: tests/integration/smartcontracts

  Caused by:
     0: Failed to build the smartcontract
     1: `cargo build` returned non zero exit code (exit status: 1) then trying to build smartcontract at path `/root/Git/iroha/client/tests/integration/smartcontracts/mint_rose`

  Location:
      client/build.rs:135:20
warning: build failed, waiting for other jobs to finish...
warning: `iroha_data_model` (lib) generated 1 warning



