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




